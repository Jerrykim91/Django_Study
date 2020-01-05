# 장고(Django)_02

## - Index
- 개발 환경<br/>
    - 파이썬, 장고, 데이터 베이스<br/>

1. 파이썬 설치<br/>
2. 장고 설치<br/>
3. 데이터베이스 설치<br/>
        - SQLite(추천)<br/>
    - 메모리에 상주하는 프로세스 없이 파일 하나에 데이터베이스를 저장 <br/>
4. 장고 프로젝트 만들기<br/>
    - URL과 뷰(views): 메인 페이지를 생성<br/>
        - 페이지를 만들기 위해서는 URL로 표현된 형식을 이용해서 파이썬 함수와 애플리케이션을 연결     <br/>
        - 뷰는 페이지를 호출하면 그 응답으로 페이지를 만들어주는 파이썬 함수   <br/>
        - 장고 애플리케이션을 프로젝트 아래에 생성 => 애플리케이션은 뷰와 데이터 모델(data model)의 묶음     <br/>

5. 데이터베이스 설정 <br/>
6. 장고 개발 서버 실행  <br/>
7. 새로운 프로젝트 실행 <br/>
8. 프로젝트의 데이터 베이스를 생성하고 관리 <br/>
9. 프로젝트 상태를 테스트 <br/>
10. 개발용 웹 서버를 실행<br/>


## 기본 구조
```py
Django web project
    ㄴ Web01
        - 프로젝트 설계를 위한 python 패키지들 이저장    
        ㄴ __init__.py 
            - 디렉토리를 패키지처럼 다루라고 알려주는 파일 
            => 이름이 중복되는것을 피하게 하는 모듈의 모음 
        ㄴ setting.py 
            - 프로젝트의 환경 및 구성을 저장
            - 환경 설정이 어떻게 동작하는지 확인
            - 데이터베이스, 사이트 언어 설정 
        ㄴ urls.py
            - 설정파일 
                - 현재 Django project 의 URL 선언을 저장 => 사이트의 '목차'
                - url주소와 장고의 기능을 연결 시켜주는 역활 
                - 장고의 강력한 기능**
    ㄴ manage.py
        - 프로젝트를 관리하는 스크립트 admin.py와 코드를 공유 
```


### - Step 01 
- Newproject 생성    
    - conda istall Django  =>  Django 모듈 설치(없다면)    
    - Newproject 생성     
        - 확인 할 부분!! manage.py있는지 확인    
        - 잘 생성 되었으면 생성한 프로젝트 폴더로 이동    


```py   
# Istall Django Web
$ cd C:\web_project\web01
- 설치 하고자 했던 위치로 폴더 이동     
    - 예시) 자기 폴더 위치 C에 생성하시오 => 빠르고 편함     
        - My_Path01 [C:\web_project\web01]     
        - My_Path02 [C:\web_project\web_re]     
 
# Django 모듈 설치( if 모듈이 없다면! 설치_conda OR pip whatever you want)
    $ conda install django     

# Newproject 생성(원하는 이름(whatever you want)의 폴더를 생성)
    $ django-admin startproject Newproject   

# 확인 할 부분 !! manage.py있는지 확인 잘 생성 되었으면 다음 step으로 이동 
    # 생성한 프로젝트 폴더로 이동
    $ cd Newproject 

# Board 앱 생성(여러개 생성 가능)
    $ django-admin startapp board
# 의문사항 => 직접해보자 
    $ django-admin.py startapp member  => 어플리케이션 생성 
    $ django-admin startproject member => 프로젝트폴더 생성시에 사용
# Member 앱 생성
    $ django-admin startapp member 
# Django 서버 구동(http://127.0.0.1:8000/)
    $ python manage.py runserver 

# DB 연동=> SET IT UP**
    $ python manage.py migrate
```


### - Step 02 
 - 사용자가 상위 URL(http://127.0.0.1:8000)을 요청 <br/>
    => 장고는 urls.py에 정의된 urlpatterns에서 요청(request)값과 일치하는 URL을 찾아 낸다 
 - URL를 찾아내면 그에 해당하는 뷰를 호출<br/>
 - 파이썬 함수인 뷰는 사용자 브라우저가 보낸 데이터를 request객체로 받아서 HttpResponse객체에 페이지 내용을 담아서 반환<br/>


### - Step 03


2. cursor() => 함수 확인 



