# mini tutorial
---

출처 - https://swarf00.github.io/2018/11/23/setup-project.html

---

```bash

minitutorial/            # main root 디렉토리
├── manage.py            # 유틸리티
└── minitutorial/        # 실제 프로젝트 디렉토리/ 프로젝트의 설정/ 파이썬패키지로 사용
    ├── __init__.py      # 파이썬패키지 필수 초기화 파일= > 가장 먼저 실행되는 스크립트
    ├── settings.py      # 설정 파일
    ├── urls.py          # 웹 url들을 view와 매칭시켜주는 파일
    └── wsgi.py          # WSGI 
    board/
    ├── __init__.py      # 패키지 초기화
    ├── admin.py         # admin setting 파일 => 등록된 모델-> 자동 생성하는 admin page에서 관리
    ├── apps.py          # 앱 설정 파일
    └── migrations/      # DB migrations 디렉토리 => 스키마의 변화가 생길 때마다 migration 파일을 생성 -> 스키마를 업데이트
        ├── __init__.py  # migrations 패키지 초기화 
        models.py        # model 파일 board의 모든 데이터를 저장할 DB를 매핑해서 모델화
        ├── tests.py     # 기능들을 test하는 기능을 구현
        └── views.py     # 요청을 처리하여 모델에 저장 / 모델에 저장된 데이터를 화면에 전달


```