# Django_Setup(_PC방)

### 제일 먼저
1. vs 코드 설치 
2. 아나콘다 설치 -> 안하면 python따로 설치 
3. git 설치 
4. 도커 설치
5. jdk설치 
6. sql_오라클 설치 
---
### 파이썬 설치후 패키지 설치 

``` py
# 웹 구동 전  설치 해야 할 팩  
    $ conda install django
    # => 버전 지정 == >  conda install django 

    # conda 라이브러리 설치          
    $ conda install cx_oracle
    # pip로 라이브러리 설치
    $ pip install cx_Oracle

# 위의 명령어 실패 시 구동 
$ python -m pip install cx_Oracle 

# 위에서 설치한 장고가 잘 인스톨되었는지 확인 
# DB 연동=> SET IT UP**
    $ python manage.py migrate
# Django 서버 구동(http://127.0.0.1:8000/)
    $ python manage.py runserver 

```
---
### **[Docker_도커 툴박스 다운로드](https://github.com/docker/toolbox/releases)**

- Python에서 db 연동하기 위해 도커이용
- PC안에 가상 PC => 서로 다른 가상환경을 사용하기위함 



---

## < Step 01 >

### 진행 과정 
- Install         

  1. 전부 체크 (깃 설치 안되어 있으면 체크 = 깔려있으면 pass )     
  2. 위에서 아래로 3개 체크     

- Docker Quickstart Terminal         
    - 터미널 진입 or 시작     
        - 시작시 ``` docker-machine start ```      
        - yes    
        - 고래 아래 그림 뜨면 진행완료      


``` Bash 
# 이거 나오면 install 잘된거

                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/

docker is configured to use the default machine with IP 192.168.99.100
For help getting started, check out the docs at https://docs.docker.com


Start interactive shell

admin@DESKTOP-THUUM3S MINGW64 /c/Program Files/Docker Toolbox

```
- Docker shutdown     
  - 툴박스에서  ``` $docker-machine stop ```
  - 그리고 => shut-down하고 메모리 환경설정을 변경해야해 !!  

- **Memory Check**    
    *주의 : virtual box에서 메모리를 4096으로 변경 후 설치  
    - 적으면 도커를 종료하고 메모리값을 재 산정하고 진행     
        - 1GB(1024MB) => 8GB(8192MB) 변경( 선택사항 - 도커에 설치 할것이 많으면 8GB가 하는게 맞음)

---

## < Step 02 > 
### oracle-12c 설치 

```Bash 
# 오라클 이미지 검색 
$ docker search oracle-12c
# 오라클 이미지 당겨오기 
$ docker pull truevoly/oracle-12c

# 이미지확인 => 5.7GB
$ docker images

---

[데이터 베이스 접속 client 프로그램 설치]    

<< 설치 순서 >>
+ stp_1 
    - jdk-8u211-windows-x64 
        => 다 ok 

+ stp_2
    - DB에 접속하는 프로그램     
    - sqldeveloper-19.2.0.206.2117-no-jre/sqldeveloper/sqldeveloper.exe     
    - 실행 => 하면 자바경로 입력 (C:\Program Files\Java\jdk1.8.0_211) 

+ stp_3
    - oracle_client 압축파일 안에 있음   
        - instantclient_19_3 file > C 드라이브로 이동         
            - 내피시 > 시스템 > 고급시스템 설정 > 환경변수         
            - 시스템 path 편집  > C 드라이브로 이동된 instantclient_19_3를 경로로 잡아줌 (C:\instantclient_19_3)   

```

---    

## 도커 최초 시작시
```Bash 
# 1. 컨테이너 만들기 
$ docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c

# 2. 로그를 찍어보면서 진행상황이 100%가 될때까지 기다려야함
$ docker logs oracle12c
# 주기적으로 log를 확인 

### 만약 아래 에러 발생 시 ###
Copying database files
1% complete
2% complete
4% complete
DBCA Operation failed.
Look at the log file "/u01/app/oracle/cfgtoollogs/dbca/xe/xe.log" for further details.

=> 도커 초기설정시 가상 메모리확장 했는지 확인해보기 

- Memory Check    
    - 적으면 도커를 종료하고 메모리값을 재산정하고 진행     
        - 1GB(1024MB) => 8GB(8192MB) 변경( 선택사항 )    
     * 본인 컴사양에 따라 (4-8GB) : virtual box에서 메모리를 4096(4GB)으로 변경 후 설치    

##############################
```

---

## Oracle 환경 설정
#### - 도커가 열려야 진행가능 

### 1. 슈퍼 관리자를 먼저 생성 => system
```bash
# 1. 슈퍼 관리자를 먼저 생성 => system

# system
# 오라클 사용자 정보 
user : system # 최고 관리자(슈퍼관리자) => 계정을 만들수 있음 
password : oracle
SID : xe

# 오라클 접속  > 새로 만들기 
Name : 192.168.99.100_system # 도커가 가진 주소 
호스트 이름 :192.168.99.100
포트 : 32764
    => 완료 ( 도움말 위에 >>> 상태 : 성공 )
```
### 2. system계정 생성 후 오라클 계정 생성
```sql
-- 2. system계정 생성 후 오라클 계정 생성
create user admin IDENTIFIED by 1234;
grant connect, resource, dba to admin;

-- 위의 코드 작성후 블록 다 잡고 => 명령문 실행 =>> 커밋 

-- 완료하면 아래 문구가 출력 
-- => User ADMIN이(가) 생성되었습니다. 
-- => Grant을(를) 성공했습니다.

====== > 접속 종료하고 사용자 계정 생성 
```

### 3. 사용자 계정 생성
```bash
### 사용자 계정 만들기     
    Name     : 192.168.99.100_admin   
    user     : admin    
    password : 1234    

    호스트 이름 :192.168.99.100
    포트        : 32764
        => 완료 ( 도움말 위에 >>> 상태 : 성공 )    


---
#### 테이블 생성 - 연습용
    이름 : MEMBER
        - id ( 키를 가짐 - 제약조건 )
        - pw
        - name
        - age (유형 : number)
        - joindate (유형 : date)

- 데이터에서 회원을 만듬 => 임의로 3개 
    - 다 작성 후 => 변경사항 => 커밋 클릭 
```
---

### 도커 재시작
```bash
# 구동중인 컨테이너 실행 확인
$ docker ps -a
# 도커 실행 하기
$ docker start oracle12c

# 혹시 팩이 안깔려 있다면 
## 라이브러리 설치 ##

# conda 라이브러리 설치
$ conda install cx_oracle
# pip로 라이브러리 설치
$ pip install cx_Oracle
# 위의 명령어 실패 시 구동 
$ python -m pip install cx_Oracle 

```

### Docker종료 시
```bash
# stop oracle12c
$ docker stop oracle12c
# Docker종료시
$ docker-machine stop
```

### 필요 시 
```Bash 
# 옵션) 데이너 실행 중지
$ docker stop oracle12c 
# 옵션) 컨테이너 삭제
$ docker rm oracle12c 
```

```$ curl http://www.example.com/```


```py
#파이썬 비트 확인
import platform 
print(platform.architecture())
```

---
파이썬 bit에 맞게 instant-client파일 다운로드     
[다운로드 위치 : 클릭](https://www.oracle.com/kr/database/technologies/instant-client/downloads.html)     
압축을 풀어서 c:\instantclient_18_5으로 이동     
[오류발생시 설치 : 클릭 ](https://support.microsoft.com/en-us/help/4032938/update-for-visual-c-2013-redistributable-package)


# Cx_Oracle 설치 확인
```py
# oracle
#!conda install cx_oracle
import cx_Oracle as oci 

#아이디/암호@서버주소:포트번호/SID
# system
conn = oci.connect('system/oracle@192.168.99.100:32769/xe')
# user
# cursor 객체 얻기
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="uft-8")
cursor = conn.cursor()  
# SQL 문장 실행
cursor.execute('SELECT id, title, content, userid, CAST(CREATED_AT AS DATE) FROM BLOG_POST') 
#[(),(),()] 포멧
blog_list = cursor.fetchall() 
print(blog_list)
#print(blog_list[2][4])

conn.close()
```


# Docker에서 mariadb 설치

```Bash
#vagrant plugin install vagrant-disksize

Vagrant.configure("2") do |config|
config.vm.box = "ubuntu/bionic64"
config.vm.network "forwarded_port", guest: 3306, host: 3396 #mariadb
config.vm.hostname = "localhost"
config.ssh.insert_key = false
config.disksize.size = '50GB'

config.vm.provider "virtualbox" do |vb|
vb.name = "mariadb"
vb.gui = false
vb.cpus = 2
vb.memory = "8192"
end
end

> vagrant up

> vagrant ssh

## OS 업데이트 및 필수 패키지 설치 - linux
$ sudo apt update
$ sudo apt upgrade -y
$ sudo timedatectl set-timezone Asia/Seoul

# Docker 설치 이미지 리포지토리 키 가져오기
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 리포지토리 추가하는 부분
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

$ sudo apt install -y docker-ce docker-ce-cli containerd.io

# vagrant를 docker 그룹에 추가
$ sudo usermod -aG docker vagrant

exit

> vagrant reload

> vargant ssh

$ docker version

$ docker search mariadb

$ docker pull mariadb

$ docker run --name mariadb-01 -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 mariadb
```


# MySQL 설치 확인 

```py
#!conda install pymysql
import pymysql 


# MySQL Connection 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', port=3346, db='test', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 

# SQL문 실행
sql = "select * from member"
curs.execute(sql)


# 데이타 Fetch
rows = curs.fetchall()
print(type(rows))

for tmp in rows:
    #print(type(tmp))
    print("{}-{}-{}-{}-{}".format(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]))

# print(rows)     # 전체 rows

# Connection 닫기
conn.close()

```


### 에러 사항 

```bash
# 에러 
(base) C:\Users\Administrator\Desktop\Django_Study-m\New_project> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 217, in ensure_connection
    self.connect()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 195, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\oracle\base.py", line 229, in get_new_connection
    **conn_params,
cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library: "The specified module could not be found". See https://oracle.github.io/odpi/doc/installation.html#windows for help

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\threading.py", line 916, in _bootstrap_inner
    self.run()
  File "C:\ProgramData\Anaconda3\lib\threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 54, in wrapper
    fn(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 117, in inner_run
    self.check(display_num_errors=True)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\core\management\base.py", line 390, in check
    include_deployment_checks=include_deployment_checks,
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\core\management\base.py", line 377, in _run_checks
    return checks.run_checks(**kwargs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\core\checks\registry.py", line 72, in run_checks
    new_errors = check(app_configs=app_configs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\urls\resolvers.py", line 399, in check
    for pattern in self.url_patterns:
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\utils\functional.py", line 80, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\urls\resolvers.py", line 584, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\utils\functional.py", line 80, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\urls\resolvers.py", line 577, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\ProgramData\Anaconda3\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\Administrator\Desktop\Django_Study-m\New_project\New_project\urls.py", line 22, in <module>
    path('member/', include('member.urls')),
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\urls\conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\ProgramData\Anaconda3\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\Administrator\Desktop\Django_Study-m\New_project\member\urls.py", line 7, in <module>
    from . import views
  File "C:\Users\Administrator\Desktop\Django_Study-m\New_project\member\views.py", line 27, in <module>
    cursor = connection.cursor()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 256, in cursor
    return self._cursor()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 233, in _cursor
    self.ensure_connection()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 217, in ensure_connection
    self.connect()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\utils.py", line 89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 217, in ensure_connection
    self.connect()
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 195, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\oracle\base.py", line 229, in get_new_connection
    **conn_params,
django.db.utils.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library: "The specified module could not be found". See https://oracle.github.io/odpi/doc/installation.html#windows for help


```