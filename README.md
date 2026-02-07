# MT48 Volume Indicator

MT48 웹 UI의 볼륨 데이터를 실시간으로 파싱하여 화면 우측 하단에 표시해주는 도구입니다.

## 📝 주요 기능 (Features)
* **실시간 볼륨 모니터링:** 웹 UI에서 볼륨 값을 추출하여 오버레이 형태로 표시합니다.

## ⚠️ 요구 사항 및 제약 사항 (Requirements & Limitations)
* **웹 앱 링크 설정:** 프로그램 실행 전, 반드시 `config.json` 파일을 열어 본인의 **MT48 웹 앱 주소**에 맞게 수정해야 정상적으로 작동합니다.
* **링크 설정 예시**: http://111.222.333.444/MT48_music/index.html (반드시 index.html까지 포함)
* **Google Chrome:** 본 프로그램 작동을 위해 크롬 브라우저가 반드시 설치되어 있어야 합니다.
* **제약사항:** 현재 버전은 **1번 채널**만 지원합니다.

## 🛠 빌드 방법 (Build Instruction)
`pyinstaller_command.txt` 파일에 포함된 명령어를 사용하여 직접 실행 파일(`.exe`)을 빌드할 수 있습니다.

## 🌐 English Description
Parses volume values from the MT48 Web UI and displays them in the bottom-right corner of the screen.

* **Requirement:** Chrome browser must be installed.
* **Note:** Currently, only **Channel 1** is supported.
* **Build:** Use the command in `pyinstaller_command.txt` to create an executable file.
