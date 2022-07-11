#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


plt.plot([2,4,2,4,2])
plt.show


# In[5]:


x=np.arange(20)
y=np.random.randint(0,20,20)#0부터 20까지의 수 중에서 난수를 20번 생성
plt.plot(x,y)
plt.show()


# In[7]:


#y축을 20까지 보이게 하고 싶으면
plt.plot(x,y)
plt.axis([0,20,0,20])
plt.yticks([0,5,10,15,20])
plt.show()


# In[8]:


plt.scatter(x,y)
plt.show()


# In[10]:


#박스 그림 T자처럼 생긴 상한선과 하한선이 변수 y의 single min, max값을 보여줌
#가로선이 총 3가지인데 맨 아래의 가로선은 q1(백분위애서 25%)
#가운데 주황선은 q2 (중앙값, 백분위 50%)
#마지막선은 q3(백분위에서 75%)

plt.boxplot((x,y))
plt.title("box plot of x,y")
plt.show()


# In[11]:


plt.bar(x,y)
plt.xticks(np.arange(0,20,1))
plt.show()


# In[12]:


#histogram 도수 분포를 직사각형의 막대 형태로 나타냄
#막대그래프 x축의 각 변량들을 그룹으로 묶으며 그것이 계급임
#계급으로 나타낸것의 특징은 0,1,2 가아닌 0~2까지의 범주형 데이터로 구성 후 그림을 그림

plt.hist(y,bins=np.arange(0,20,2)) #0부터 20까지 2개씩 범주로 묶음
plt.xticks(np.arange(0,20,2))
plt.show()


# In[13]:


#원형그래프 비율 확인에 용이 .pipe
z=[100,300,200,400]

plt.pie(z,labels=['one','two','three','four']) #데이터 값과 대응되는 라벨 필수
plt.show()


# ## seaborn

# In[14]:


import seaborn as sns


# In[15]:


#커널밀도 그림 
#히스토그램과 같은 연속적인 분포를 곡선화 해서 그린 그림 sns.kdeplot()

#일단 히스토그램을 그리면
x=np.arange(0,22,2) #간격정함
y=np.random.randint(0,20,20) #0-20중 20번 샘플링
plt.hist(y, bins=x)
plt.show()


# In[17]:


sns.kdeplot(y,shade=True) #false면 색칠 없어짐, y값은 도수이고 전체 density를 
plt.show() #1로 봤을때 어느정도의 density 를 갖는지 보여줌


# In[18]:


#카운트그림(count plot) 범주형 colunm의 빈도수를 시각화 group by후의 도수를 하는것과 동일효과
#sns.countplot()
vote_df=pd.DataFrame({"name":['andy','bob','cat'],"vote":[True,True,False]})

vote_df


# In[19]:


vote_count=vote_df.groupby('vote').count()
vote_count


# In[20]:


plt.bar(x=[False,True],height=vote_count['name'])
plt.show()


# In[21]:


#matplot으로 그린 막대그래프를 seaborn을 사용해 표현
sns.countplot(x=vote_df["vote"])
plt.show()


# In[23]:


#캣그림(cat plot)
#숫자형 변수와 하나 이상의 범주형 변수의 관게를 보여주는 함수
#sns.catplot()

#일단 앞서 다운 받아뒀던 covid 자료를 불러와 저장하고 
covid=pd.read_csv("./country_wise_latest.csv")
covid.head(5)


# In[24]:


s=sns.catplot(x='WHO Region', y='Confirmed', data=covid, kind='strip')
#여기서 kind로 그래프 종류를 바꿀 수 있음 stip, violin등등
s.fig.set_size_inches(10,6)#사이즈지정
plt.show()
#region별 확진자 수를 볼 수 있어서 범주형 데이터와 수치형 데이터를 매핑하는데 좋음


# In[25]:


#스트립 그림 
#scatter plot과 유사하게 데이터의 수치를 표현하는 그래프
s=sns.stripplot(x='WHO Region', y='Recovered', data=covid)
plt.show()


# In[26]:


#swarmplot 유사한 점들이 겹치는 경우 이걸 양 옆으로 분산해 
#해당 값들이 얼마나 있는지 한눈에 확인

s=sns.swarmplot(x='WHO Region', y='Recovered', data=covid)
plt.show()
#점들의 값들이 너무 커서 주어진 데이터를 다표시할 수 없다는 워닝 무시 ㄱㄴ


# In[27]:


#히트맵(heatmap)
#데이터의 행렬을 색상으로 표현해주는 그래프 상관계수에서 가장 많이 사용된다


#covid의 상관계수
#상관계수 = 두 변수 x,y 사이의 상관관계의 정도를 나타내는 수치



covid.corr() 


# In[28]:


sns.heatmap(covid.corr())
plt.show()


# In[ ]:




