# board\urls.py

from django.urls import path
from . import views  # 뷰에서 불러옴 

# 경로(path) 생성 => 장고의 urls => 함수형 뷰를 호출 
# 이곳에서 경로는 만들고 함수는 안 만들면 에러남 
# => 반대 케이스도 마찬가지 뷰를 작성 안 하더라도 아래 경로이름을 가진 함수는 선언은 해줘야함**

# <<  name을 짓는 이유  >>
# 템플릿에 포함된 장고를 명확하게 참고 할수있음 
# 단 하나의 파일만 수정해도 프로젝트 내의 모든 url 패턴을 바꿀수있게 도와 줌 

# path 함수는 4개의 인자를 받을 수 있는데 route(url), view(handler)는 필수로 입력

# urlpatterns = [
#     # 추가함으로서 'hello/'라는 경로 hello 핸들러가 호출
#     path('hello/<to>', views.hello , name ='hello'),     

#     # 게시판 기능 경로 추가  
#     path('article/', views.list_article , name ='list_article'),       
#     path('article/<article_id>/', views.detail_article, name ='detail_article'), 
#     # create => name정의 하니까 에러 나중에 재도전
#     path('article/create/', views.create_or_update_article,{'article_id':None}),         # {'article_id':None} 필수
#     # update => name정의 하니까 에러 나중에 재도전
#     path('article/<article_id>/update/', views.create_or_update_article),       

# ]

# create_or_update_article 핸들러에 article_id()함수의 기본값이 없기 때문에
#  반드시 핸들러에 추가 파라미터를 {'article_id':None} 필수 입력 

# http://127.0.0.1:8000/board/article/           # 'list' 출력
# http://127.0.0.1:8000/board/article/create/    # 'detail create' 출력
# http://127.0.0.1:8000/board/article/8/         # 'detail 8'  출력
# http://127.0.0.1:8000/board/article/12/update/ # 'update 12' 출력



urlpatterns = [
    path('hello/<to>', views.hello), 
    # as_view 메소드는 간단하게 설명하면 뷰클래스의 초기화와 핸들러를 반환하는 기능을 제공
    path('article/', views.ArticleListView.as_view()),
    path('article/create/', views.ArticleCreateUpdateView.as_view()),
    path('article/<article_id>/', views.ArticleDetailView.as_view()),
    path('article/<article_id>/update/', views.ArticleCreateUpdateView.as_view()),
]