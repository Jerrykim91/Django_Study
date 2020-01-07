# member\urls.py
# import 
# 경로 설정 -> 장고의 urls -> path
from django.urls import path
from . import views 

# 경로 생성 => 함수형 뷰를 호출 

urlpatterns = [

# 게시판 생성 
path('content', views.content, name = 'content'),
path('posting', views.posting, name = 'posting'),
path('list', views.list, name = 'list')


]
