#!/usr/bin/env python
# coding: utf-8

# In[8]:


#라이브러리 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


esales_df=pd.read_csv("./sales.csv")


# In[10]:


esales_df #주문량이 높은 고객부터 배치


# ## 목적
# ### 1. 요일별 수익 비교
# ### 2. 요일별 주문 비교 
# ### 3. 시간대 별 수익, 주문 비교
# ### 4. 한달간 수익
# ### ->  1~4를 고려해서 프로모션 시기 및 시간 결정
# ### 5. 고객의 총 주문수대비 이익을 비교해 상위고객과 하위고객 비교
# ### 6. 최초 주문날짜와 최신 주문 날짜 그리고 총 주문수를 비교해 고객별 사용 빈도수 측정
# ### 7. 최초 주문날짜와 최신 주문날짜가 일치하는 고객 비율 추출(일회성 고객)
# ### 8. 날짜별 최근 주문한 고객 수
# ### -> 5~8 를 고려해서 고객별 프로모션 기획 

# In[11]:


esales_df.describe()


# In[12]:


esales_df.info()


# In[13]:


#시간대별 수입비교, 주문 비교
time_revenue= esales_df[['TIME_0000_0600_REVENUE','TIME_0601_1200_REVENUE','TIME_1200_1800_REVENUE','TIME_1801_2359_REVENUE'  
 ]].sum()
tr=pd.DataFrame(time_revenue)
tr.rename(index={'TIME_0000_0600_REVENUE':'0-06','TIME_0601_1200_REVENUE':'06-12','TIME_1200_1800_REVENUE':'12-18','TIME_1801_2359_REVENUE':'18-24'},inplace=True)
tr_mean=float(tr.mean())
tr['mean']=tr_mean
tr.columns=['REVENUE','MEAN']
time_order= esales_df[['TIME_0000_0600_ORDERS','TIME_0601_1200_ORDERS','TIME_1200_1800_ORDERS','TIME_1801_2359_ORDERS']].sum()

to=pd.DataFrame(time_order)
to.rename(index={'TIME_0000_0600_ORDERS':'0-06','TIME_0601_1200_ORDERS':'06-12','TIME_1200_1800_ORDERS':'12-18','TIME_1801_2359_ORDERS':'18-24'},inplace=True)
to_mean=int(to.mean())
to['mean']=to_mean
to.columns=['ORDER','MEAN']
tr.plot(title="Time Revenue")
to.plot(title="Time Order")


# In[14]:


#일주일간 매출 비교 , 평균치 그리기

week_revenue= esales_df[['MONDAY_REVENUE','TUESDAY_REVENUE','WEDNESDAY_REVENUE','THURSDAY_REVENUE','FRIDAY_REVENUE','SATURDAY_REVENUE','SUNDAY_REVENUE']].sum()
wr=pd.DataFrame(week_revenue)
wr.rename(index={'MONDAY_REVENUE':'MR','TUESDAY_REVENUE':'TR','WEDNESDAY_REVENUE':'WR','THURSDAY_REVENUE':'THR','FRIDAY_REVENUE':'FR','SATURDAY_REVENUE':'STR','SUNDAY_REVENUE':'SR'},inplace=True)
wr_mean=float(wr.mean())
wr['mean']=wr_mean

#일주일간 주문 비교 , 평균 치 그리기
week_order=esales_df[['MONDAY_ORDERS','TUESDAY_ORDERS','WEDNESDAY_ORDERS','THURSDAY_ORDERS','FRIDAY_ORDERS','SATURDAY_ORDERS','SUNDAY_ORDERS']].sum()
wo=pd.DataFrame(week_order)
wo.rename(index={'MONDAY_ORDERS':'MO','TUESDAY_ORDERS':'TO','WEDNESDAY_ORDERS':'WO','THURSDAY_ORDERS':'THO','FRIDAY_ORDERS':'FO','SATURDAY_ORDERS':'STO','SUNDAY_ORDERS':'SO'},inplace=True)
wo_mean=wo.mean()
wo['mean']=int(wo_mean)
wr.plot(title="Week Revenue")
wo.plot(title="Week Order")


# In[15]:


#일주일간 수입, 주문 비교 
fwr=wr.drop(['mean'],axis=1)
fwo=wo.drop(['mean'],axis=1)
#같은 범위에서 비교하기 위해 order 값을 보정해줌
fwr_sum=int(fwr.sum())
fwo_sum=int(fwo.sum())
fwo_f=fwo/fwo_sum*fwr_sum
plt.plot(range(1,8),fwr, label='REVENUE')
plt.plot(range(1,8),fwo_f,label='ORDER')
plt.legend()
plt.title("A week's Revenue and Order Tendency")
plt.show()


# In[16]:


esales_df.info()


# In[17]:


## 한달간 수익, 주문

month_revenue=esales_df[['WEEK1_DAY01_DAY07_REVENUE','WEEK2_DAY08_DAY15_REVENUE','WEEK3_DAY16_DAY23_REVENUE','WEEK4_DAY24_DAY31_REVENUE' ]].sum()
mr=pd.DataFrame(month_revenue)
mr.rename(index={'WEEK1_DAY01_DAY07_REVENUE':'1week','WEEK2_DAY08_DAY15_REVENUE':'2week','WEEK3_DAY16_DAY23_REVENUE':'3week','WEEK4_DAY24_DAY31_REVENUE':'4week' },inplace=True)
mr_mean=mr.mean()
mr['mean']=int(mr_mean)


month_order=esales_df[['WEEK1_DAY01_DAY07_ORDERS','WEEK2_DAY08_DAY15_ORDERS','WEEK3_DAY16_DAY23_ORDERS','WEEK4_DAY24_DAY31_ORDERS'
]].sum()
mo=pd.DataFrame(month_order)
mo.rename(index={'WEEK1_DAY01_DAY07_ORDERS':'1week','WEEK2_DAY08_DAY15_ORDERS':'2week','WEEK3_DAY16_DAY23_ORDERS':'3week','WEEK4_DAY24_DAY31_ORDERS':'4week'
},inplace=True)
mo_mean=mo.mean()
mo['mean']=int(mo_mean)
mr.plot(title="Month Revenue")
mo.plot(title="Month Order")



# In[18]:


#일주일간 수입, 주문 비교 
fmr=mr.drop(['mean'],axis=1)
fmo=mo.drop(['mean'],axis=1)
#같은 범위에서 비교하기 위해 order 값을 보정해줌
fmr_sum=int(fmr.sum())
fmo_sum=int(fmo.sum())
fmo_f=fmo/fmo_sum*fmr_sum
plt.plot(range(1,5),fmr, label='REVENUE')
plt.plot(range(1,5),fmo_f,label='ORDER')
plt.legend()
Month_R_O_Tendency=plt.title("A month's Revenue and Order Tendency")
plt.show()
#plt.savefig('./sin.png')


# In[19]:


#한달수익, #일주일수익 #시간별 수익 subplot

fig=plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
#plt.plot(Month_R_O_Tendency)
plt.plot(tr)
plt.legend("vm")
plt.title("Time Revenue")

plt.subplot(1,3,2)
plt.plot(wr)
plt.legend("vm")
plt.title("Week Revenue")


plt.subplot(1,3,3)
plt.plot(mr)
plt.legend("vm")
plt.title("Month Revenue")






# In[20]:


fig=plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.plot(to)
plt.legend("vm")
plt.title("Time Order")

plt.subplot(1,3,2)
plt.plot(wo)
plt.legend("vm")
plt.title("Week Order")

plt.subplot(1,3,3)
plt.plot(mo)
plt.legend("vm")
plt.title("Month Order")


# ### 고객 분석

# In[227]:


### 4. 고객의 총 주문수대비 이익을 비교해 중요 고객 파악과 고객별 소비성향 파악
### 높은 수익을 내는 물건을 구매하는 고객과 낮은 수익을 내는 물건을 구매하는 고객
RT=esales_df['REVENUE'].div(esales_df['TOTAL_ORDERS'])
a=pd.concat([esales_df['CustomerID'],RT],axis=1)
a.columns=['CustomerID','RV/TOD']
a.sort_values(by='RV/TOD',ascending=False)

ah=a.head(5)
at=a.tail(5)

aa=pd.concat([ah,at])
aa.sort_values('RV/TOD',ascending=False).plot.bar(x='CustomerID',y='RV/TOD',rot=0, color=['g','g','g','g','g','b','b','b','b','b'],figsize=(12,5), title="Top5&Bottom5 Customer's ratio of Revenue/Total_Orders")


# In[229]:


esales_df[['CustomerID','FIRST_ORDER_DATE','LATEST_ORDER_DATE','TOTAL_ORDERS']]
#esales_df['LATEST_ORDER_DATE'] - esales_df['FIRST_ORDER_DATE']

LT=pd.to_datetime(esales_df['LATEST_ORDER_DATE'])
FT=pd.to_datetime(esales_df['FIRST_ORDER_DATE'])
b=LT-FT
bc=pd.concat([esales_df['CustomerID'],b],axis=1)

bd=pd.DataFrame(bc)
bd.columns=['CustomerID','d_days']
days_num=bd['d_days'].dt.days
frequency=esales_df['TOTAL_ORDERS']/days_num
fre_cus=pd.concat([bd,frequency],axis=1)
fre_cus.columns=['CustomerID','d_days','frequency']
fre=fre_cus.loc[fre_cus['d_days']!='0days']
free=fre.sort_values(by='frequency',ascending=False)
fh=free.head(10)

fh.sort_values('frequency',ascending=False).plot.bar(x='CustomerID',y='frequency',rot=0, color=['g'],figsize=(12,5), title="Top10 ratio of Total_Orders/time")


### 5. 가입기간과 총 주문수를 비교해 사용 빈도수 측정
### 가입기간 동안 주문을 많이 한 고객 10명


# In[113]:


## 1회성 구매고객 비율 원그래프
c=b

cc=pd.concat([esales_df['CustomerID'],c],axis=1)
cc.columns=['CustomerID','days']
allData=cc['days']
al=len(allData) #전체 고객수
count=0
cc['days']== '0days'
oneData=cc.loc[cc['days']=='0days']
onn=len(oneData) #1회성 고객수
notonn=al-onn #1회성 제외 고객수

dfpie=pd.Series([notonn,onn],index=['not once','only once'])
plt.pie(dfpie, labels= dfpie.index, colors=['silver','purple'],autopct='%.1f%%')


# In[260]:


lon = esales_df[['CustomerID','LATEST_ORDER_DATE',]]
### 6.날짜별 최근 주문한 고객 수
long=lon.sort_values(by='LATEST_ORDER_DATE',ascending=True)
longsize=long.groupby('LATEST_ORDER_DATE').size()
longg=pd.DataFrame(longsize)
longg.plot(title="Customer's Latest_order_date")
plt.legend("c")
plt.show()


# In[ ]:





# In[ ]:




