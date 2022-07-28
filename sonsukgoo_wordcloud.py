#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install selenium')
get_ipython().run_line_magic('pip', 'install webdriver-manager')


# In[ ]:





# In[26]:


#필요한 모듈 불러오기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

headlines=[]
from selenium.webdriver.support.ui import WebDriverWait
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://www.google.com/search?q=%EC%86%90%EC%84%9D%EA%B5%AC&sxsrf=ALiCzsbRbfnTz13sCo8JdvXtcMQyPLhXPQ:1658979550856&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi03cW21Jr5AhUCRd4KHVWmCloQ_AUoA3oECAIQBQ&biw=782&bih=744&dpr=1.25")
    driver.implicitly_wait(10)
    for i in range(1,11):
        element=driver.find_element(By.XPATH,'//*[@id="rso"]/div[{}]/div/a/div/div[2]/div[2]'.format(i))
        headlines.append(element.text.strip())
    print(headlines)


# In[27]:


get_ipython().run_line_magic('pip', 'install wordcloud')
get_ipython().run_line_magic('pip', 'install konlpy')


# In[25]:


#웹사이트에서 긁어와 저장해둔 a를 활용해 시각화를 해보자
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#횟수기반 딕셔너리 생성
from collections import Counter

#문장에서 명사를 추출하는 형태소 분석 라이브러리
from konlpy.tag import Hannanum


# In[29]:


hannanum=Hannanum()
words=[]
for ai in headlines:
    nouns=hannanum.nouns(ai)
    words+=nouns
counter=Counter(words)
counter


# In[31]:


wordcloud=WordCloud(
    font_path='C:\\Users\\jiin\\font\\HBIOSSYS.ttf',
    background_color="white",
    width=3000,
    height=3000,
    
)
img=wordcloud.generate_from_frequencies(counter)
plt.imshow(img)


# In[57]:


user_agent={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
import requests
from bs4 import BeautifulSoup

import time
works=[]
res=requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjky&x_csa=%7B%22fromUi%22%3A%22kb%22%7D&pkid=1&os=6263698&qvt=0&query=%EC%86%90%EC%84%9D%EA%B5%AC%20%EC%9E%91%ED%92%88%ED%99%9C%EB%8F%99",{"User-Agent":user_agent})
soup=BeautifulSoup(res.text,"html.parser")

parsed_data=soup.find_all("strong","this_text")
for data in parsed_data:
    works.append(data.text.strip())
    time.sleep(0.5)
print("최근 드라마 작품 = "+works[0])
print("정주행 list")
print(works)


# In[ ]:




