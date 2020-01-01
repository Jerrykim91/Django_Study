# board\urls.py
# Board
# http://127.0.0.1:8000/board/

# import 
# 경로 설정 -> 장고의 urls -> path
from django.urls import path
# 현재 패키지 => view 모듈(views.py)에서 호출 
# => 행위(메소드)가 정의 되어있다. 
from . import views 

# 경로 생성 => 함수형 뷰를 호출 
# Board/views.py로 부터 => html을 생성 할때 마다 경로 생성 
# path('urls이름', views.urls이름, name = 'urls이름')
urlpatterns = [
     path('index', views.index, name = 'index')
]
