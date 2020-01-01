# member/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# main_page
# request는 어디에서부터 오는지 알아야 겠어 
def main_page(request):
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