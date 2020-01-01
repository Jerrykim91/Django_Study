# member\urls.py
# import 
# 경로 설정 -> 장고의 urls -> path
from django.urls import path
# 현재 패키지 => view 모듈(views.py)에서 호출 
# => 행위(메소드)가 정의 되어있다. 
from . import views 

# 경로 생성 => 함수형 뷰를 호출 
# member/views.py로 부터 => html을 생성 할때 마다 경로 생성 
# path('urls이름', views.urls이름, name = 'urls이름')
urlpatterns = [
    path('main_page', views.main_page, name = 'main_page'),
]




# html을 생성 안해도 보여지는구나~











# Member
# http://127.0.0.1:8000/member/index => 인덱스(index) 함수 동작 => views.py 에서 
# http://127.0.0.1:8000/member/join
# http://127.0.0.1:8000/member/login