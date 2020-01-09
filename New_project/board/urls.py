# member\urls.py
##########################################

from django.urls import path
from . import views 




# 경로(path) 생성 => 장고의 urls => 함수형 뷰를 호출 
# 이곳에서 경로는 만들고 함수는 안 만들면 에러남 
# => 반대 케이스도 마찬가지 뷰를 작성 안 하더라도 아래 경로이름을 가진 함수는 선언은 해줘야한다. **

urlpatterns = [

    # 게시판 생성 
    path('content', views.content, name = 'content'),
    path('posting', views.posting, name = 'posting'),
    path('list', views.list, name = 'list')


]

# <<  name을 짓는 이유  >>
# 템플릿에 포함된 장고를 명확하게 참고 할수있다. 
# 단 하나의 파일만 수정해도 프로젝트 내의 모든 url 패턴을 바꿀수있게 도와 줌 