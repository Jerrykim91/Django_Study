# member/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 
from django.shortcuts import render
# URL의 변화여부가 필요하다면 Redirect
from django.shortcuts import redirect
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체
# 페이지를 웹 서버로 전달하기 위해서 이 클래스를 사용
from django.http import HttpResponse
# csrf 공격방지 패키지
from django.views.decorators.csrf import csrf_exempt
# 디비연결을 위한 팩 
from django.db import connection

#==========================================================

# 렌더(render) 
# index에서 인자값으로 request을 받았어 
# 받았으니까 돌려줘야해 그때 render로 뭔가를 돌려주는데 
# #그게 html 페이지(위치값이랑 확장자명 빼먹지 말기 ) !!! 

# request 
# request = 사용자가 입력한 값과 기타 정보를 담고 있음 (GET, POST, request,등등..)

#==========================================================

# PARAMETER VAL 
cursor = connection.cursor()


# Create your views here.
# 함수형태로 생성, 기호에 따라 클래스로도 생성 가능  


# signin(3-로그인)
@csrf_exempt
def sign_in(request):
    if request.method == 'GET':
        return render( request, 'member/sign_in.html' ) 

    elif request.method == 'POST':
        # 사용자로부터 어떤 데이터를 받냐 => 로그인 할 때 주로 뭘 입력하는데 ? 
        # => 배열 형태로 받는데 이거를 request.POST 형태로 받아야하나? 
        get_info = [request.POST['id'] , request.POST['pw']]

        # 정보를 받았으니까 정보를 db에 업로드 시켜야지 sql문으로 
        sql = """ 
         SELECT ID, NAME FROM MEMBER 
         WHERE ID=%s AND PW=%s
        """
        cursor.execute(sql, get_info)
        # data는 매 호출마다 한 row씩 데이터를 리턴해줌 
        data = cursor.fetchone()
        # 확인
        print('='*45)
        print('확인작업 ==> ', data ,'\n타입체크 ==> ', type(data))
        print('='*45)

        # if data: # 세션설정 
        #     request.session['userid'] = data[0]
        #     request.session['username'] = data[1]
        #     print('userid: ',request.session['userid'])
        #     print('username:', request.session['username'])
        #     return redirect('/member/index')


        # 세션은 아직 ! 
        return redirect('/member/main_page')
        # sign_in.html을 작성하러 갑시다. =>  

# main_page
# def main_page(request):
#     #output은 html코드로 HttpResponse에 담겨 전달 
#     output = '''
# <html>
# <head><title>%s</title></head>
# <body>
# <h1>%s</h1><p>%s</p>
# </body>
# </html>
# ''' % (
# '제리 | 공부방',
# '제리의 공부방에 오신 것을 환영합니다.',
# '여기에 내용를 저장하고 공유할 수 있습니다!'
# )
#     return HttpResponse(output)















    


# Signup(2-회원가입)
@csrf_exempt
def sign_up(request):
    # GET을 요청했다면 요청받은 렌더링 값을 리턴 => 페이지 이동 클릭 개념으로 생각하면 수월  
    if request.method == 'GET':
        return render( request, 'member/sign_up.html' ) 
    # 만약에 POST를 요청하면 새로운 경로를 송신 => '/member/index' 
    # ( 근데 왜 ? )
    elif request.method == 'POST':
        # 뭐를 구현해야할까 -> 회원가입이니까 
        # 정보 => ID, PW, PRESONAL-INFO(2-3)
        # ID, PW , NAME, AGE => 추가 
        ID   = request.POST['id'] # html에서 넘어오는 값이라고는하는데 음 
        PW   = request.POST['pw']
        AGE  = request.POST['age']
        NAME = request.POST['name']

        # 디비는 순서가 중요하니까 리스트로 담아야지 
        # 튜플로 담아도 되긴한데 수정이 힘드니까 리스트로 하는것같음 
        get_data = [ID, PW, AGE, NAME]
        # 확인을 위해 출력 수시로 출력하는 습관을 들이면 좋을것 같음 
        print(get_data)

        # DB에 추가 =>MEMBER라는 테이블을 생성하고 그테이블에 담을거임
        # MEMBER(id, pw, age, name, joindate) DB의 테이블 인덱스 네임과 같아야한다.
        # SQL문 작성 
        sql = """
        INSERT INTO MEMBER( ID, PW, AGE, NAME, JOINDATE ) 
        VALUES(%s,%s,%s,%s, SYSDATE)
        """
        # 실행 => 커서 선언 !! 
        # cursor.execute(sql,[, parametwers]]) => 여기서 리스트 형태의 매개변수 값을 받음  
        # cursor = connection.cursor() => 위에 선언 해둠 
        # DB 실행
        cursor.execute(sql, get_data)

        return redirect( '/member/main_page' )
        # sign_up.html을 작성하러 갑시다. =>  



# main_page(1-임시 메인페이지)
def main_page(request):
    if request.method == 'GET':
        return render( request, 'member/main_page.html' ) 
