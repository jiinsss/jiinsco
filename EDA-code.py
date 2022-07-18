#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis

# In[3]:


#라이브러리 불러오기

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
#matplot lib를 inline 환경에서 사용하겠다


# In[6]:


#동일 경로에 train.csv가 있다면
#데이터 불러오기

titanic_df=pd.read_csv("./train.csv")
#jupyter noteboook 설치위치와 같은 위치에 저장 
#C:\Users\jiin


# In[8]:


#상위 5개 데이터 확인

titanic_df.head(5)


# In[9]:


# 각 컬럼의 데이터 타입 확인
titanic_df.dtypes
#판다스 기능 사용


# ## 2.데이터 전체적으로 살펴보기

# In[10]:


# 데이터전체 정보를 얻는 함수 describe()

titanic_df.describe() #수치형 데이터에 대한 요약만을 제공


# In[12]:


# servived 평균이 0.5보다 적음(생손자 상대적으로 적다)
# sib sp max 8 대가족 탑승 ,parch max 6 대가족
# fare 에서 평균과 max의 차이가 큼 아웃라이어

#이제 두 수의 관계인 상관계수를 확인

titanic_df.corr()
#상관성과 인과성 correlation is not causation

# 상관성 : a up, b up
# 인과성 : A->B
#상관성은 있어 보여도 인과성으로 결론을 빠르게 지을 수는 없다


# In[14]:


#반비례일 경우 상관계수 음
#pclass와 fare 즉 돈 더 낸 사람들과의 survived 상관계수 관련성 예측

#결측치 확인(빈공간)

#titanic_df.isnull()  #null =true
titanic_df.isnull().sum()
#age, cabin,embarked에서 결측치 발견


# In[15]:


#결측치를 어떻게 메꿔야 하는지 정하는 것도 중요

#여기까지 전체적인 데이터를 살펴봤다


# ## 데이터의 개별 속성 파악하기

# In[26]:


#생존사, 사망자 명수?

titanic_df['Survived'].sum() #1(생존자) count
titanic_df['Survived'].value_counts()  #0(사망자)과 1(생존자)로 이루어진 값들별 갯수 추출


# In[29]:


#0과 1로 값이 구분되어 있으니까
#이거를 barplot 으로 sns.countplot()
import seaborn as sns

sns.countplot(x='Survived',data=titanic_df)
plt.show()


# In[39]:


# pclass와 survicved

titanic_df[['Pclass','Survived']].groupby('Pclass').count()
#pclass 기준으로 묶어줌
#통계함수 count를 apply해서 의미를 만듦
#survived가 0인지 1인지 상관없이 모두 count되었기 때문에 클래스별 전체 인원수가 print됨


# In[40]:


# 생존자 인원을 구하려면
#생존이 1 이니까 sum을 하면 됨
titanic_df[['Pclass','Survived']].groupby('Pclass').sum()


# In[41]:


#생존자와 전체 인원 비율 -> mean

titanic_df[['Pclass','Survived']].groupby('Pclass').mean()


# In[44]:


#히트맴 활용
sns.heatmap(titanic_df[['Pclass','Survived']].groupby('Pclass').mean())
plt.plot()


# In[52]:


# 성별과 survived


titanic_df[['Sex','Survived']]
#성별로 나눠야 하니까 group by 기준 두개로
#생존 유무와 성별 이렇게 두개
titanic_df.groupby(['Survived','Sex']).count()

titanic_df.groupby(['Survived','Sex'])['Survived'].count() #0,1 별 카운트 해줌
#survived만 필요하니까
#survived컬럼에 대한 접근


# In[56]:


#sns.catplot
#0과 1 로 구분을 col=survived, 매개변수count로 두고 구분
sns.catplot(x='Sex',col='Survived', kind='count', data=titanic_df)
plt.show()


# In[57]:


# age와 survived

#age에 결측치가 존재 했었음 -> 그러나 전체적인 경향성만 볼꺼니까 결측치 신경 X

titanic_df.describe()['Age']


# In[70]:


titanic_df[titanic_df.Survived ==1]['Age']


# In[73]:


## seaborn 에서 연속적인 데이터의 경향을 부드럽게 표현하는 커널 plot kdeplot
#figure(도면)-> axis(틀) -> plot
fig, ax= plt.subplots(1,1, figsize=(10,5))
sns.kdeplot(x=titanic_df[titanic_df.Survived ==1]['Age'], ax=ax) #ax축으로 축을 그려주겠다
sns.kdeplot(x=titanic_df[titanic_df.Survived ==0]['Age'], ax=ax)

plt.legend(['Survived','Dead'])
plt.show()


# In[78]:


# 복합적인 요소에 대한 분석 sns.catplot()
#성별과 pclass 그리고 survived의 관계를 보자
sns.catplot(x='Pclass', y='Survived', kind='point', data=titanic_df)
plt.show()


# In[77]:


# hue 또 다른 범주로 나눌 수 있는 변수
# 단일 변수에서 볼 수 없었던 값이 보임
sns.catplot(x='Pclass', y='Survived', hue='Sex', kind='point', data=titanic_df)
plt.show()


# In[86]:


# age + pclass의 survived

titanic_df['Age'][titanic_df.Pclass == 1].plot(kind='kde')
titanic_df['Age'][titanic_df.Pclass == 2].plot(kind='kde')
titanic_df['Age'][titanic_df.Pclass == 3].plot(kind='kde')

plt.legend(['1st class', '2nd class', '3rd class'])
plt.show()
#높은 클래스일수록 높은 나잇대를 보인다는 것을 확인 할 수 있었다


# In[ ]:




