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