#!/usr/bin/env python
# coding: utf-8

# In[1]:


#원하는 요소만 가져올 수 있도록 코드를 분석해 주는 라이브러리를 사용해보자
#beautifulsoup4
get_ipython().run_line_magic('pip', 'install beautifulsoup4')


# In[6]:


import requests

res=requests.get("http://www.example.com")
res.text
#res를 그대로 사용하지 말고 html parser에 전달해보자


# In[7]:


from bs4 import BeautifulSoup


# In[8]:


soup=BeautifulSoup(res.text,"html.parser") 
#생성자에 활용할 인자 res.text를 넣고 html로 파싱을 해줄 htm.parser입력

#prettify()를 활용해 분석된 html을 더 보기 편하게 변환해 주자
print(soup.prettify())


# In[9]:


#body 가져오기
soup.body


# In[12]:


#<p> 태그로 감싸진 요소 하나 찾기

soup.find("p")


# In[14]:


#특정 요소들을 한번에 찾기
soup.find_all("p") 


# In[15]:


h1=soup.find("h1")


# In[16]:


#태그 이름 가져오기 
h1.name


# In[17]:


#태그 내용 가져오기
h1.text


# ## 원하는 요소 가져오기   1)책 이름 모으기

# In[ ]:




