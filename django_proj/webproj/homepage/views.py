from http.client import REQUESTED_RANGE_NOT_SATISFIABLE, HTTPResponse
import numbers
from django.shortcuts import HttpResponse, render
#django.shortcuts패키지에서 랜더링 수행(만든 http 보여주게함)
# Create your views here.
####model import
from .models import Coffee
from .forms import CoffeeForm
#view 구현을 위해 함수 작성 시작
def index(request): #request가 인자로 주고 이에관해 처리 등을 할수있음
  #  return HttpResponse("<h1>Hello World!</h1>")
#어느 경로로 이 request가 들어오면 시행할지 정해야하는데 webproject안의 urls.py에서 설정
    name = "Michael"
    nums=[1,2,3,4,5] #for 문에 넣어줄 값
    return render(request,'index.html',{"my_name":name, "my_list":nums})#긴html파일을 다룰 render함수 사용, 
    #render(함수에 넣은 인자, 응답을 하는 과정에서 보여줄 파일 지정, request와 html을 처리하는 과정에서 사용할 인자)
def coffee_view(request):
  coffee_all=Coffee.objects.all() #select * from coffee[sql같은의미]
  #만약 Request가 post라면
  #post를 바탕으로 form 을 생성하고
  #form 이 유효하면 -> 저장
  if request.method=="POST":
    form=CoffeeForm(request.POST)#html을 바탕으로post로 보내준걸 form으로 하겠다
    if form.is_valid():
      form.save()
  form =CoffeeForm() #view에 import후 form 객체생성
  return render(request,'coffee.html',{"coffee_list":coffee_all,"coffee_form":form})#{}안에 model에서 가져온 값들을 넣어줄거임
