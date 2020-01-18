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

urlpatterns = [
    # 추가함으로서 'hello/'라는 경로 hello 핸들러가 호출
    path('hello/<to>', views.hello , name ='hello'),       

]

