import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import json

#----------------------config----------------------
import sys, os
application_path = ''
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
print(application_path)

config_path = os.path.join(application_path, 'config.json')
with open(config_path) as f:
    config = json.load(f)
webapp_url = config['WebApp']
print(webapp_url) # value_last

#----------------------UI----------------------
# create window
window = tk.Tk()

# adjust size
width = 300
height = 150
window.geometry("250x100-0-47")
window.overrideredirect(True)

bg_color = '#7f7c81'
label=tk.Label(text='Loading...',
               font=("Calibri", 30, "bold"),
               fg='#fff',
               bg=bg_color)
window.configure(background=bg_color)
label.pack(expand=True)

# always on top
window.attributes('-topmost', True)

window.update()

#----------------------Selenium----------------------
chrome_options = Options()
chrome_options.add_argument('--headless=new') # for Chrome >= 109
chrome_options.add_argument("--window-position=-2400,-2400")
driver = webdriver.Chrome(options=chrome_options)

def millis():
    return round(time.time() * 1000)

def get_db_text():
    js = "return document.getElementById('bus2-mastergain-value').innerHTML"
    db_i = driver.execute_script(js)
    js = "return document.getElementById('bus2-mastergain-decimal').innerHTML"
    db_d = driver.execute_script(js)
    db_text = db_i + db_d + ' dB'
    return db_text


#----------------------main loop----------------------
ms = 0
db_text = ''
db_text_new = ''
refresh_flag = False
while True:
    # try getting decibel data from website
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'popUpOverlay')))
        db_text_new = get_db_text()
        js = "return document.getElementById('popUpOverlay').getAttribute('style')"
        style = driver.execute_script(js)
        if style == 'display: flex;':
            refresh_flag = True
    except:
        refresh_flag = True

    if refresh_flag:
        try:
            driver.get(webapp_url)
            time.sleep(2)
            refresh_flag = False
        except:
            continue
        
    # update ui
    if db_text != db_text_new:
        window.deiconify()
        label.config(text=(db_text_new))
        db_text = db_text_new
        ms = millis()
    else:
        time_diff = millis() - ms
        if time_diff > 700:
            window.withdraw()
    
    window.update()


