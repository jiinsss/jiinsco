#!/usr/bin/env python
# coding: utf-8

# In[2]:


#파이썬으로 http 통신을 진행할 수 있는 라이브러리 request를 설치해준다
get_ipython().run_line_magic('pip', 'install requests')


# In[3]:


# requests 라이브러리를 불러온 후 , naver의 홈페이지를 요청한 후 응답받아보기
import requests
#객체로 온 응답을 받을 변수 선언(res)
res=requests.get("http://www.naver.com")
res


# In[4]:


#header를 확인
res.headers


# In[6]:


#body를 텍스트 형태로 확인 //많이 있으니까 1000번째 까지만 슬라이싱
res.text[:1000]


# ## Post

# In[16]:


#payload와 함께 post를 보내보자 #get은 그냥 가져오는거라 body에 별 내용 안적었지만
#post는 정보를 갱신해야 하는데 어떻게 갱신해야 할 지 알려줘야해서
#body에 그 내용(payload)을 적어준다
#보내려면 json타입이어야 하는데 dic 형태가 이와 유사
payload={"name":"hello", "age":13}

res=requests.post("https://webhook.site/60780ed8-3835-44ed-acc0-a7fe2b9d2346", payload)


# In[17]:


res.status_code #200일경우 잘 가고 응답까지 된 것


# ## robots.txt  윤리적으로 웹 스크래핑/크롤링

# In[21]:


#웹페이지메인주소/robots.txt 를 입력하면 robots.txt를 확인 할 수 있다

import requests

res=requests.get("http://www.naver.com/robots.txt")


# In[26]:


print(res.text) #user-agent: 규칙적용 대상, disallow :크롤링 금지페이지, allow 크롤링 허용 페이지
#모든 유저에게서 모든요청을 거부할거다. 
#allow  /$는 뒤에 로봇.txt가 붙지않은 순수한 홈페이지만 크롤링 허용


# In[31]:


#자주 사용하는 사이트 robots확인
res=requests.get("https://jjnsco.tistory.com/robots.txt")
print(res.text)


# In[ ]:




