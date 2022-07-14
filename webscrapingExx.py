#!/usr/bin/env python
# coding: utf-8

# ## 원하는 요소 가져오기 1

# In[1]:


#스크래핑에 필요한 라이브러리를 불러오자

import requests
from bs4 import BeautifulSoup


# In[2]:


res = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
soup=BeautifulSoup(res.text,"html.parser")


# In[6]:


# h3 태그에 해당되는 요소를 하나 찾아보자
book=soup.find("h3")


# In[4]:


#h3 태그에 해당되는 요소 모두
h3_results=soup.find_all("h3")
h3_results[0]


# In[11]:


#book list에서 원하는 제목만 추출
book.a.text
#for문을 사용해서 뽑기
for book in h3_results:
    print(book.a.text)


# In[14]:


#속성을 이용해 뽑기
for book in h3_results:
    print(book.a["title"])


# ## Locator로 원하는 요소 찾기

# In[15]:


#id와 class를 이용해서 html의 특정 태그를 지칭하고 가져오는 방법에 대해 알아보자

#스크래핑에 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup


# In[16]:


res=requests.get("http://example.python-scraping.com/")

soup=BeautifulSoup(res.text,"html.parser")


# In[17]:


#id 없이 div 태그를 찾자

soup.find("div")


# In[18]:


#id 가 results 인 div 태그를 찾아보자

soup.find("div", id="results")


# In[22]:


#class는 유사한 것들을 분류하는 것 
#차트 속의 데이터 등을 찾을 때 사용한다


find_result=soup.find("div","page-header")
find_result


# In[26]:


find_result.h1.text.strip() #strip 공백 지우기


# ## 원하는 요소 가져오기 2 hashcode 질문 가져오기

# In[31]:


# 스팸봇으로 거부되지 않도록 사용자 정보인 user agent
#user_agent={"User-Agent":""} 헤더에 넣을 수 있게 key 와 value 형태의 dict으로 작성
user_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


# In[32]:


import requests
from bs4 import BeautifulSoup
#get으로 요청을보냄 + 추가적인 인자 user_agent를 넣어줌(헤더)
res=requests.get("https://hashcode.co.kr/",user_agent)


# In[33]:


#이제 응답을 바탕으로 BeautifulSoup 객체를 생성해보자

soup= BeautifulSoup(res.text,"html.parser")


# In[35]:


#질문의 제목을 모아서 가져와 보자
#class, id 이용
#<li></li>
#soup.find("li", "question-list-item")
#class 안으로 연쇄 접근
soup.find("li", "question-list-item").find("div","question").find("div","top").h4.text


# In[40]:


#로직을 이용해 여러개 뽑기

questions=soup.find_all("li", "question-list-item")

for question in questions:
    print(question.find("div","question").find("div","top").h4.text)


# ## Bonus 페이지네이션(pagination)

# In[41]:


#페이지 내에서 스크래핑
#pagination 되어있는 질문 리스트의 제목을 모두 가져온다
#과도한 요청을 방지하기 위해 1초마다 요청을 보낸다
import time
for i in range(1,6):
    res=requests.get("https://hashcode.co.kr/?page={}".format(i)) #{}안의 값이 바뀌니까 .format(i)로 동적으로 만들어줌
    soup=BeautifulSoup(res.text,"html.parser")
    
    questions=soup.find_all("li", "question-list-item")

    for question in questions:
        print(question.find("div","question").find("div","top").h4.text)
    time.sleep(0.5) #0.5의 인터벌을 줌


# In[ ]:




