# board/views.py 
# => 사용자 요청을 처리하는 동작을 하는 메소드를 생성 

#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
# Create your views here.

# 모델 설계전 구상 
# 1. 게시판 글 목록 나열
# 2. 제목과 작성자 표시 
# 3. 게시글 들어가면=> 상세화면으로 이동 => 제목 내용 작성일 출력
# 4. 상세화면에서 글 수정하기 클릭 => 글수정페이지로 이동 
# 5. 수정화면에서 저장하기 클릭 =>  수정된 내용이 저장 => 게시판으로 이동 
# 6. 수정화면에서 게시글 삭제 클릭 => 게시글이삭제 게시판으로 이동 
# 7. 새글작성 클릭 => 새로운 글쓰기화면출력 
# 8. 글 작성후 저장클릭 => 수정내용 저장후 게시판이동 '

# 화면 구성 
# 목록, 상세, 수정, 추가
# (수정, 추가 => 추가화면에는 각 입력값이 빈 상태 // 수정화면은 추가화면에 데이터베이스에 저장된 값으로 초기화) 



# 액션 핸들러 정의 

def do_create_article(request):
    return HttpResponse(request.POST)

def do_update_article(request):
    return HttpResponse(request.POST)


# 더미 핸들러 정의 
# create_or_update_article # 생성 및 수정하기, 수정할때는 article의 id 필요 
def create_or_update_article(request, article_id):
    if article_id:
        return HttpResponse('update {}'.format(article_id))
    else: 
        return HttpResponse('create')

# detail_article - 상세보기 
def detail_article(request, article_id):
    return HttpResponse('detail {}'.format(article_id))


# list_article - 목록보기
def list_article(request):
    return HttpResponse('list')


# 핸들러 선언 => 첫인자는 항상 request
def hello(request, to):
# (request, 이후에 url패턴을 통해 전달받을 파라미터들을 선언)
# 키워드인자라 네이밍은 => urls에서 사용된 변수네임과 일치

    return HttpResponse('Hello {}!'.format(to))
# format을 이용해서 출력 => http://127.0.0.1:8000/board/hello/hi => 'Hello hi!' 출력

