# 뭐를 불러와서 사용할 지를 생각해 보자 
from django.shortcuts import render, redirect
# 페이지를 웹 서버로 전달하기 위해서 이 클래스를 사용
from django.http import HttpResponse
# csrf 공격방지
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import Table9

# Create your views here.
# INSTALLED_APPS => board 추가 **

# 커서 변수 선언 => sql문 수행위한 cursor객체
cursor = connection.cursor() 

#content(4_본문) 
def content(request):
    if request.method == 'GET':
        # 몇번을 눌러서 페이지가 이동한건지 알려준다 => (/board/content?no=글번호)
        no  = request.GET['no'] # 0은 디폴트값
        # no = request.GET.get('no', 0 )
        print(no)

        # s뭐를 보여줘야하나 => 글 내용, 글제목, 작성자 , ** 글번호
        # 데이터베이스에서 가지고 오자 
        # => 기본적인 내용들 선택(글내용, 글제목, 작성자, ** 글번호, 작성시간, 조회수)
        # => 글번호에 매치되는 데이터들을 
        sql = """
            SELECT
                NO, TITLE, CONTENT ,WRITER,
                HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI')
            FROM 
                BOARD_TABLE9
            WHERE
                NO = %s
        """
        # list.html => 글 번호로 가는 경로를 설정  
        # sql하나만 넣고 돌려보자 
        cursor.execute( sql, [no] )    
        # db에서 정보를 불러온다 => 한번에 하나씩 
        # check 
        data = cursor.fetchone()
        # 확인을 위해 출력 => 제대로 데이터가 도달하는지 
        print(data)

        # data = [NO, TITLE, CONTENT ,WRITER, HIT, TO_CHAR] 
        # "one" => 어디서부터 온거지 

        # 본문은 content는 보여주기만 하는 거라서 포스트가 필요없다 
        # GET으로 받아서 쏨  => 에러의 이유 => 주 내용을 포스트안에 담아서 작업했음 => 멍청이

        return render( request, 'board/content.html', {"one":data} )




# list(1_글목록 + 3_추가 목록 보여주기)
@csrf_exempt
def list(request):
    if request.method == 'GET':
        # 세션은 *특정행동*을 하기위해 키를 유저가 임시적(소멸전까지)으로 가지고 *그거*를 유지하는것 
        # request.session['hit'] = 1 # 세션에 hit = 1 
        # sql 작성 => 글 목록을 보여줘야하나까
        # 보여주고 싶은거만 선택해서 호출 
        sql = """
            SELECT
                NO, TITLE, WRITER,
                HIT,TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI')
            FROM 
                BOARD_TABLE9
            ORDER BY NO DESC
        """
        cursor.execute(sql)
        # 가지고 있는거 전부 받아 data라는 변수에 담는다
        data = cursor.fetchall()
        # 데이터 확인 
        print(type(data))
        print(data) 

        return render(request, 'board/list.html', {"send":data})
    
    
# posting(2_글쓰기)
@csrf_exempt
def posting(request):
    if request.method == 'GET':
        return render(request, 'board/posting.html')
    # POST에 뭐가 들어가야하나 .... 
    # 일단은 제목, 내용, 글쓴이부터 정의하고 생각하자 
    elif request.method == 'POST':
        # title   = request.POST['title']
        # content = request.POST['content']
        # writer  = request.POST['writer']
    # 맴버처럼 배열에 담아 뿌릴거  
        getdata = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer']
            ]
        print(getdata)
        # sql문 작성 
        # => 글 작성 할때마다 추가를 위한 SQL 데이터 삽입문 
        # 1회차 (IMG ,HIT 없이, 예외함수 없이)
        # 1회차 (에러 : HIT, 예외함수 없어서 )
        sql ="""
            INSERT INTO BOARD_TABLE9
            (TITLE, CONTENT, WRITER ,HIT, REGDATE )
            VALUES(%s, %s, %s, 0, SYSDATE)
        """
        # 커서 변수 선언 잊지 말기 
        # cursor.execute(sql과 배열형태의 데이터 )
        cursor.execute(sql, getdata)
        
        return redirect("/board/list")

# - 자 어떤 기능을 넣어야 할까 
# - 글을 써야지 
# - 글을 등록해야지 
# - 글을 디비로 보내야지 -> 모델이 있어야 겠네
# - 글리스트를 봐야지  

        # try:   
        #     print(getdata)
        #     # sql문 작성 
        #     # => 글 작성 할때마다 추가를 위한 SQL 데이터 삽입문 
        #     # 1회차 (IMG ,HIT 없이, 예외함수 없이)
        #     # 2회차 (에러 : HIT, 예외함수 없어서 )
        #     sql ="""
        #         INSERT INTO BOARD_TABLE03
        #         (TITLE, CONTENT, WRITER ,HIT, REGDATE )
        #         VALUES(%s, %s, %s, %s,0, SYSDATE)
        #     """
        #     # 커서 변수 선언 잊지 말기 
        #     # cursor.execute(sql과 배열형태의 데이터 )
        #     cursor.execute(sql, getdata)

        # except Exception as e:
        #     print(e)