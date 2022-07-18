from django import forms
#form 과 연동할 model 가져오기
from .models import Coffee
#어떤 form 을 만들지 , modleForm 을 상속한 form 을 생성
class CoffeeForm(forms.ModelForm): #어떤 모델의 정보를 넣을 form이 생성됨
    class Meta:#그 입력될거를 뭘로 설정할것인지
        model= Coffee #어떤 model에 대한것인지
        fields =('name','price','is_ice') #어떤 필드 받을지