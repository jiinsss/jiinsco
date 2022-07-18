from django.contrib import admin
#장고가 제공하는 기본 관리자 , superuser를 이용해 접근가능
# Register your models here.
#연동 시작
from .models import Coffee
admin.site.register(Coffee) #관리자페이지에서 model관리 가능

