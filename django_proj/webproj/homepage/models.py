
from django.db import models

# Create your models here. 
class Coffee(models.Model): 
    def __str__(self):
        return self.name
        #object 말고 커피를 이름으로 표현 설정
    #models.model을 상속하는 클래스 작성
    name=models.CharField(default="",max_length=30)#default는 기본값 설정
    price=models.IntegerField(default=0) #null의경우 false가 기본이라 null허용일때만 true
    is_ice=models.BooleanField(default=False) 
    #한 행이 가져야할 타입 설정 가능
    #문자열, 숫자, 논리형, 시간/날짜 등등
