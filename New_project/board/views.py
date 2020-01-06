# 뭐를 불러와서 사용할 지를 생각해 보자 
from django.shortcuts import render, redirect
# 페이지를 웹 서버로 전달하기 위해서 이 클래스를 사용
from django.http import HttpResponse
# csrf 공격방지
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

# Create your views here.


# posting(1- 글쓰기)
def posting():
    pass 
# - 자 어떤 기능을 넣어야 할까 
# - 글을 써야지 
# - 글을 등록해야지 
# - 글을 디비로 보내야지 -> 모델이 있어야 겠네 
# - 모델 먼저 생성 하고 
#     - 테이블 어떻게 구성할것인가 
