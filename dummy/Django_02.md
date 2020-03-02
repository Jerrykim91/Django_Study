# **Django_Chapter 02**
---

## - Index
- 개발 환경<br/>
    - 파이썬, 장고, 데이터 베이스<br/>

    ### 아웃라인 순서  
    Step - 1 
    프로젝트 뼈대 만들기 
    Step - 2
    모델 코딩하기
    Step - 3 
    URLconf 코딩하기
    Step - 4 
    템플릿 코딩하기
    Step - 5 
    뷰 코딩하기 

# 애플리케이션 설계하기 
 <화면 UI 설계>
 - 템플릿 설계 
    - index.html
        - 질문 리스트를 보여줌 
    - detail.html
        - 하나의 질문에 대해 투표 할수 있도록 답볍 항목을 폼으로 보여줌 
    - results.html
        - 질문에 따른 투표 결과를 보여줌 

- 테이블 설계 
 -모든 컬럼은 not-null정의, 컬럼 값이 있어야함 
 - pk 자동 증가 속성으로 지정 
 - Choice테이블의 question 컬럼은  Question 테이블과 연결 => index에 생성 
    - Question 테이블 설계 : 질문을 저장하는 테이블 
        + id - int - notnull, pk - pk
        + question_text - char - notnull- 질문문장
        + pub_date  -datetime - notnull- 질문 생성 시각

    - Choice 테이블 설계 : 질문별로 선택용 답변 항목을 저장하는 테이블  
        + id 
        + Choice_text
        + votes
        + question


# Step01 - 프로젝트 뼈대 생성 

## 기본 구조
```py
Django New project
    ㄴ New project
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
        ㄴ wsgi.py
            - WSGI 규격으로 연동하기 위한 파일 
    ㄴ manage.py
        - 프로젝트를 관리하는 스크립트 admin.py와 코드를 공유 
```

    - 프로젝트 생성 
        - Newproject 생성    
            - conda istall Django  =>  Django 모듈 설치(없다면) 

            
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


        - 확인 할 부분!! manage.py있는지 확인    
        - 잘 생성 되었으면 생성한 프로젝트 폴더로 이동    

    - 애플리케이션 생성 
    - 프로젝트 설정 파일 변경 
        - setting.py에 필요한 설정값 지정 
        - 확인해야할 4가지 
            1. ALLOWED_HOSTS      
                => 운영 모드인경우 서버의 IP나 도메인을 지정, 개발 모드에 지정하지 않아도 됨        
            2. INSTALLED_APPS    
                => 프로젝트에 포함되는 어플리케이션을 등록 => 모듈명만등록해도 됨 
                => 설정 클래스를 찾을수 있게 모듈 경로까지 포함하여 등록하기를 추천     
            3. DATABASES      
                => 프로젝트에 사용할 데이터베이스 엔진 설정    
            4. TIME_ZONE = 'UTC'     
                => 타임 존 지정     
    - 기본 테이블 생성      
        - ```$ python manage.py migrate```     
        - 이 명령이 필요한 이유 => 안하면 서버 안 열림      
            => 장고는 모든 웹 프로젝트 개발 시 반드시 사용자와 그룹 테이블 등이 필요하다는 가정하에 설계        
    - 지금까지 작업 확인     
       - runserver 실행 방법 
        ㄴ테스트용 웹 서버인 runserver를 다음과 같이 실행가능 
            - ```$ python manage.py runserver ```
            ㄴ 주소를 지정하지 않으면 디폴트로 8000번에 지정
            - ```$ python manage.py runserver 8888```
            ㄴ 포트번호만 지정하면 지정한 주소(8888)를 사용  
            - ```$ python manage.py runserver 0.0.0.0:8080 ```
# Step02 - 애플리케이션 개발하기 - MODEL 코딩 
# Step03 -  애플리케이션 개발하기 - VIEW 및 TEMPLATE코딩 


