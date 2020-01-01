# member/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 

from django.shortcuts import render
# HttpResponse 클래스를 django.http에서 import합니다. 
# 페이지를 웹 서버로 전달하기 위해서 이 클래스를 사용
from django.http import HttpResponse


# Create your views here.


# main_page
# request는 어디에서부터 오는지 알아야 겠어 
# request =  사용자가 입력한 값과 기타 정보를 담고 있음 (GET, POST, request,등등..)
def main_page(request):
    #output은 html코드로 HttpResponse에 담겨 전달 
    output = '''
<html>
<head><title>%s</title></head>
<body>
<h1>%s</h1><p>%s</p>
</body>
</html>
''' % (
'장고 | 북마크',
'장고 북마크에 오신 것을 환영합니다.',
'여기에 북마크를 저장하고 공유할 수 있습니다!'
)
    return HttpResponse(output)