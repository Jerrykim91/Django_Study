# 뭐를 불러와서 사용할 지를 생각해 보자 
from django.shortcuts import render, redirect
# 페이지를 웹 서버로 전달하기 위해서 이 클래스를 사용
from django.http import HttpResponse
# csrf 공격방지
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

# Create your views here.
# INSTALLED_APPS => board 추가 **

# 커서 변수 선언 => sql문 수행위한 cursor객체
cursor = connection.cursor() 

# list(1_글목록 + 3_추가 목록 보여주기)
@csrf_exempt
def list(request):
    if request.method == 'GET':
        # sql 작성 => 글 목록을 보여줘야하나까
        # 보여주고 싶은거만 선택해서 호출 
        sql = """
        SELECT
            NO, TITLE, WRITER,
            HIT,TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI')
        FROM 
            BOARD_TABLE03
        ORDER BY NO DESC
        """
        cursor.execute(sql)
        # 가지고 있는거 전부 받아 data라는 변수에 담는다
        data = cursor.fetchall()
        # 데이터 확인 
        print(type(data))
        print(data) 

        return render(request, 'board/list.html', {'send':data})
    
    
# posting(2- 글쓰기)
@csrf_exempt
def posting(request):
    if request.method == 'GET':
        return render(request, 'board/posting.html')
    # POST에 뭐가 들어가야하나 .... 
    # 일단은 제목, 내용, 글쓴이부터 정의하고 생각하자 
    if request.method == 'POST':
        # title   = request.POST['title']
        # content = request.POST['content']
        # writer  = request.POST['writer']
    # 맴버처럼 배열에 담아 뿌릴거  
        getdata = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer']
            ]
        try:   
            print(getdata)
            # sql문 작성 
            # => 글 작성 할때마다 추가를 위한 SQL 데이터 삽입문 
            # 1회차 (IMG ,HIT 없이, 예외함수 없이)
            # 1회차 (에러 : HIT, 예외함수 없어서 )
            sql ="""
                INSERT INTO BOARD_TABLE03
                (TITLE, CONTENT, WRITER ,HIT, REGDATE )
                VALUES(%s, %s, %s, %s,0, SYSDATE)
            """
            # 커서 변수 선언 잊지 말기 
            # cursor.execute(sql과 배열형태의 데이터 )
            cursor.execute(sql, getdata)

        except Exception as e:
            print(e)

        return redirect("/board/list")

# - 자 어떤 기능을 넣어야 할까 
# - 글을 써야지 
# - 글을 등록해야지 
# - 글을 디비로 보내야지 -> 모델이 있어야 겠네
# - 글리스트를 봐야지  

