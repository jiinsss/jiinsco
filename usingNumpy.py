#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


#numpy


# In[3]:


#numpy


# In[5]:


#numpy


# In[6]:


##numpy


# In[7]:


x=np.array([1,2,3])
c=5

print("더하기 : {}".fromat(x+c))


# In[8]:


x=numpy.array([1,2,3])
c=5

print("더하기 : {}".fromat(x+c))


# In[12]:


x=numpy.array([1,2,3])
c=5

print("더하기 : {}".format(x+c))
print("곱하기 : {}".format(x*c))
print("나누기 : {}".format(x/c))
print( "".format(x+c))


# In[13]:


y= numpy.array([1,3,5])
z=numpy.array([1,2,3,4])
print("더하기 : {}".format(y+z))
print("곱하기 : {}".format(y*z))
print("나누기 : {}".format(y/z))


# In[14]:


w=numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

w[0,0]


# In[15]:


w[1,2]


# In[16]:


w[1:1,1:2]


# In[17]:


w=numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

w[1:1,1:2]


# In[18]:


w[1:1, 1:2]


# In[19]:


w=numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
w[0:2,1:3] # 인덱스로 범위 지정


# In[27]:


a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
x=numpy.array([0,1,0])
print(a+x)
print(x)
#broadcasting
bx=x[:,None] #전치행렬 
print(bx)
print(a+bx)


# In[29]:


y=numpy.array([0,1,-1])
print(a*y)


# In[31]:


t=numpy.array([1,2,3])
a=t[:,None]
u=numpy.array([2,0,-2])
print(t+u)
print(a+u)


# In[37]:


#zero
#
numpy.zeros((3,3,3))
numpy.ones((3,3,3))


# In[41]:





# In[43]:


numpy.zeros(3) #영행렬, 공간이 원점으로 축소


# In[42]:


numpy.diag((2,4))#대각행렬


# In[44]:


numpy.eye(2,dtype=int)#항등행렬


# In[46]:


mat_1=numpy.array([[1,4],[2,3]])
mat_2=numpy.array([[7,9],[0,6]])

mat_1.dot(mat_2)


# In[49]:


#trace : main daigonal 합(대각선합)
arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
arr.trace()


# In[50]:


#행렬식 determinant numpy.linalg.det()
#선형변환 과정에서 vector의 scaling(영역의 변화) 척도
#3이면 기존의 3배, 1/2 이면 기존의 반
arr_2=numpy.array([[2,3],[1,6]])
numpy.linalg.det(arr_2)


# In[51]:


numpy.linalg.inv(arr_2)#역행렬


# In[52]:


#고유값과 고유벡터

mat=[[2,0,-2],[1,1,-2],[0,0,1]]
numpy.linalg.eig(mat)


# In[53]:


eig_val,eig_vec=numpy.linalg.eig(mat)
eig_val


# In[54]:


eig_vec


# In[58]:


eig_val[0] * eig_vec[:,0]  #(lamda)x


# In[69]:


x=numpy.array([1,2,3])
numpy.linalg.norm(x, ord=1) #n1 norm 
numpy.linalg.norm(x, ord=2)#n2 norm 


# In[71]:


#is this singular matrix?
y=numpy.array([[1,2],[3,4]])
a=numpy.linalg.det(y)
if a==0:
    print("singular matrix")
else:
    print("not singular matrix")
        


# ## markdown

# ### prerequisite : Table
# -행과 열을 이용해서 데이터를 저장하고 관리하는 자료구조(컨테이너)
# 
# -주로 행은 개체, 열은 속성을 나타냄
# 

# In[75]:


import pandas as pd


# ## series?
# -1-D labeled array
# 
# -인덱스를 지정해 줄 수 있음
# 

# In[85]:


s= pd.Series([1,4,9,16,25])
s
#b=s[0]
#b


# In[86]:


t= pd.Series({'one':1,'two':2})
t
#a=t['one'] #series는 dict와 비슷
#a


# In[87]:


s[s>s.median()]# 자기 자신이 median(중앙값) 보다 큰 값들만 가지고 와라


# In[88]:


numpy.exp(s)


# In[89]:


s.dtype


# In[91]:


#series에 값 추가
t['six']=6
t


# In[92]:


'six' in t #boolean


# In[93]:


'seven' in t


# In[94]:


t.get('seven')


# In[95]:


t.get('seven',0)


# # series에 이름 붙이기
# name 속성을 가지고 있다, 처음 seriese를 만들때 이름을 붙일 수 있다

# In[99]:


s= pd.Series(numpy.random.rand(5), name="random_nums")
s


# In[100]:


s.name="임의의 난수"
s


# ## pandas로 2차원 데이터 다루기 - dataframe
# dataframe? -2d labeled table
# - 인덱스를 지정할 수도 있음
# 

# In[101]:


d={"height":[1,2,3,4],"weight":[30,40,50,60]}
df=pd.DataFrame(d)
df


# In[103]:


df.dtypes #data type 확인


# ## From csv to dataframe
# - comma separated value를 data frame으로 생성해줄수있다
# - read.csv() 사용

# In[117]:


# 주피터 폴더가 저장된 경로에 country csv존재하면

covid = pd.read_csv("./country_wise_latest.csv")

covid


# In[120]:


#위에서부터 5개를 관찰하는 방법(함수)

covid.head(5) #head(n) 처음 n개의 데이터를 참조


# In[121]:


covid.tail(5) #tail(n) 마지막 n개의 데이터를 참조


# In[122]:


## 데이터 접근하기

#df['column_name'] or df.column.name

covid['Active']


# In[124]:


#covid.WHO Region


# In[125]:


type(covid['Active']) # dataframe의 각 column은 Seriese다


# In[126]:


covid['Active'][0]


# In[127]:


covid['Active'][1:5]


# In[128]:


# 조건을 이용해서 데이터 접근하기

#신규 확진자가 100 명을 넘는 나라 top5 찾기

covid[covid['New cases'] > 100].head(5)



# In[133]:


#who 지역이 동남아시아인 나라 찾기

covid['WHO Region'].unique()
covid[covid['WHO Region']=='South-East Asia']


# In[137]:


# 행을 기준으로 데이터 접근하기 

#예시 데이터 - 도서관 정보

books_dict={"Available":[True,True,False], "Location":[102,215,323],"Genre":["Programming","Physics","Math"]}
books_df=pd.DataFrame(books_dict,index=['버그란 무엇인가','물리학이다','미분학이다'])

books_df


# In[138]:


#인덱스를 이용해 가져오기    .loc[row,col]
books_df.loc["버그란 무엇인가"]


# In[140]:


#미분학이다 대출 가능한지
#books_df.loc["미분학이다"]['Available']
books_df.loc["미분학이다",'Available']


# In[143]:


#숫자 인덱스를 이용해서 가져오기    .iloc[rowidx,colidx]
books_df.iloc[0,1]
#books_df.iloc[1, 0:1] #인덱스 1행의 0~1열 가져오기


# In[153]:


#groupby

#split(쪼갬), apply(통계함수 sum,min,median을 적용해서 각 데이터 압축)
#combine(apply된 결과를 바탕으로 새로운 Series 생성(group_key:applied value))

covid.head

#WHO Region별 확진자수
#1.covid에서 확진자 수 column만 추출
#2.이를 covid의 who Region을 기준으로 group by

covid_by_region=covid['Confirmed'].groupby(by=covid["WHO Region"])

covid_by_region


# In[154]:


covid_by_region.sum()


# In[155]:


#국가당 감염자 수 
covid_by_region.mean() #sum() / 국가 수


# In[172]:


#mission
#covid 데이터에서 100 case 대비 사망률(Deaths/100case) 가장 높은 국가?
#covid['Deaths / 100 Cases']==covid['Deaths / 100 Cases'].max()
#covid[covid['Deaths / 100 Cases']==covid['Deaths / 100 Cases'].max()]
covid[covid['Deaths / 100 Cases']==covid['Deaths / 100 Cases'].max()]['Country/Region']


# In[183]:


#covid 데이터에서 신규확진자가 없는 나라중 who region 이 Europe인걸 모두 출력

covid_case=covid['New cases']==0
covid_region=covid['WHO Region']=='Europe'
answer=covid[covid_case & covid_region]

answer


# In[ ]:


#avocado = pd.read_csv("./archive/avocado.csv")
#exp = avocado.groupby(avocado['region'])
#exp.max()

