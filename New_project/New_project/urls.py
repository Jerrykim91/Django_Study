"""New_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include 다른 URL패턴을 포함할때 필수 사용 
# 유일한 예외는 관리자 URL => admin.site.urls
# urlpatterns 안에서 선언한것은 => URLconf에 연결 

# 요청을 받으면 장고는 제일 먼저 이곳에 와서 URL패턴을 쭉읽고 URLconf타고 해당하는 하위URL 찾아간다. 
# 그래서 어플 생성시 가장 먼저 이곳에서 상위 URL을 설정하고 작업한다. 

urlpatterns = [
    # 
    # path('/', include('index.urls')),
    path('polls/',include('polls.urls')),
    path('board/', include('board.urls')),
    path('member/', include('member.urls')),
    # 관리자 
    path('admin/', admin.site.urls),
]
