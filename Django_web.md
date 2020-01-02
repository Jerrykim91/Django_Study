# Django WEB 
---
## 장고(Django)

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

## 구조 파악
```
Django web project
    ㄴ Web01(127.0.0.1:8000/board/index)
        => 공통으로 통제하기 수월함
        ㄴ urls.py
            ㄴ 설정 파일 
                - url주소와 장고의 기능을 연결 시켜주는 역활 
        ㄴ setting.py
            ㄴ 설정 파일 
                - DB
                - 사이트 언어
    ㄴ manage.py
    ㄴ Member
        ㄴ views.py (함수형 뷰)
        ㄴ urls.py  (함수형 뷰 호출 => member/views.py로부터)
        ㄴ models.py
    ㄴ Static (CSS)
        ㄴ CSS
    ㄴ Templates(HTML)
        ㄴ member
            ㄴ index.html
    ㄴ Board(app폴더)
        ㄴ views.py 
        ㄴ urls.py  
        ㄴ models.py  
    ㄴ Blog 
```
---
## - Index
- 개발 환경
    - 파이썬, 장고, 데이터 베이스
        1. 파이썬 설치
        2. 장고 설치
        3. 데이터베이스 설치
                - SQLite(추천)
            - 메모리에 상주하는 프로세스 없이 파일 하나에 데이터베이스를 저장 
        4. 장고 프로젝트 만들기
        - **Step01**
            - 터미널 => ```django-admin.py startproject 프로젝트이름```
            - 현재 디렉터리에 '프로젝트이름'을 만들고 기본파일을 자동 설치
        - **Step02**
            - Web 요소 구성하기  
            - 어플리케이션 생성 (여러개 생성 가능)   
                - Board, Member 앱 생성     
            - Django 서버 구동(http://127.0.0.1:8000/) 
        - **Step 03**
            - Member 기능 추가 
                1.  INDEX, LOGIN, Singin 페이지 등등 생성
        5. 데이터베이스 설정 
        6. 장고 개발 서버 실행  
        7. 새로운 프로젝트 실행 
        8. 프로젝트의 데이터 베이스를 생성하고 관리 
        9. 프로젝트 상태를 테스트 
        10. 개발용 웹 서버를 실행합니다.
---
 
## > Step 01     
- Web 폴더 생성     
    - Istall Django Web     
        - Django 모듈 설치(없다면)    
    - Newproject 생성     
        - 확인 할 부분!! manage.py있는지 확인    
    - 잘 생성 되었으면 생성한 프로젝트 폴더로 이동      

``` py 
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
#========================================================================
# 기본 구조
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
---

## > Step 02 
- Web 요소 구성하기     
    - Board 앱 생성(여러개 생성 가능)    
    - Member 앱 생성     
    - Django 서버 구동(http://127.0.0.1:8000/)    
        - Page 열리는지 확인 => 확인 후       

```py    
# Board 앱 생성(여러개 생성 가능)
    $ django-admin startapp board
# 의문사항 => 직접해보자 
    $ django-admin.py startapp member
    $ django-adminb startproject member
# Member 앱 생성
    $ django-admin startapp member 
# Django 서버 구동(http://127.0.0.1:8000/)
    $ python manage.py runserver 

# DB 연동=> SET IT UP**
    $ python manage.py migrate
```
---
## > Step 03 
- **Sep1**           
    1. Memebr 기능추가
        - Memebr : 회원 관리      
            - 로그인       
            - 회원가입     
            - 회원정보수정     
            - 로그아웃

    - INDEX 페이지 생성
        - URL주소와 장고의 기능을 연결하기 위해  web_re\urls.py에서 urls를 지정
        - ```web_re\urls.py```의 path()함수 안에 ```urls주소/```를 불러 올 url 정보 혹은 동작을 어디에서부터 가지고 올건지를 정의  => urls주소\urls.py    
            - ```include('urls주소\.urls') # 경로를 포함한다.  ```
            => member 폴더안에 member\urls.py를 생성하고 경로를 직접적으로 지정         
            **중요 => import include를 까먹지 말것 !!**       
        - 동작 확인을 하기 전     
            - 예를들면 member app안에 urls를 작성!       
                - view로 이동 => 동작을 만든다(메소드 생성)  
                - HTML 파일을 만든다.        
                    - 만약 템플릿 폴더가 없다면 먼저 생성하고 파일을 만든다.       
                    
        ### 의문 1. 
        ```py
        # index 
        def index(request):
        #return HttpResponse(" 열었다 ")
        return render(request,'member/index.html') 
        # <= 이건 왜 안됨? 복잡할때 사용한다는데 글쎄 =>DIRS 때문에
        ```
    - LOGIN 페이지 생성 
        - 위 내용반복 임으로 생략하고 진행 

    - Singin 페이지 생성 

#### Django 에서는 기본적으로 CSRF 토큰을 이용해 CSRF공격을 방지
 > CSRF 공격이란?
- CSRF 공격(Cross Site Request Forgery)은 웹 어플리케이션 취약점 중 하나로, 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격

<br>       

---






























---
### SQLite 설치
- 오라클 사용할거라 그냥 실습
- 설치는 아래 링크로 이동 
> 4번째_DB Browser for SQLite - .zip (no installer) for 64-bit Windows  
[주소로 이동](https://sqlitebrowser.org/dl/)


###  출처 
인사이트 - 장고