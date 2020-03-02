# Summary
---
# 장고(Django)

1. 구성요소들 간의 긴밀한 통합 
    - 장고는 각 요소가 긴밀하게 통합되어 있음  
    - 모든 부분이 통합적(integration)이며 동작이 빠르다. 그리고 재사용 가능하게 설계   

2. 객체 관계의 매핑     
    - 객체 관계의 매핑(Object-Relational Mapper, ORM))이란     
        : 데이터 베이스 엔진과 데이터 모델을 연결시키는 다리와 같은 역활     
    - 다양한 데이터 베이스를 지원, 유연한 데이터 베이스 시스템 변경     
    - 장고는 데이터베이스를 일관성 있게 추상화해서 단일한 API로 여러 데이터베이스를 사용      

3. 간단한 URL 주소 설계    
    - 강력하고 유연한 URL 주소 디자인  
         - URL주소 형태를 직접 결정 
    - 파이썬 함수를 각 주소 형태와 직접 연결 
        - 일반 사용자와 검생 엔진 각각에 알맞는 결과를 제공 

4. 자동으로 구성되는 관리자 화면 
    - 장고는 실행하는 순간 미리 내장되어 있는 관리자 화면 제공 
    - 여러 어플리케이션의 데이터를 쉽게 관리, 재구성 

5. 풍부한 개발 환경
    - 가벼운 웹 서버를 포함하고 있고 개발뿐아니라 테스트 용도로 사용가능 
    - 디버깅 모드를 사용 할 경우 장고는 문제를 쉽게 파악하고 해결 할 수 있게 상세한 에러 메세지를 보여줌 

6. 이외
    - 간단하고 확장 할 수 있는 템플릿 텍스트 처리 엔진 (template and text filtering engine)
    - 폼을 만들고 사용자 입력을 검사하는 유효성 검사 API
    - 확장할 수 있는 인증 시스템 
    - 성능 향상에 도움이 되는 캐싱 시스템 
    - RSS 피드를 만들어주는 피드 시스템(feed framework)




---
# 오라클 서버 구동

```
$ docker ps -a # 컨테이너 실행 확인
$ docker start oracle12c  # 컨테이너 구동
$ docker ps -a
```

# DB 연동(1회만) 

```
$ python manage.py migrate
$ python manage.py runserver
```

# 오라클 서버 셧다운
```
$ docker stop oracle12c
$ docker-machine stop
```

---

### 오라클 세팅 
```bash

# 오라클12c 설치- 오라클 이미지 검색 
$ docker search oracle-12c
$ docker pull truevoly/oracle-12c

# 이미지확인 => 5.7GB
$ docker images

# 최초 시작시- 컨테이너 만들기 
$ docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c
# (주기적으로 log를 확인하여 100%가 될때까지 기다려야됨.)
$ docker logs oracle12c
```

### 재시작 
```bash
# 구동중인 컨테이너 실행 확인
$ docker ps -a
# 도커 실행 하기
$ docker start oracle12c
# 도커 종료 하기
$ docker stop oracle12c
# 도커 종료
$ docker-machine stop
```

### 필요시
```bash
# 옵션) 데이너 실행 중지
$ docker stop oracle12c 
# 옵션) 컨테이너 삭제
$ docker rm oracle12c 
```


### 몽고디비 세팅 
```bash
# 이미지 검색
$ docker search mongo 
# 이미지 가져오기 
$ docker pull mongo  
# 이미지 확인
$ docker images   

# 컨테이너 생성
# 인증을 통해 생성 => 빼면 (-auth) 아무나 접속 가능 
$ docker run --name mongodb -d -p 32766:27017 mongo -auth   
# 인증없이 생성
$ docker run --name mongodb -d -p 32766:27017 mongo   
# 설치시 로그 확인 (수시로)
$ docker logs mongodb         

# 컨테이너 삭제(필요시)
$ docker stop mongodb
$ docker rm mongodb

```

####  추가로 
[Robo 3T 다운링크](https://robomongo.org/download)     
- Robo 3T 1.3 압축파일로 다운로드 (스튜디오x)     
- robomongo 초기 세팅 => 도커랑 연결하기 위한 주소      
    - **Connection setting**     
    ```192.168.99.100``` : ```32766```

```bash
# 라이브러리 생성 
$ pip install pymongo
```


---

## 프로젝트 기본 구조 생성 

- 기본 초기세팅으로 도커에 오라클 oracle12c와 mongodb 설치가 되어있다고 가정한다.

```bash
# 오라클 디비 구동 및 종료
$ docker start oracle12c
$ docker stop oracl12c

# 몽고 디비 구동 및 종료
$ docker start mongodb
$ docker stop mongodb

# 도커 구동 및 종료
$ docker-machine stop
$ docker-machine start
```
---

### stp 1 

```bash
# 프로젝트 생성
$ django-admin startproject 프로젝트이름
# 애플리케이션 생성
$ django-admin startapp 앱 이름 
# 디비 연동
$ python manage.py migrate
# 런서버
$ python manage.py runserver

# 폴더 생성
- templates / 각 어플네임
- static /css

```
---

## stp 2

```py
# setting 설정 

# 어플 추가 하기 (모델 생성 하는것만 )
INSTALLED_APPS =[] 
# 템플릿 절대경로 추가 
TEMPLATES = ['DIRS': [os.path.join(BASE_DIR), 'templates'], ] 
# 디비 계정 추가 
DATABASES = {
    'default': {

            # oracle (예시)
            # 'ENGINE': 'django.db.backends.oracle',
            # 'NAME': 'xe', #SID
            # 'USER': 'admin',
            # 'PASSWORD' : '1234',
            # 'HOST' : '192.168.99.100',
            # 'PORT' : '32764'
    }
} 

# 스테틱 절대경로 추가
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
---
 
## stp 3

```py
# 상위 urls.py에 내용추가 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # include로 경로 생성할때 마다 => 각 어플경로에 하위 urls.py 생성
    path('어플이름/', include('어플이름.urls')),

]
```
---

## stp 4 

- 각 어플에 설계한 모델을 생성 후 아래 코드를 커맨드창에 실행 

```bash
# 에러확인
$ python manage.py check 
# 장고에 자료생성
$ python manage.py makemigrations 어플이름
# 디비로 전달
$ python manage.py migrate 어플이름
```
- 디비와 연동을 확인후 작업을 시작할것 
---
