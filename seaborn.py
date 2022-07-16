#!/usr/bin/env python
# coding: utf-8

# ## 시각화 라이브러리 Seaborn

# In[7]:


get_ipython().run_line_magic('pip', 'install seaborn')


# In[9]:


import seaborn as sns


# ## 꺾은선 그래프

# In[10]:


sns.lineplot(x=[1,3,4],y=[0.7,0.2,0.1])


# ## 막대그래프

# In[12]:


sns.barplot(x=["a","b","c","d"],y=[0.7,0.2,0.1,0.5])


# In[13]:


import matplotlib.pyplot as plt


# In[15]:


sns.barplot(x=[1,2,3,4],y=[0.7,0.2,0.1,0.05])
plt.title("bar plot")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()


# In[18]:


#line plot에서 y 축 범위를 2-4 lim
sns.lineplot(x=[1,3,2,4],y=[4,3,2,1])
plt.ylim(2,4)
plt.show


# In[19]:


#크기를 20*10으로 바꿔라
plt.figure(figsize=(20,10))
sns.lineplot(x=[1,3,2,4],y=[4,3,2,1])
plt.ylim(2,4)
plt.show


# ## 스크래핑 결과 시각화하기

# In[3]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# In[12]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.weather.go.kr/w/weather/forecast/short-term.do")
#delay 넣기
driver.implicitly_wait(1)
temps=driver.find_element(By.ID,"my-tchart").text
#print(temps.replace("℃","").split("\n"))

#문자열은 숫자와 데이터 타입이 다르기 때문에 타입을 다시 바꿔줘야함
temps= [int(i) for i in temps.replace("℃","").split("\n") ]
print(temps)


# In[13]:


#이걸로 꺾은선 그래프를 그려보자

import seaborn as sns

sns.lineplot(
    x=[i for i in range(len(temps))],
    y=temps

)


# In[17]:


#import seaborn as sns
import matplotlib.pyplot  as plt
#ylim을 더 길게 
plt.ylim(min(temps)-2,max(temps)+2)
plt.title("expected temperature")
sns.lineplot(
    x=[i for i in range(len(temps))],
    y=temps

)
plt.show()


# ## 해시코드 질문태그 시각화

# In[24]:


user_agent={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


# In[29]:


import requests
from bs4 import BeautifulSoup

#질문의 빈도를 체크
#frequency={}

for i in range(1,5): #페이지 1~5 까지 추출
    res=requests.get("https://hashcode.co.kr/?page={}".format(i))#useragent도넣어줌
    soup=BeautifulSoup(res.text,"html.parser")

#1. ul 태그를 모두찾기
#2. 1번안에 li 태그의 text를 추출

    ul_tags=soup.find_all("ul","question-tags")
    for ul in ul_tags:
        li_tags=ul.find_all("li")#그냥 find 했을때 해당 내용이 없음 오류발생이라 find all 해야함
        for li in li_tags:
            print(li.text.strip()) #빈칸 삭제


# In[31]:


import requests
from bs4 import BeautifulSoup

import time
#질문의 빈도를 체크
frequency={}

for i in range(1,5): #페이지 1~5 까지 추출
    res=requests.get("https://hashcode.co.kr/?page={}".format(i))#useragent도넣어줌
    soup=BeautifulSoup(res.text,"html.parser")

#1. ul 태그를 모두찾기
#2. 1번안에 li 태그의 text를 추출

    ul_tags=soup.find_all("ul","question-tags")
    for ul in ul_tags:
        li_tags=ul.find_all("li")#그냥 find 했을때 해당 내용이 없음 오류발생이라 find all 해야함
        for li in li_tags:
            tag=li.text.strip()
            if tag not in frequency:
                frequency[tag]=1
            else:
                frequency[tag]+=1
    time.sleep(0.5)
print(frequency)


# In[35]:


#COUNTER 빈도가 가장 높은 value  추출

from collections import Counter
counter=Counter(frequency)
counter.most_common(10) # 상위 10개 뽑기


# In[38]:


# seaborn 을 이용해 barplot

import seaborn as sns
x=[elem[0] for elem in counter.most_common(10)]
y=[elem[1] for elem in counter.most_common(10)]

sns.barplot(x=x,y=y)


# In[42]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20,10)) #20*10 으로 아래 글씨 안겹치게 확대


plt.title("Frequency of question in hashcode")
plt.xlabel("tag")
plt.ylabel("Frequency")
import seaborn as sns
x=[elem[0] for elem in counter.most_common(10)]
y=[elem[1] for elem in counter.most_common(10)]

sns.barplot(x=x,y=y)

plt.show()


# ## wordcloud

# In[43]:


get_ipython().run_line_magic('pip', 'install wordcloud')
get_ipython().run_line_magic('pip', 'install konlpy')


# In[55]:


#시각화에 쓰이는 라이브러리
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#횟수를 기반으로 딕셔너리 생성
from collections import Counter

#문장에서 명사를 추출하는 형태소 분석 라이브러리
from konlpy.tag import Hannanum
 


# In[56]:


national_anthem="""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
남산 위에 저 소나무 철갑을 두른 듯
바람 서리 불변함은 우리 기상일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
가을 하늘 공활한데 높고 구름 없이
밝은 달은 우리 가슴 일편단심일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
이 기상과 이맘으로 충성을 다하여
괴로우나 즐거우나 나라 사랑하세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
"""


# In[59]:


# hananum 객체를 생성한 후 .nouns()로 명사 추출
hannanum= Hannanum()
nouns = hannanum.nouns(national_anthem)
# konlpy는 자바를 사용하는 분석기라 자바를 설치해야함
nouns[:10]


# In[60]:


counter= Counter(nouns)
counter #counter 를 사용하면 dict형태로 만들어준다


# In[82]:


#이제 wordcloud를 만들자

wordcloud=WordCloud(
   font_path='C:\\Users\\jiin\\font\\ulsanjunggu.ttf',
    background_color="white",
    width=1000,
    height=1000,
)#한국어 폰트를 인자로 넣어줘야함
img=wordcloud.generate_from_frequencies(counter)
plt.imshow(img)


# In[ ]:


## 질문 태그가 아닌 질문 제목을 형태분석


# In[83]:


user_agent={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


# In[88]:


import requests
from bs4 import BeautifulSoup

import time
#질문의 빈도를 체크
questions=[]

for i in range(1,6): #페이지 1~6 까지 추출
    res=requests.get("https://hashcode.co.kr/?page={}".format(i),{"User-Agent":user_agent})#useragent도넣어줌
    soup=BeautifulSoup(res.text,"html.parser")

 
    parsed_datas=soup.find_all("li","question-list-item")
    for data in parsed_datas:
        questions.append(data.h4.text.strip())
    time.sleep(0.5)


# In[89]:


questions[:10]


# In[90]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud

from collections import Counter

from konlpy.tag import Hannanum


# In[91]:


words=[]
hannanum = Hannanum() #지난번엔 문장 하나를 넣었지만 questions 안에서 하나씩 뽑
for question in questions:
    nouns= hannanum.nouns(question)#한번 반복할때 나온 명사들
    words+=nouns #누적해서 나오는 명사들
    
print(len(words))


# In[92]:


counter=Counter(words)
counter


# In[93]:


WordCloud(
    font_path='C:\\Users\\jiin\\font\\ulsanjunggu.ttf',
    background_color="white",
    height=1000,
    width=1000,
)
img=wordcloud.generate_from_frequencies(counter)
plt.imshow(img)


# In[ ]:




