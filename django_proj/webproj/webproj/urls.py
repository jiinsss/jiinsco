"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from homepage.views import index,coffee_view #view에대한 정보가 없어서 방금 homepage의 view에서 불러온다

urlpatterns = [
    #아래 로직 말고 경로 하나더 추가해주자
    path('',index), #127.0.0.1/ , 위의 import homage로 불러왔으니까 홈페이지 안의 함수 index(path니까 ,도입력) 입력
    path('coffee/', coffee_view),
    path('admin/', admin.site.urls),#127.0.0.1/admin
]
