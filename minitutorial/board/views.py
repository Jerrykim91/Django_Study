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

# ===========================================================================
# Class Based View로 변경
# 추가 될 내용만 나열 
from django.views.generic import TemplateView
from .models import Article
# 모든 뷰에 클래스변수로 template_name 속성을 추가 =>  모두 'base.html'로 정의
# 'base.html' => 템플릿 파일이름 

# template_name을 정의하면
# 앱 의 templates에서 자동으로 참조해 파일명이 template_name인 파일을 템플릿으로 사용

# 게시글 목록
# 모든 핸들러에 공통적으로 self.render_to_response로 반환
# 모든 뷰에 공통적으로 get 핸들러가 정의되어 있음
# post 핸들러는 액션이 필요한 ArticleCreateUpdateView에서만 정의

class ArticleListView(TemplateView):  
    # template_name 속성 추가    
    template_name = 'base.html'
    # 모든 게시글
    queryset = Article.objects.all()

    def get(self, request, *args, **kwargs):
        # 템플릿에 전달할 데이터
        ctx = {
            'view': self.__class__.__name__, # 클래스의 이름
            'data': self.queryset            # 검색 결과
        }                             
        return self.render_to_response(ctx)

# 게시글 상세
class ArticleDetailView(TemplateView):       
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)

# 게시글 추가, 수정
class ArticleCreateUpdateView(TemplateView):  
    template_name = 'base.html'
    # 화면 요청
    def get(self, request, *args, **kwargs):  
        ctx = {}
        return self.render_to_response(ctx)
    # 액션
    def post(self, request, *args, **kwargs): 
        ctx = {}
        return self.render_to_response(ctx)


def hello(request, to):
    return HttpResponse('Hello {}.'.format(to))
# 핸들러가 함수에서 클래스로 변경 -> url 연결도 변경


# ===========================================================================

# # 액션 핸들러 정의 
# def do_create_article(request):
#     # create 액션
#     return HttpResponse(request.POST)

# def do_update_article(request):
#     # update 액션
#     return HttpResponse(request.POST)


# # 더미 핸들러 정의 
# # create_or_update_article # 생성 및 수정하기, 수정할때는 article의 id 필요 
# def create_or_update_article(request, article_id):
# # 한 함수안에 두개의 메소드를 if를 가지고 정의 =>article_id의 여부에 따라
#     # 수정하기  => article_id 유
#     if article_id: 
#         if request.method == 'GET':
#             return HttpResponse('update {}'.format(article_id))
#         elif request.method == 'POST':
#             return do_create_article(request)
#         else: 
#             return HttpResponseNotAllowed(['GET','POST'])
#     # 생성하기 => article_id 무
#     else: 
#         if request.method == 'GET':
#             return HttpResponse('create')
#         elif request.method == 'POST':
#             return do_update_article(request)
#         else: 
#             return HttpResponseNotAllowed(['GET','POST'])
# # HttpResponseNotAllowed 클래스
# # HttpResponse와 다르게 status_code가 405이고 
# # 허용되지 않는 메소드로 요청했다는 의미를 가지고 있음 
# # 고로, POST 방식이므로 GET과 POST만 허용

        
# # detail_article - 상세보기 
# def detail_article(request, article_id):
#     return HttpResponse('detail {}'.format(article_id))


# # list_article - 목록보기
# def list_article(request):
#     return HttpResponse('list')


# # 핸들러 선언 => 첫인자는 항상 request
# def hello(request, to):
# # (request, 이후에 url패턴을 통해 전달받을 파라미터들을 선언)
# # 키워드인자라 네이밍은 => urls에서 사용된 변수네임과 일치

#     return HttpResponse('Hello {}!'.format(to))
# # format을 이용해서 출력 => http://127.0.0.1:8000/board/hello/hi => 'Hello hi!' 출력

