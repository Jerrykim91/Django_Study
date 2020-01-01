# member/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 

from django.shortcuts import render
# HttpResponse 클래스를 django.http에서 import합니다. 
# 페이지를 웹 서버로 전달하기 위해서 이 클래스를 사용
from django.http import HttpResponse

# 템플릿 메서드를 가지고 옴 
from django.template.loader import get_template
from django.template import Context

# Create your views here.


# main_page
# request는 어디에서부터 오는지 알아야 겠어 
# request =  사용자가 입력한 값과 기타 정보를 담고 있음 (GET, POST, request,등등..)
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

def main_page(request):
    template = get_template('main_page.html')
    var = Context({
        'head_title' : '제리|공부방',
        'page_title' : '제리의 공부방에 오신것을 환영합니다.',
        'page_body'  : '정보를 저장하고 공유하세요~',
    })
    print(' 되?')
    output = template.render(var)
    return HttpResponse(output)
    #return render(request, '/member/index.html') 
    