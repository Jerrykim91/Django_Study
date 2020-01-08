from django.db import models

# Create your models here.


# polls => 2개의 테이블이 필요 => Question, Choice 정의 하기 
# 직관적인 필드 클래스

# Question
class Question(models.Model):
    question_txet = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_txet

# Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
# 장고에서는 테이블을 하나의 클래스로 정의 => 컬럼은 클래스의 변수(속성값)로 매핑
# django.db.models.Model => 상속 받아서 정의 


# 작성시 유의 사항 
# 1. PK(Primary Key) 지정 하지않아도 자동으로 만들어짐
# 2. date published => pub_date컬럼에 대한 레이블 문구 
# 3.  __str__() 메소드는 객체를 문자열로 표현할때 사용하는 함수 => 정의하지 않으면 제대로 표시되지않음  

# 변경사항 반영 =>테이블 추가 할때마다 생성  
# $ python manage.py check
# $ python manage.py makemigrations 어플이름 
# 필수
# $ python manage.py migrate 어플이름 

