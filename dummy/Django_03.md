# Django == Chapter 03
---
# 장고(Django)_03

## - Index
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
    $ django-admin.py startapp NAME  => 어플리케이션 생성 
    $ django-admin startproject NAME => 프로젝트폴더 생성시에 사용
# Member 앱 생성
    $ django-admin startapp member 
# Django 서버 구동(http://127.0.0.1:8000/)
    $ python manage.py runserver 

# DB 연동=> SET IT UP**
    $ python manage.py migrate
```

