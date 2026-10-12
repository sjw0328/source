# Third-Party Notices

OMEGA X 는 아래 라이브러리를 사용합니다. 각 라이브러리는 해당 라이선스를 따르며, 모두 GPL-3.0 과 호환됩니다.
PyInstaller 로 빌드한 실행 파일에는 이 라이브러리들이 포함되므로, 실행 파일을 배포할 때는 이 문서와 각 라이선스 전문을 함께 제공해야 합니다.

| 라이브러리 | 라이선스 | 출처 |
|---|---|---|
| CustomTkinter | MIT | https://github.com/TomSchimansky/CustomTkinter |
| darkdetect (CustomTkinter 의존) | BSD-3-Clause | https://github.com/albertosottile/darkdetect |
| psutil | BSD-3-Clause | https://github.com/giampaolo/psutil |
| requests | Apache-2.0 | https://github.com/psf/requests |
| urllib3 (requests 의존) | MIT | https://github.com/urllib3/urllib3 |
| certifi (requests 의존) | MPL-2.0 | https://github.com/certifi/python-certifi |
| charset-normalizer (requests 의존) | MIT | https://github.com/jawah/charset_normalizer |
| idna (requests 의존) | BSD-3-Clause | https://github.com/kjd/idna |
| packaging | Apache-2.0 OR BSD-2-Clause | https://github.com/pypa/packaging |
| Python / Tkinter | PSF License | https://www.python.org/ |

라이선스 전문은 각 패키지에 동봉되어 있습니다(`pip show -f <패키지명>` 으로 위치 확인).
requests 가 Apache-2.0 이므로 이 프로젝트는 GPL 제2판이 아니라 제3판 이상으로만 배포합니다.
