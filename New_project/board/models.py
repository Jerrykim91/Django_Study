from django.db import models

# Create your models here.
# 모델은 무조건 클래스로 생성 

#  필수 !!! 이거 테이블 추가 할때마다 생성 
# $ python manage.py check 
# $ python manage.py makemigrations board
# $ python manage.py migrate board

# ========================================================================   
#  
# class classname(object):
# classname => 테이블 이름 
# object => models.Model => django.db.models.Model 클래스를 상속 받아 정의 
#
# ========================================================================    


# Table03
class Table9(models.Model):
    # vs code 오류 제거용 
    objects = models.Manager()
    
    # 테이블의 컬럼 구성 => ' 변수 = 모델.필드타입(제약조건) '
    # 타입 필드의 첫 글자는 대문자로 
    no     = models.AutoField(primary_key = True) # 글번호
    title  = models.CharField(max_length = 200)   # 글제목
    content= models.TextField()                   # 글내용
    # CharField 와 textField 차이는 => 글자수를 얼마나 할당할 수 있는지 차이 
    writer  = models.CharField(max_length = 50)   # 글쓴이
    hit     = models.IntegerField()               # 방문자 수
    # BinaryField는 원시 이진 데이터를 저장하는 특수필드 => 이미지를 디비에 이진수로 저장
    img     = models.BinaryField(null = True)     # 이미지 
    regdate = models.DateTimeField(auto_now_add=True) # 접속시간 => 현재시간으로 설정 




