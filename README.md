# OMEGA X

Windows 반응 속도 최적화 도구. 지금 쓰는 앱에 CPU·디스크 우선순위를 몰아주고, 백그라운드 앱은 절전 모드(EcoQoS)·메모리 우선순위 하향으로 뒤로 미룹니다. 모든 변경은 종료 시 원래대로 되돌립니다.

A Windows responsiveness tool. It prioritises the app you are using and eases off background apps (EcoQoS, lower memory priority). Every change is reverted on exit.

- 화면에 나오는 수치는 전부 이 PC에서 실제로 잰 값입니다. "몇 % 빨라졌다"는 말은 하지 않습니다.
- 벤치마크 점수는 거의 변하지 않습니다(보통 2% 미만). 체감되는 건 입력·전환 반응입니다.
- 서버로 보내는 데이터는 없습니다. 인터넷은 GitHub 업데이트 확인에만 씁니다.

## 요구 사항

- Windows 10 1607 이상 (EcoQoS 등 일부 기능은 Windows 11 22H2 이상)
- Python 3.10 이상
- 최대 부스트 등 일부 기능은 관리자 권한 필요 (필요할 때만 UAC로 요청)

## 실행

```
pip install -r requirements.txt
python dsafg.py
```

`version.txt` 가 `dsafg.py` 와 같은 폴더에 있어야 합니다. 없거나 형식이 깨지면 앱이 일부러 실행되지 않습니다.

## 빌드 (PyInstaller)

```
pip install pyinstaller
pyinstaller --onefile --windowed --name OMEGA_X --add-data "version.txt;." dsafg.py
```

`--add-data "version.txt;."` 를 빠뜨리면 빌드된 EXE가 실행되지 않습니다. 빌드 후 검증:

```
dist\OMEGA_X.exe --selftest=result.txt;<version.txt의 버전>
```

`result.txt` 첫 줄이 `OK` 면 정상입니다.

## 주의

- 일부 온라인 게임의 안티치트가 우선순위 변경을 비정상 행위로 볼 수 있습니다. 사용 책임은 사용자에게 있습니다.
- 되돌리지 않는 변경: GameDVR(게임 녹화) 끄기, 사용자가 직접 실행한 임시 파일 삭제·휴지통 비우기·시작프로그램 제거·프로세스 종료. 첫 실행 동의 화면에 전부 적혀 있습니다.
- 코드 서명이 없어 SmartScreen 경고가 뜰 수 있습니다.

## 버그 신고 · 기여

- 버그·제안: GitHub Issues (Windows 버전과 `%APPDATA%\OMEGA_X\error.log` 첨부)
- 보안 취약점: [SECURITY.md](SECURITY.md)
- 기여 방법: [CONTRIBUTING.md](CONTRIBUTING.md)

## 라이선스

Copyright (C) 2026 서주원 (Seo Juwon) / OMEGA SYSTEMS

[GNU General Public License v3.0 or later](LICENSE) (SPDX: `GPL-3.0-or-later`).
사용·수정·재배포 자유, 상업적 이용 포함. 배포할 때는 같은 GPL 조건과 전체 소스 코드를 함께 제공해야 합니다.
이 프로그램은 어떠한 보증도 없이 제공됩니다.

사용한 외부 라이브러리와 라이선스: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

문의: seodes105@gmail.com · https://pinnn.me/@seodes105
