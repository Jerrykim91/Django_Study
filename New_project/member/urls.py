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
    path('join', views.join, name = 'join'),
    path('edit', views.edit, name = 'edit'),
    path('list', views.list, name = 'list'),
    path('sign_up', views.sign_up, name = 'sign_up'),
    path('sign_in', views.sign_in, name = 'sign_in'),
    path('main_page', views.main_page, name = 'main_page'), 
]




# html을 생성 안해도 보여지는구나~

