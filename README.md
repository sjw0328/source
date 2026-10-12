# OMEGA X

[![OpenSSF Baseline](https://www.bestpractices.dev/projects/15412/baseline)](https://www.bestpractices.dev/projects/15412)

Windows 반응 속도 최적화 도구. 지금 쓰는 앱에 CPU·디스크 우선순위를 몰아주고, 백그라운드 앱은 절전 모드(EcoQoS)·메모리 우선순위 하향으로 뒤로 미룹니다. 대부분의 변경은 기능을 끄거나 앱을 종료할 때 되돌리도록 만들어져 있습니다(예외는 아래 "주의" 참고).

A Windows responsiveness tool. It prioritises the app you are using and eases off background apps (EcoQoS, lower memory priority). Most changes are designed to be reverted when you turn the feature off or exit (exceptions below).

- 화면의 수치는 이 PC에서 측정한 값이며, 정확성이나 성능 향상을 보장하지 않습니다.
- 개발자는 데이터를 수집하는 서버를 운영하지 않습니다. 앱은 업데이트를 확인·다운로드할 때 GitHub에 접속하며, 이 과정에서 GitHub에 전달되는 정보(IP 주소, 앱 버전이 담긴 User-Agent 등)는 GitHub의 정책을 따릅니다.

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

기능별 사용법: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)

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

- 이 프로그램은 Windows 설정과 프로세스를 실제로 변경합니다. 사용 전 중요한 데이터를 백업하십시오.
- 비정상 종료·강제 종료·전원 차단 시 일부 변경이 남을 수 있습니다. 다음 실행 때 되돌리도록 시도하지만 보장하지 않습니다.
- 되돌리지 않는 변경: GameDVR(게임 녹화) 끄기, 사용자가 직접 실행한 임시 파일 삭제·휴지통 비우기·시작프로그램 제거·프로세스 종료.
- 일부 온라인 게임의 안티치트가 우선순위 변경을 비정상 행위로 판단할 수 있습니다.
- 코드 서명이 없어 SmartScreen 경고가 뜰 수 있습니다.

## 면책

이 소프트웨어는 "있는 그대로(AS IS)" 제공되며, 상품성·특정 목적 적합성·무결함을 포함한 어떠한 명시적·묵시적 보증도 하지 않습니다. 사용에 따른 모든 위험과 책임은 사용자에게 있습니다. 관련 법령이 허용하는 최대 범위에서, 저작권자는 이 소프트웨어의 사용 또는 사용 불능으로 발생한 어떠한 직접·간접·부수적·결과적 손해(데이터 손실, 시스템 장애, 계정 제재 포함)에 대해서도 책임지지 않습니다. 자세한 내용은 GPL 제15조·제16조를 따릅니다.

## 버그 신고 · 기여

- 버그·제안: GitHub Issues (Windows 버전과 `%APPDATA%\OMEGA_X\error.log` 첨부)
- 보안 취약점: [SECURITY.md](SECURITY.md)
- 기여 방법: [CONTRIBUTING.md](CONTRIBUTING.md)

## 라이선스

Copyright (C) 2026 서주원 (Seo Juwon) / OMEGA SYSTEMS

[GNU General Public License v3.0 or later](LICENSE) (SPDX: `GPL-3.0-or-later`).
사용·수정·재배포 자유, 상업적 이용 포함. 배포할 때는 같은 GPL 조건과 전체 소스 코드를 함께 제공해야 합니다.

사용한 외부 라이브러리와 라이선스: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

문의: seodes105@gmail.com · https://pinnn.me/@seodes105
