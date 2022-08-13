# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NZ5ZzoVzcaHOfN74L6Te7z4iBPaomqW
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

"""what is pytorch?
python 기반의 과학연산패키지, numpy를 대체하면서 gpu를 이용한 연산

tensor는 numpy의 ndarray와 유사하며 gpu를 이용한 연산
"""

from __future__ import print_function
import torch
torch.__version__

x =torch.empty(5,3)
print(x)

x=torch.randn(5,3) #normal 표준 정규분포에서 샘플링, 0을평균
print(x)
x=torch.rand(5,3) #0~1 사이의 값에서 랜덤으로 가져옴
print(x)

x= torch.zeros(5,3,dtype=torch.long)
print(x)

x=torch.ones(5,3, dtype=torch.long)
print(x)

x=torch.tensor([5,5,3]) #tensor 생성
print(x)

x=x.new_ones(5,3, dtype=torch.double)
print(x)
x=torch.randn_like(x, dtype=torch.float) #파라미터 x의 5,3을 따라 생성
print(x)

print(x.size())

#연산
y= torch.rand(5,3)
print(x)
print(y)
print(x+y)

print(torch.add(x,y))

#결과 temsor를 인자로 제공
result= torch.empty(5,3)
print(result)

torch.add(x,y, out=result)# x,y 를 result에 넣어줌
print(result)

#inplace 방식 = 텐서를 새로 생성하지 않고 y.add_(x) 바꿔치기함 
print(y)
y.add_(x) 
print(y)#y에 할당하지 않았는데 x가 더해진 값이 나온다

#inplace 방식으로 연산한 결과는 y.add_(x) 처럼 _가 붙어있음
#Numpy스러운 인덱싱 표기 방법을 활용 할 수 있다
print(x)
print(x[:,1]) #1번째 열을 다 가져오겠다

x= torch.randn(4,4)
print(x)

y=x.view(16)  #(4,4)를 16개의 차원을 가진 벡터로 쭉 피겠다
z=y.view(-1,2) # -1은 남는 원소를 자동으로 결정해서 한 행에 2개씩 넣어줘라 
print(y)
print(z)
print(y.size(), z.size())

x= torch.randn(1)
print(x)
print(type(x), type(x.item()))#x.item으로 가져오면 tensor가 아닌 float으로 가져옴
print(x.item())

"""Numpy변환(bridge)
torch tensor 를 numpy 배열로 변환하거나 그 반대는 쉽다
cpu상의 torch tensor와 numpy 배열은 저장 공간을 공유하기 때문에 하나라도 변경하면 다른 하나도변경된다

"""

# torc tenso를 numpy 배열로 변환하기
a= torch.ones(5)
print(a)

b=a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

#영향을 안받게 하려면 clone으로 저장공간을 따로 만들어줌
temp=a.clone()
temp_numpy=temp.numpy()

a.add_(1)
print(a)
print(temp_numpy)

#numpy배열을 torch tensor로 변환하가
import numpy as np
a=np.ones(5) #numpy
print(a)
b=torch.from_numpy(a) #torch
np.add(a,1,out=a)
print(a)
print(b)#a 에다 더해도 똑같이 b도 영향

"""CUDA tensors = .to 메소드로 temsor를 어떠한 장치로도 옮길 수 있다"""

import torch
#torch.device 를 사용해 tensor를 gpu 안팎으로 이동해본다
#이 코드는 cuda가 사용 가능한 환경에서만 실행한다

x=torch.rand(4,4)
if torch.cuda.is_available():#일단 cuda 사용가능한지
    device= "cuda:0" #gpu 0번째로 이동 시키겠다
    y= torch.ones_like(x, device=device) #x와 같은형태 4,4
    print(y)

    x=x.to(device)
    z=x+y
    print(z)
    print(z.to("cpu", torch.double)) #zf를 다시 cpu형태로 변환

x.cuda() #cuda에서 연산

import tensorflow as tf
print(tf.__version__)

#모양이 [1,2.3]이고 값은 0으로 3차원 텐서가 변수로 생성
my_variable= tf.Variable(tf.zeros([1,2,3]))
my_variable

v=tf.Variable(0,0)
print(v)
w=v+1#v값(변수)기준으로 바뀌는 값

print(v)

#값을 변수에 할당하려면 assign, assign_add 메소드와 tf.Variable 클래스에 있는 친구들(friends)을 사용
a=tf.Variable(0,0)
a.assign_add(1)
a.read_value() #numpy =1나옴

"""tf.Tensor 객체의 랭크는 그 차원의 수"""

#랭크 0
mammal= tf.Variable("코끼리",tf.string)
ignition=tf.Variable(451,tf.int16)
floating = tf.Variable(3.14159265359, tf.float64)
its_complicated = tf.Variable(12.3 -4.85j,tf.complex64)

print(mammal)
print(ignition)
print(floating)
print(its_complicated)
tf.rank(mammal)

#랭크 1 벡터
mystr =tf.Variable(['안녕하세요'], tf.string)
print(mystr)
tf.rank(mystr)

#고차원 랭크(랭크 2~)
mymat=tf.Variable([[7],[11]], tf.int16)
print(mymat)
tf.rank(mymat)

my_image = tf.zeros([10,299,299,3]) #배치*높이*너비*색상

r=tf.rank(my_image)
print(r)

#원소 참조하기
my_vector = tf.Variable([1,2,3,4], tf.int32)
print(tf.rank(my_vector))

my_scalar =my_vector[2] #idx 2 원소 3 가져옴
print(my_scalar)

squares= tf.Variable([[4,9],[16,25]])
my_row=squares[1] #열백터
my_col= squares[:,1] #모든 행의 인덱스와 열의 번호
print(my_row)
print(my_col)

#60개의 원소
rank_three_tensor =tf.ones([3,4,5])
print(rank_three_tensor.shape)
print(rank_three_tensor)
matrix=tf.reshape(rank_three_tensor, [6,10])

print("==================")
print(matrix)
print(matrix.shape)

matrixB=tf.reshape(matrix,[3,-1]) #-1은 자동으로 결정하라는 거고, 60/3=20,3행20열
print("++++++++++++++++")

print(matrixB.shape)
print(matrixB)


matrixAlt=tf.reshape(matrixB,[4,3,-1]) #12, -1 -> 60/4/3 =5, 

print(matrixAlt.shape)

yet_another= tf.reshape(matrixAlt,[13,2,-1]) #에러 ->60/13/2 는 나머지가 나와서 안됨

#정수형 텐서를 실수형으로 변환 cast
a= tf.constant([1,2,3])
print(a)

float_tensor=tf.cast(tf.constant([1,2,3]), dtype=tf.float32)
float_tensor

"""실습 2
Autograd


텐서의 모든 연산에 대한 자동 미분을 제공하는 패키지

실행 - 기반 - 정의 프레임 워크로 코드를 어떻게 작성하여 실행하느냐에 따라 역전파가 정의 된다는 것을 의미

역전파는 학습 과정의 매 단계마다 달라진다

tensor의 경우 .requires_grad 의 속성을 true 로 실행하면

해당 텐서에서 이루어진 모든 연산을 추적하기 시작한다


계산이 완료된 후 .backward() 를 호출해 자동으로 도함수와 grad를 계산하고 tensor 의 변화도는 . grad의 속성에 누적됨

Function과 tensor는 서로 연결되어있고 모든 연산 과정을 부호화해 순환하지 않는 그래프를 만든다

직접 만든 tensor를 제외한 연산 등으로 나온 tensor는 모두 Function을 참조하고, .grad_fn의 속성이 True가 나온다 



"""

import torch
x= torch.ones(2,2, requires_grad =True)
print(x)
print(x.grad_fn)

y = x+2

print(y)

print(y.grad_fn) #연산에 의한 값이니까 grad fn존재

z= y *y*3
out = z.mean()
print(z) #곱셈결과 mul back
print(out) #평균결과 mean back

# requares_grad_() 를 사용해 기존 tensor의 requires_grad의 값을 바꾼다
# 입력값이 지정되지 않으면 기본값은 False

a= torch.randn(2,2)
print(a) #지정 안했으니까 grad값 false

a = ((a*3)/(a-1))
print(a)
print(a.requires_grad) # 위 a의 grad값 상속

# a의 grad true 로 바꾸기

a.requires_grad_(True)

print(a.requires_grad)

b=(a*a).sum()
print(b.requires_grad)

"""변화도 Gradient

* backward() 를 여러번 하려면 retain_graph = True 로 설정해 줘야함
"""

x= torch.ones(2,2, requires_grad =True)
y= x+2
z=y*y*3 
out= z.mean()
y.retain_grad()
z.retain_grad() # 중간값에 대한 미분값

out.backward(retain_graph=True) #값을 따로 지정 안했으니까
#out.backward(torch.tensor(1.)) 과 같이 미분식에 1을 집어넣은 값 4.5가 나온다

print(x.grad)
print(y.grad)
print(z.grad) #윗줄에서 중간값에 대한 미분값을 불러서 저장했으니까 값이 그대로나옴 코드가 없었으면 none
print(z.is_leaf) #자식노드가 없는노드 즉 말단 노드를 leaf노드라고 함

out.backward() #backward / 미분 한번더
print(x.grad)
print(y.grad)

"""벡터와 야코비안의 곱을 계산하는 엔진

torch.autograd

전체 야코비안을 직접 계산 할 수는 없지만, 벡터 -야코비안 곱은 backward에 해당 인자로 제공하여 얻을 수 있다
"""

x= torch.randn(3, requires_grad =True)
y=x*2 

while y.data.norm() < 1000:
    y =y*2 
print(y)

#y의 벡터 야코비안 값을 구함
v= torch.tensor([0.1,1.0,0.001], dtype=torch.float)
y.backward(v)

print(x.grad)

#with torch.no_grad()로 코드블록을 감싸서
# autograd가 .required_grad =True 인 부분의 연산 기록을 추적하는것을 막는다

print(x.requires_grad)
print((x**2).requires_grad)
with torch.no_grad():
    print((x**2).requires_grad)

#또는 .detach()를 호출해 기록추적을 막음

print(x.requires_grad)
y=x.detach()
print(y.requires_grad)
print(x.eq(y).all()) #값이 같은지 확인

#즉 detach를 활용하면 내용물은 같지만 requires_grad 가 다른 새로운 텐서를 가질 수 있음

"""ANN(Artificial Neural Networks)

* 신경망은 torch.nn 패키지를 사용해 생성할 수 있음
* nn 모델을 정의하고 미분하기 위해 위에서 살펴본 autograd를 사용
* nn.Module은 계층(layer)과 output을 반환하는 forward(input) 메소드를 포함한다


* 간단한 순전파 네트워크(feed-forward-network)
* 입력을 받아 여러 계층에 차례로 전달한 후, 최종 출력을 제공
* 신경망의 일반적인 학습 과정




* 학습 가능한 매개변수(가중치)를 갖는 신경망을 정의 
* 데이터 셋 입력을 반복
* 입력을 신경망에서 전파(process)
* 손실(loss : 입력값과 예측값 차이) 계산
* 변화도를 신경망의 매개변수들에 역으로 전파 - 역전파 과정
* 신경망의 가중치를 갱신 
* 새로운 가중치=가중치 -학습률*변화도(grad)



"""

import pandas as pd
from sklearn.datasets import load_iris
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

class Net(nn.Module): 
    def __init__(self):
        super(Net, self).__init__()

        self.layer0 = nn.Linear(4, 128) #선형함수 5개 층 통과
        self.layer1 = nn.Linear(128, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 16)
        self.layer4 = nn.Linear(16, 3)

        self.bn0 = nn.BatchNorm1d(128)#배치단위 안의 값들을 정규화
        self.bn1 = nn.BatchNorm1d(64)
        self.bn2 = nn.BatchNorm1d(32)

        self.act = nn.ReLU()    #비선형함수통과

    def forward(self, x):
      x = self.act(self.bn0(self.layer0(x))) #레이어통과, 정규화, 활성화함수 통과
      x = self.act(self.bn1(self.layer1(x)))
      x = self.act(self.bn2(self.layer2(x)))
      x = self.act(self.layer3(x))
      x = self.layer4(x)

      return x

"""손실 함수(Loss Function)

* 손실함수는 (output, target)을 한 쌍으로 입력받아, 출력이 정답으로부터 얼마나 떨어져 있는지 추정하는 값을 계산

* forward 함수만 정의하고 나면 backward 함수는 autograd를 사용해 자동으로 정의된다
*모델의 학습 가능한 매개변수는 net.parameters()에 의해 변환된다
"""

#랜던값 생성

criterion =nn.CrossEntropyLoss() #다중 분류문제에서 사용

ex_X, ex_y = torch.randn([4,4]), torch.tensor([1,0,2,0]) #4개의 샘플과 4개의 특성 그리고 
#정답값이 있음 1번분류인지 0번분류인지 2번분류인지 0번분류인지 


#net을 가져와 모델을 정의 
net = Net()

#입력값이 모델을 통과한 결과값
output = net(ex_X)
print(output)
#손실계산
loss = criterion(output, ex_y)
#계산한 손실 출력
print('loss: ', loss.item())
  
net.zero_grad() #역전파를 위해 grad를 다 0으로 만들어줌, pytorch는 값을 누적시키기떄문

print('layer0.bias.grad before backward')
print(net.layer4.bias.grad)
print(net.layer4.bias.is_leaf) #leaf 노드가 ture가나오는데
#이떄 leaf노드는 retain_grad()를 하지 않아도 grad값이 나온다

loss.backward() #loss로 역전파 진행

print('layer0.bias.grad after backward')
print(net.layer4.bias.grad) #backward 후 그래디언트 생성

#생성된 네트워크의
params= list(net.parameters())
print(len(params))
print(params[0].size()) #0번쨰 layer의 가중치

"""가중치 갱신

* 가장 단순한 갱신 규칙은 확률적 경사 하강법(SGD:stochastic Gradient descent)

* 새로운 가중치= 가중치 -학습률* 변화도


"""

#torch.optim 패키지에 다양한 갱신 규칙이 구현되어있음
import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.001)

optimizer.zero_grad() #optimizer grad를 0으로 초기화
output = net(ex_X)
loss = criterion(output, ex_y) #얼마나 다른지
loss.backward()
optimizer.step()  # 업데이트 진행

"""MLP 모델

* iris 데이터를 가져와서 모델에 넣어서 학습하고 출력되는 과정을 보자

"""

#data load
dataset = load_iris()

data = dataset.data #데이터
label = dataset.target#타겟(정답)

print(dataset.DESCR)

print('shape of data :',data.shape) #150 개마다 4개의 속성
print('shape of label:',label.shape) #150 개마다 한개의 label

# 훈련과 테스트 데이터로 나누기
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.25)
print(len(X_train))
print(len(X_test))

# DataLoader 생성
# numpy->Tensor
X_train = torch.from_numpy(X_train).float()
y_train = torch.from_numpy(y_train).long()
X_test = torch.from_numpy(X_test).float()
y_test = torch.from_numpy(y_test).long()

train_set = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_set, batch_size=4, shuffle=True) #한번에 몇개의 데이터를 신경망에 볼껀지 batch
#랜덤으로 셔플링 하는효과 넣음

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.layer0 = nn.Linear(4, 128)
        self.layer1 = nn.Linear(128, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 16)
        self.layer4 = nn.Linear(16, 3)

        self.bn0 = nn.BatchNorm1d(128)
        self.bn1 = nn.BatchNorm1d(64)
        self.bn2 = nn.BatchNorm1d(32)

        self.act = nn.ReLU()

    def forward(self, x):
      x = self.act(self.bn0(self.layer0(x)))
      x = self.act(self.bn1(self.layer1(x)))
      x = self.act(self.bn2(self.layer2(x)))
      x = self.act(self.layer3(x))
      x = self.layer4(x)

      return x #어떻게 분류가 될껀지 리턴
      # return nn.Softmax(x)

net = Net()
print(net) #어떠한 요소들이 포함되어있는지 확인

#옵티마이저 sgd를 이용해 학습 진행
optimizer = torch.optim.SGD(net.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss() #loss
epochs = 200 #200번 반복

losses = list()
accuracies = list()

for epoch in range(epochs):
  epoch_loss = 0  #epoch 마다 loss와 accuracy
  epoch_accuracy = 0
  for X, y in train_loader:
  
    optimizer.zero_grad()
    
    output = net(X)

    loss = criterion(output, y)
    loss.backward() #오차로 역전파
    #output = [0.11,0.5,0.8] 중 가장 큰 0.8이 결과에대한 label값 -> 이걸로 accuracy 측정
    optimizer.step()#업데이트
    #
    _, predicted = torch.max(output, dim=1)
    accuracy = (predicted == y).sum().item() #예측 label이 답 y와 동일하면 맞는거니까 accuracy측정
    epoch_loss += loss.item()
    epoch_accuracy += accuracy 

  epoch_loss /= len(train_loader)
  epoch_accuracy /= len(X_train)
  print("epoch :{}, \tloss :{}, \taccuracy :{}".format(str(epoch+1).zfill(3),round(epoch_loss,4), round(epoch_accuracy,4)))
  
  losses.append(epoch_loss)
  accuracies.append(epoch_accuracy)

# Plot result, 위의 변화 값들을 그래프로 표현

import matplotlib.pyplot as plt

plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.2)

plt.subplot(1,2,1)
plt.title("$loss$",fontsize = 18)
plt.plot(losses)
plt.grid()
plt.xlabel("$epochs$", fontsize = 16)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)


plt.subplot(1,2,2)
plt.title("$accuracy$", fontsize = 18)
plt.plot(accuracies)
plt.grid()
plt.xlabel("$epochs$", fontsize = 16)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)

plt.show()
#loss 감소 정확도 증가

# 지금까지 훈련데이터로만 학습을 했다면
#이제 위에서 만들어둔 test데이터로 모델 성능 평가

output = net(X_test) #만들어둔 모델에 테스트 데이터를 넣어서 
print(torch.max(output, dim=1))#예측을 3개를 하는데 가장 높은값이 나온거고(val과 그 값의 idx)
_, predicted = torch.max(output, dim=1)
accuracy = round((predicted == y_test).sum().item() / len(y_test),4) #측정

print("test_set accuracy :", round(accuracy,4))

"""이제 텐서플로우에 자동 미분과정을 진행해 보자




자동 미분과 그래디언트 테이프


그레디언트 테이프
* 텐서플로는 자동미분을 위한 tf.GradienTape API를 제공
* tf.GradientTape는 컨텍스트 안에서 실행된 모든 연산을 테이프에 기록
* 후진방식자동미분을 사용해 테이프에 기록된 연산 그래디언트를 계산
"""

import tensorflow as tf
print(tf.__version__)

x = tf.ones((2, 2))
# 1, 1
# 1, 1
with tf.GradientTape() as t: #이렇게 만든 x값의 기록을 보겠다 (watch)
  t.watch(x)
  #reduce_sum() : 특정 축을 기준으로 합을 구해줌, 아무것도 입력 안 하면 모든 요소의 합
  y = tf.reduce_sum(x) #sum 1+1+1+1=4
  print('y: ', y)
  z = tf.multiply(y, y)#제곱
  print('z: ', z)

# 입력 텐서 x에 대한 z의 도함수
#
dz_dx = t.gradient(z, x)
print(dz_dx)

for i in [0, 1]:
  for j in [0, 1]:
    # dz_dx[i][j]가 8이 아니면 AssertionError
    assert dz_dx[i][j].numpy() == 8.0

x=tf.ones((2,2))

with tf.GradientTape() as t:
    t.watch(x)
    y= tf.reduce_sum(x)
    z= tf.multiply(y,y)

# tf.GradientTape() 안에서 계산된 중간값에 대한 그래디언트도 구할 수 있다

# 테이프 사용해 x가 아닌 중간값 y에 대한 도함수 계산
dz_dy = t.gradient(z,y)
assert dz_dy.numpy() ==8.0

#GradientTape.gradient() 메소드가 호출되면 GradientTape에 포함된 리소스가 해제
#동일한 연산에 대해 여러 gradient를 계산하려면 지속성있는(persistent=True) 그래디언트 테이프 생성하면됨
#이렇게 생성한 그래디언트 테이프는 gradient()메소드의 다중 호출 허용
x = tf.constant(3.0)
print(x)
with tf.GradientTape(persistent=True) as t:
  t.watch(x)
  y = x * x
  z = y * y  # z = x ^ 4
dz_dx = t.gradient(z, x)  # 108.0 (4*x^3 at x = 3)
print(dz_dx)
dy_dx = t.gradient(y, x)  # 6.0   (2 * x at x = 3)
print(dy_dx)
del t  # 테이프에 대한 참조를 삭제합니다

"""제어흐름 기록 

연산이 실행되는 순서대로 테이프에 기록되기 때문에 파이썬 제어흐름이 자연스럽게 처리된다
"""

def f(x, y):
  output = 1.0
  for i in range(y):
    if i > 1 and i < 5:   #i(y)가 2,3,4일 때 output*=x output은 x^n승
      output = tf.multiply(output, x)
  return output

def grad(x, y):
  with tf.GradientTape() as t:
    t.watch(x)
    out = f(x, y)
  return t.gradient(out, x)

x = tf.convert_to_tensor(2.0)
print(x)

print(grad(x, 6).numpy())	#output=2^3->gradient=3*2^2
assert grad(x, 6).numpy() == 12.0

print(grad(x, 5).numpy())	#output=2^3->gradient=3*2^2
assert grad(x, 5).numpy() == 12.0

print(grad(x, 4).numpy()) 	#output=2^2->gradient=2*2^1
assert grad(x, 4).numpy() == 4.0
# assertion error가 발생하지 않아서 해당 값들이 차례로 출력 됨

"""고계도(higher order) 그래디언트

컨텍스트 안에 있는 연산들은 자동 미분을 위해 기록되고
만약 이 컨택스트 안에서 그래디언트를 계산하면 해당 그래디언트 연산 또한 기록된다

   +케라스 경우 fit 함수를 써서 fit 안에서 인자만 넣어주면 자동으로 시행됨
연산 과정을 추적하고 싶다면 gradienttape를 사용한다



"""

x = tf.Variable(1.0) 
print(x)

with tf.GradientTape() as t:
  with tf.GradientTape() as t2:
    y = x * x * x
  dy_dx = t2.gradient(y, x)      # dy_dx = 3 * x^2 at x = 1
d2y_dx2 = t.gradient(dy_dx, x)   # d2y_dx2 = 6 * x at x = 1

assert dy_dx.numpy() == 3.0
assert d2y_dx2.numpy() == 6.0
print(dy_dx)
print(d2y_dx2)

"""ANN (artificial neural network)

sequential 모델을 사용하는 경우

sequential 모델은 각 레이어에 정확히 하나의 입력 tensor와 하나의 출력 텐서가 있는 일반 레이어 스택에 적합하다
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define Sequential model with 3 layers
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),  # Pytorch - nn.Linear 
        layers.Dense(3, activation="relu", name="layer2"), # 그 안에 3개의 노드와 relu 로 활성함수
        layers.Dense(4, name="layer3"),
    ]
)
# Call model on a test input
x = tf.ones((3, 3))
# [1, 1, 1] --> [o, o] --> [o, o, o] --> [o, o, o, o] #마지막으로 4개의 노드를 통과하니까 그리고 총 3개의 층
y = model(x)

#layer들이 sequential 모델안에 없으면
# y=layer3(layer2(layer1(x))) 로 적어줘서 순차적으로 진행하도록 만들어줘야함
print(y)

model.layers

# add 로 모델을 층들을 추가해주면서 점진적으로 모델을 작석 할 수 있다
model= keras.Sequential()
model.add(layers.Dense(2, activation="relu"))
model.add(layers.Dense(3, activation="relu"))
model.add(layers.Dense(4))

#pop을 사용해 제일 마지막 레이어 제거 가능
model.layers

model.pop()
print(len(model.layers))

"""패션 MNIST 를 사용한 분류문제

* 패션 MNIST 데이터에는 10개의 카테고리와 70,000개의 흑백 이미지가 포함
* 이미지의 해상도는 28*28
* 네트워크 훈련에 60,000개의 이미지를 사용하고 평가를 위해 10,000개를 사용
"""

# tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras

# 헬퍼(helper) 라이브러리를 임포트합니다
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images.shape

len(train_labels)

train_labels #각 라벨은 0-9 사이의정수

"""데이터 전처리"""

#훈련 데이터의 첫번째 이미지

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()  # 0-255 사이의 값을 갖는 이미지 plot

#신경망 모델에 주입하기 전 값의 범위를 0-1로 조정 -> 정규화

train_images =train_images / 255.0

test_images = test_images /255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

"""모델 구성

행렬 형태를 벡터형태로 펴주고 선형모델 사용

"""

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),#flatten으로 벡터로 1*784
    keras.layers.Dense(128, activation='relu'),#노드가 128개인 층을 통과
    keras.layers.Dense(10, activation='softmax') #확률 softmax. 카테고리가 10개 노드 통과해 10개로 출력
])
model.summary()

keras.utils.plot_model(model, show_shapes =True)

model.compile(optimizer='adam', # SGD, SGD + momentum
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']) #정확도를 기준으로 보고 좋아지는 방향으로 학습 설정, loss 주는 방향으로 하고 싶음 loss대신 쓰면 됨
model.fit(train_images, train_labels, epochs=5)#입력값과 정확값, 반복 적어줌 , loss가 줄고 정확도가 느니까 학습이 잘 되고있음 확인 가능

#검증 

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print("Test loss:", test_loss)
print("Test accuracy:", test_acc)

# 훈련된 모델들을 사용해 이미지에 대한 예측 만들기

predictions =model.predict(test_images)
#테스트 세트에 있는 각 이미지에 대한 예측을 진행 한 후 첫번째 에측 값
#10개의 옷 품목에 상응하는 모델의 신뢰도를 나타냄

predictions[0]

#가장 높은 신뢰도를 가진 레이블 출력
# 위의 값에서 9번째가 가장 컸음

np.argmax(predictions[0])

# 실제 테스트 데이터의 0번째 값

test_labels[0]  #두 값이 일치하니까 분류 잘 했음

# 10개의 클래스에 대한 예측을 모두 그래프로 표현
# 올바르게 예측된 레이블은 파란색으로, 잘못 예측된 레이블은 빨강색으로 표현
# 숫자는 예측 레이블의 신뢰도 퍼센트
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red' #잘못예측 빨강

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

#0번째 원소의 이미지
i=0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i,predictions, test_labels)
plt.show()

#0번째 원소의 이미지
i=12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i,predictions, test_labels)
plt.show()

# 처음 X 개의 테스트 이미지와 예측 레이블, 진짜 레이블을 출력합니다
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

