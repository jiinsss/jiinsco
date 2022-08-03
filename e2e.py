#!/usr/bin/env python
# coding: utf-8

# ## 데이터 다운로드
# 

# In[2]:


#python 3.5 이상부터 가능
import sys
assert sys.version_info >=(3,5)

#0.2이상 
import sklearn
assert sklearn.__version__ >="0.20"

import numpy as np
import os

#그래프그릴때 설정
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

#그린거 어디다 저장할거인지 지정
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "end_to_end_project"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Ignore useless warnings (see SciPy issue #5998)
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")


# In[3]:


#데이터를 호출하는걸 함수로 만들어 둚


import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"  #여기서 가져올거임
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# ### fetch_housing_data를 호출하면 현재 작업공간에 datasets/housing 이라는 디렉토리를 
# 
# ### 만들고 housing.tgz파일을 내려받고 풀어 housing.csv파일을 만든다

# In[4]:


fetch_housing_data()


# In[5]:


import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path =os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# ## 데이터 구조 훑어보기

# In[6]:


housing =load_housing_data() #csv로 만든거 확인
housing.head()

#median_house_value 예측 할 값의 중간 값
#경도,위도로 나눠진 각 행은 구역(block)/지역 을 나타낸다
#total room은 해당 지역 전체의 방수



# In[7]:


housing.info() #결측값 존재 유무 확인-> 다 non- null count를 확인해보면 
#total_bedrooms이 20433으로 다른 행들보다 적게 존재


# In[8]:


#범주형 필드 ocen_proximity 의 요약-> value_counts()

housing["ocean_proximity"].value_counts()

#ocean_proximity 값의 종류를 세줌


# In[9]:


#숫자형 필드 그 나머지 것들 의 요약-> descriobe()
housing.describe()


# In[10]:


#persentage 해석 = 전체중 50%구역은 housing_median_age는 29년보다 작다


# ### 히스토그램으로 데이터 분석해보기
# 

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
housing.hist(bins=50 , figsize=(20,15)) #bin 막대그래프 가로사이즈, 클수록 가늘어짐, #figsize 그래프사이즈
save_fig("attribute_histogram_plots")
plt.show()


# In[12]:


#median income 수입의 중간값의 경우 가로가 수익일텐데 0,2,4처럼 작은 숫자이다(만불 단위로 나뉘어서 적혀있을 가능성 있음)

#housing median age , median housevalue 둘다 마지막 부분에 줄다가 극단적으로 증가하는 이상한 양상
## ㄴ> 특정값 이상에 대해서는 뭉뜽그려서 묶어놔서 제한을 뒀을 가능성이 있음

## ===> 데이터 정제 한 사람과 의사소통 필요, 이상 값들은 제외를 하는게 더 나을 수 있음



# ### 테스트 데이터셋을 만들기
# 
# ### 충분한 데이터가 있으면 보통 20% 사용
# ### 초기의 경우 데이터셋이 많이 없을 수 있어서 하나의 데이터셋을 훈련, 테스트용으로 분리하는것이 일반적

# In[13]:


#랜던 작업 실행
np.random.seed(42)

#주어진 데이터에서(인풋) 일정한 비율test_ration로 뽑아내는 함수 작성
#랜덤함수에서 permutation(n) = n개의 숫자를 0부터 시작하도록 섞어서 뽑아냄
#:testsetsize ,testsetsize: 첫번째 몇개까지 뽑고 그 후 나머지부분을 test와 train에 각각 넣음
#iloc [train_incides] 지정된 범위의 데이터 인덱스에 iloc으로 접근해 뽑아와서 저장

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


# In[14]:


a= np.random.permutation(10)
a


# In[15]:


train_set, test_set =split_train_test(housing,0.2)
len(train_set), len(test_set)


# ### 이렇게 train과 test데이터를 나눴지만
# ### 새로운 데이터가 들어 온 경우 또 다시 train과 test를 나눠야하는데 이때 그 전에 나눠뒀던게 다시 섞일 수 있음
# ## 각 샘플마다 식별자가 있다면 그것을 사용해 분할 하면 이를 방지 할 수 있다
# 
# ## 식별자가 있을때(들어왔을 때) 식별자를 해싱시키고(crc32) 2의 32승으로 나눈 값이 testration 보다 작다면 true를 리턴 = test에 속하면 true를 리턴하겠다 
# ### 식별자가 유일하다면 return값이 계속 같을 것임

# In[16]:


from zlib import crc32
#2의 32승보다 1작은 숫자 0xff~
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32
#식별이 끝났다면 test data split함수에 나눌 기준이 될 id_column을 추가해줌

#앞서 나눴던 건 그냥 나눴던거고 이번에는 식별자를 갖고 나눌거임
def split_train_test_by_id(data, test_ratio, id_column):
    ids=data[id_column]
    in_test_set=ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[-in_test_set],data.loc[in_test_set]


# ### 인덱스를 id column으로 추가하기

# In[17]:


housing_with_id = housing.reset_index()
train_set,test_set = split_train_test_by_id(housing_with_id, 0.2, "index")


# In[18]:


housing.head()


# In[19]:


housing_with_id.head() #위의 그래프와 다르게 index가 추가됨


# #### 위 방법 인덱스를 갖고 id 칼럼으로 추가할때 문제점은
# #### id가 되려면 항상 일정하게 유지가 되어야 하는데 행 번호를 id로 쓰면 중간에 데이터가 유실되면
# #### 아래값들이 위로 채워지며 올라와 id 값이 바뀔 수 있다
# #### 또한 id 값들이 영향을 안받으려면 뒤에다 값을 집어넣어야 한다는 제한도 있다
# 
# ### id 값은 unique해야한다

# ### ->경도와 위도를 사용해 id를 만듦

# In[20]:


housing_with_id["id"] = housing["longitude"] *1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")


# In[21]:


train_set.head()  #맨 마지막 열에 경도와 위도로 만든 id라는 feature 추가됨


# ### scilkit-learn에서 기본적으로 제공되는 데이터 분할 함수

# In[22]:


from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)


# #### 다음 데이터 분할 함수를 사용하면 id를 사용해 잘 분할했다 하더라도 
# #### 테스트 데이터가 전체의 특성을 잘 보여주지 못하는 경우가 발생한다 
# #### 투표비율의 경우 전체 비율의 특성을 test데이터에서도 잘 보여주도록 해야하는데
# #### 이때 사용하는 방법이 계층적 샘플링이다
# 
# ### 계층적 샘플링(stratified sampling)
# #### 전체 데이터를 계층이라는 동질의 그룹으로 나누고, 테스트 데이터가 전체 데이터를 잘 대표하도록 각 계층에서 올바른 수의 샘플을 추출
# 
# #### 모든 속성을 다 샘플링 하기에 힘드니까 목표값이 되는 housing value를 제외하고 이 목표값과
# #### 가장 연관이 있을 것 같은 값들을 가지고 테스트를 해봄
# 
# 

# In[23]:


#히스트그램으로 한번 살펴봄 집의 가격은 income과 비슷할것이다
housing["median_income"].hist()


# In[25]:


#연속적인 값에 가깝(다양한값)기때문에 계층척 샘플링을 하기 어렵다
# 따라서 그룹으로 나눔 카테고리화
#판다스의 cut 함수 사용
housing["income_cat"]= pd.cut(housing["median_income"],
                              bins=[0., 1.5, 3.0, 4.5, 6., np.inf], #0~1.5,1.5~3,
                              labels=[1, 2, 3, 4, 5])


# In[26]:


#나눈 값들의 빈도수 분포 보기
housing["income_cat"].value_counts()


# In[27]:


housing["income_cat"].hist()


# In[30]:


#계층적 샘플링을 sklearn에서 이미 제공함  StratifiedShuffleSplit 

from sklearn.model_selection import StratifiedShuffleSplit
#테스트 사이즈는 그대로 0.2 (20퍼센트)
split=StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
#어떤 특성에 대해  샘플링을 할건지 (앞에서 생성했던 income_cat 입력)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


# In[31]:


strat_train_set.info() #16512 -80%


# In[32]:


strat_test_set.info() #4128 -20%


# ### 새로 생성했던 특성 income cat이 테스트 데이터에서도 분포를 유지하고 있는지 확인
# 

# In[38]:


#비율을 보기 위해 전체 데이터 개수로 나눠줌
#전체 값에서의 비율
housing["income_cat"].value_counts() / len(housing)


# In[37]:


#테스트 값에서의 비율
strat_test_set["income_cat"].value_counts() /len(strat_test_set)
#거의 같은값임


# ### 데이터 이해를 위한 탐색과 시각화

# In[39]:


#이제 income cat 안쓰니까 drop 해줌
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat",axis=1,inplace=True)


# In[40]:


#원래 데이터 손상 방지를 위해 복사본 만들기
housing =strat_train_set.copy()  #train 데이터 카피한게 이제 housing임


# ### 지리적 데이터 시각화 - train data

# In[43]:


housing.plot(kind="scatter",x="longitude",y='latitude')
save_fig("bad_visualization_plot")


# #### 밀집된 영역표시 alpha 옵션 주기

# In[51]:


housing.plot(kind="scatter",x="longitude",y='latitude', alpha=0.1)
save_fig("better_visualization_plot")


# #### 더 다양한 정보 표시
# #### s 원의 반지름 -> 인구
# #### c 색상 -> 가격

# In[141]:


housing.plot(kind="scatter",x="longitude",y='latitude', alpha=0.4,
             s=housing["population"]/100, label="population", figsize=(10,7),
             c="median_house_value",cmap=plt.get_cmap("jet"), colorbar=True,
             sharex=False
            )
plt.legend()
save_fig("housing_price_satterplot")

# color -> 집값이 붉을수록 비쌈
# scale -> 원의 크기가 클수록 인구가 많이있음


# In[ ]:


#지도와 앞서 만든 그래프 같이 프린트하기 -> 지역 찾기에 좋음

# Download the California image
images_path = os.path.join(PROJECT_ROOT_DIR, "images", "end_to_end_project")
os.makedirs(images_path, exist_ok=True)
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
#DOWNLOAD_ROOT = "https://ko.wikipedia.org/wiki/%EC%BA%98%EB%A6%AC%ED%8F%AC%EB%8B%88%EC%95%84%EC%A3%BC#/media/%ED%8C%8C%EC%9D%BC:USA_California_location_map.svg"
filename = "california.png"


import matplotlib.image as mpimg
california_img=mpimg.imread(os.path.join(images_path, filename))
ax = housing.plot(kind="scatter", x="longitude", y="latitude", figsize=(10,7),
                       s=housing['population']/100, label="Population",
                       c="median_house_value", cmap=plt.get_cmap("jet"),
                       colorbar=False, alpha=0.4,
                      )
plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5,
           cmap=plt.get_cmap("jet"))
plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)

prices = housing["median_house_value"]
tick_values = np.linspace(prices.min(), prices.max(), 11)
cbar = plt.colorbar()
cbar.ax.set_yticklabels(["$%dk"%(round(v/1000)) for v in tick_values], fontsize=14)
cbar.set_label('Median House Value', fontsize=16)

plt.legend(fontsize=16)
save_fig("california_housing_prices_plot")
plt.show()


# ### 상관관계(CORRELATIONS)관찰
# 
# 

# In[ ]:


### 1과 -1로 갈수록 강한 상관관계로 감(절댓값이 클수록)
#-1  은 음의 상관관계  1은 양의 상관관계

corr_matrix = housing.corr()

corr_matrix["median_house_value"].sort_values(ascending=False)

#median income 수입이 medina value 집값과 가장 큰 상관관계를 보임 0.68
#latitude 음의 상관관계 -0.14 -> 비교적 음의 상관관계가 있는데 위쪽으로 올라갈수록 평균 집값이 내려간다


# In[ ]:


#### housing value와 연관 있을것같은 속성들에 대하 상관관계를 관찰해보자


# In[66]:


from pandas.plotting import scatter_matrix

attributes =["median_house_value","median_income","total_rooms","housing_median_age"]

#집값, 방수, 몇년된집
scatter_matrix(housing[attributes], figsize=(12,8))
save_fig("scatter_matix_plot") #대각선 방향의 막대그래프는 자기 자신에 대한 값이라 히스토그램을 보여줌

#상관관계가 클 경우 선형적인 모습을 보임(1,2)처럼


# In[69]:


#(1,2)를 확대해보자
housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
plt.axis([0, 16, 0, 550000])
save_fig("income_vs_house_value_scatterplot")

#문제점 발견
#50만불에서 선형적인 양상을 가짐 -> 데이터 생성시 경계값 제한(50만 이상 뭉탱구리)
#중간에도 선형 양상이 보임 --> 이러한 선형양상의 값들은 제외시켜주는게 좋음


# ### 특성 조합들 실험
# ### 여러특성의 조합으로 세로운 특성만들기, 예를들면 가구당 방개수, 침대방의 비율, 가구당 인원

# In[71]:


housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]

corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

#median income 1위, rooms per household 2위
#bedrooms per room 강한 음의 상관관계  -> 한 집에 있는 방 중 침실의 비율인데 보통 침실갯수는 일정해서
# 총 방수가 분모로 들어가 총 방수가 적을수록 값이 증가해 음의 상관관계를 갖는다


# ### 머신러닝 알고리즘을 위한 데이터 준비
# #### 데이터 준비는 데이터 변환과정으로 볼수 있으며 데이터 수동변환과 자동변환(함수만들기)이 있다
# #### 데이터 자동 변환의 장점
# #### 새로운 데이터에대한 변환을 손쉽게 재생산 할 수 있다
# #### 향후 재사용 할 수 있는 라이브러리를 구축하게 된다
# #### 실제 시스템에서 가공되지 않은 데이터를 알고리즘에 쉽게 입력으로 사용할 수 있도록 해줌
# #### 여러 데이터 변환 방법을 쉽게 시도해 볼 수 있다

# In[75]:


housing = strat_train_set.drop("median_house_value",axis=1) #목표값 feature인 median house value 값을 떼고
housing_labels=strat_train_set["median_house_value"].copy() # 여기에 저장
# 목표값은 굳이 가공할 필요가 없기 때문


# ### 데이터 정제
# #### 누락된 값을 다루는 방법들
# #### - 해당 구역을 제거(행 제거)
# #### - 해당 특성을 제거(열 제거)
# #### -어떤 값으로 채움(평균, 중간값, 0 등)

# In[78]:


housing.isnull().any(axis=1) #인덱스 번호와 그 값들


# In[80]:


sample_incomplete_rows = housing[housing.isnull().any(axis=1)].head()
sample_incomplete_rows

#total bedfrooms nan(값이 없다 -> missing value를 포함하는 값들을 모았기 때문)


# In[83]:


#이제 누락된 값을 갖는 위의값 행을 제거해주면 된다 dropna

#total_bedrooms 의 값이 nan을 갖고 있을때 그행을 drop
sample_incomplete_rows.dropna(subset=["total_bedrooms"])


# In[85]:


# 열을 제거 drop

sample_incomplete_rows.drop("total_bedrooms",axis=1)


# In[91]:


# 어떤 값으로 채우기 -> 중간값으로 채워보자 fillna
# 채워넣는게 데이터 보존 측면에서 더 낫다
median= housing["total_bedrooms"].median()
sample_incomplete_rows["total_bedrooms"].fillna(median, inplace =True)
median


# In[89]:


sample_incomplete_rows


# #### 이러한 작업들(정제)을 간단히 끝낼 수 있음
# ### SimpleImputer사용하기

# In[93]:


from sklearn.impute import SimpleImputer
imputer =SimpleImputer(strategy = "median")

#median은 수치형만 계산 될 수 있어서 텍스트 속성 제외한 복사본 생성 후 넣어줌
housing_num = housing.drop("ocean_proximity",axis=1)

imputer.fit(housing_num)


# In[95]:


imputer.statistics_ # 그 값들 확인(housing feature의 median 값 계산)


# In[97]:


housing_num.median().values # 위의 계산값과 같음


# ### 이제 학습된 imputer 객체를 사용해 누락된 값을 중간값으로 바꿀 수 있다

# In[101]:


X= imputer.transform(housing_num)


# In[102]:


x[0] #data frame이 아닌 numpy array가 리턴됨


# In[104]:


#data frame으로 되돌리기

housing_tr = pd.DataFrame(x,columns=housing_num.columns, index=housing.index)


# In[105]:


### 제대로 채워져 있는지 확인


# In[106]:


sample_incomplete_rows.index.values  #아까 null 뽑아둔거 인덱스 , 즉  결측치가 있는 값들의 인덱스


# In[107]:


housing_num.loc[sample_incomplete_rows.index.values ] #아무것도 안한거, 결측치 nan존제


# In[109]:


housing_tr.loc[sample_incomplete_rows.index.values ] # imputer로 중간값으로 채워진 것들, 결측지가 중간값으로 채워짐


# ### Estimator, Transformer, predictor
# 
# ### 1. Estimator (추정기)
# #### 앞서 사용햇던 imputer,linear regression(선형회귀)들이 이에 해당되는데 
# ### 추정기는 데이터 셋이 input으로 들어오면 파라미터 값들을 구하는 것이다
# #### 즉 imputer에서의 파라미터는 median 이었고 linear에서는 feature 개수였다
# #### 이 과정은 fit() 이라는 함수로 진향되고, 데이터셋을 매개변수로 전달받는데
# #### 지도학습의 경우 label을 담고 있는 데이터셋이 매개변수로 전달된다
# 
# ### 2. 변환기(tranformer)
# ### 예측하는 것 뿐 아니라 변환까지 시키는 것으로 imputer가 이에 역시 해당된다
# #### fit() 이 이루어진 값들이 들어오고 transform() 함수를 통해 동작이 수행되고 변환된 데이터셋을 반환
# 
# 
# ### 3. predictor(예측기)
# #### 추정기중 일부는 새로운 데이터 셋에 대해 예측값을 생성 할 수 있다( linear regression

# ### 텍스트와 범주형 특성 다루기

# In[143]:


housing_cat = housing[["ocean_proximity"]]
housing_cat.head(10)
#이러한 텍스트들을 numerical 한 값으로 바꿔줘야함


# In[144]:


from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat) #fit과 transform 한번에 처리
housing_cat_encoded[:10]


# In[145]:


ordinal_encoder.categories_   
#categories들을 학습해서 아래의 unique한 값들을 생성했고 순서에 따라
#1H ocean이면 1로 바꾸고 inland 이면 4 로 바꾸는 등 이런식으로 변환시팀


# #### 이 표현 방식의 문제점은 
# #### sklearn이 inland 와 같은 string 갑의 유사도에 따라 순서를 정한거라 실제 inland의 위치순 등의
# #### 의미 있는 순서 배열이 힘들다
# 
# 
# ### 이때 사용하는게 one-hot encoding
# 

# In[146]:


from sklearn.preprocessing import OneHotEncoder

cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat) #fit과 transform 한번에 처리
housing_cat_1hot


# #### 인코딩을 했을때 대부분의 값이 0이고 한 값만 1이 되어서 이걸 optimize하기 위해 사용하는게 sparse matrix
# #### 이걸 다시 일반 matrix 로 바꿔줘야함

# In[147]:


# 1.toarray()사용
housing_cat_1hot.toarray().shape #각 행에 5개의 값이 들어가있음 (16512,5)
# 이 다섯개의 값중 하나만 1이 되는게 one hot encoder
housing_cat_1hot.toarray()


# In[148]:


# 2.sparse 옵션을 false로 두면 걍 바로 일반 mat로 나옴

cat_encoder = OneHotEncoder(sparse=False)
housing_cat_1hot = cat_encoder.fit_transform(housing_cat) #fit과 transform 한번에 처리
housing_cat_1hot


# #### 결측값을 어떻게 처리할 것인가 
# ### 나만의 변환기 만들기
# 
# #### 반드시 구현해야 할 함수-> fit()   transfrom()
# 
# #### 조합으로 만들었던 rooms per household, population_per_household 두개의 새로운 특성을 데이터 셋에 추가해
# #### add_bedrooms_per_room 값이 true 로 주어지면 bedrooms_per_room 특성까지 추가 -> add bedroom은 하이퍼파라미터이다
# 
# #### 모델 학습에 효과적인 여러가지 경우를 시도해볼때 이 하이퍼파라미터를 가지고 조합을 수행해 더 효과적으로 수행할 수 있음

# In[149]:


from sklearn.base import BaseEstimator, TransformerMixin
#baseEstimator, transformermixin을 상속받은 클래스 작성
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6
# 데이터 안에 있는 값을 변경 할 수 있으니까 인덱스 지정해둠

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # 하이퍼파라미터 add bed 옵션 사용
        self.add_bedrooms_per_room = add_bedrooms_per_room #옵션을 사용해 변수 설정
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X): # X는 numpy array(data set)
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room: #이게 true면
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix] #변수 생성
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]# np.c_ 여러 값들을 합침 #생성했던거까지 3개 전달 
        else:
            return np.c_[X, rooms_per_household, population_per_household]#false면 생성했던 feature 빼고 전달

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False) #add bed 가 false일때 생성이니까
housing_extra_attribs = attr_adder.transform(housing.values) #이게 반환될때 X로감


# In[150]:


# 바로 위의 return 값은 numpy array형태라 dataframe으로 변환시켜줌
housing_extra_attribs = pd.DataFrame(
    housing_extra_attribs,
    columns=list(housing.columns)+["rooms_per_household", "population_per_household"],#두개만 생성
    index=housing.index)
housing_extra_attribs.head()


# #### 특정 범위에 있는것만 뽑기,featuare들의 범위들이 다 다르면 모델학습에 어려움이 있을 수 있음
# 
# ### 이때 사용하는게 특성 스케일링
# #### min, max가 0-1 사이에 있도록 조정
# #### 표준화(standardization) : 평균이 0 분산이 1이 되도록 만들어줌 (sklearn의 StanderScaler 사용)
# 
# ### 변환 파이프라인(Transformation Pipelines)
# #### 여러개의 변환이 순차적으로 이루어져야 할 경우 사용

# In[154]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")), # median으로 결측치 채우기("imputer"이름의 추정기)
        ('attribs_adder', CombinedAttributesAdder()), # 앞에서 customizing한 클래스로 만든새로운 특성 추가하기
        ('std_scaler', StandardScaler()), # 표준화하기
    ])

housing_num_tr = num_pipeline.fit_transform(housing_num) #housing_num은 ocean ~를 제외한 수치형 데이터임


# #### 이름, 추정기쌍의 목록
# #### 마지막 std_scaler 은 fit() 만 나머지 위의 두개는 fit() 과 transform() 함수를 가지고 있어야함
# #### 이제 이 변환기 및 추정기들이 적힌 순서대로 호출하고 진행함

# In[157]:


housing_num_tr #파이프라인 사용 전과는 다른 값이 나옴


# #### 각 열마다 다른 파이프라인을 적용 할 수 있음 
# #### 예를들어 수치형과 범주형들에 대해 별도의 변환이 필요하다면
# ### ColumnTransfomer를 사용하면 됨

# In[159]:


from sklearn.compose import ColumnTransformer

num_attribs = list(housing_num) # 수치형 특성들
cat_attribs = ["ocean_proximity"] # 범주형 특성

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),#이름, 아까 만들었던 파이프라인을 여기에 num_attributs(수치)에 적용 
        ("cat", OneHotEncoder(), cat_attribs), # 이름, onehot 을 범주형에 적용
    ])
##각각 다른거 적용
housing_prepared = full_pipeline.fit_transform(housing)


# In[160]:


housing_prepared #우리가 원하는 최종적인 데이터


# In[162]:


housing_prepared.shape,housing.shape #변환을 한 뒤에는 feature들을 추가헀었으니까 열의 값이 16개로 늘었다


# ### 모델훈련(Train a Model)
# #### 선형회귀 모델을 사용해보자

# In[173]:


from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
lin_reg.fit(housing_prepared, housing_labels) #fit 학습완료, 이게 numpyarray로 저장


# In[174]:


len(lin_reg.coef_) #16개나옴
lin_reg.coef_


# In[175]:


# 이 개수값 16개가 크거나 작거나 이에따라 모델에 영향을 어떻게 미치는가
# 즉 개수의 크기와 모델간의 영향 확인

#numpy array는 dataset과 다르게 feature이름들이 주어지지 않아서 featurename 다시 지정
extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
cat_encoder = full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs = list(cat_encoder.categories_[0])
attributes = num_attribs + extra_attribs + cat_one_hot_attribs
sorted(zip(lin_reg.coef_, attributes), reverse=True)



# #### 왼쪽이 학습한 feature 개수값 , 오른쪽이 이름
# #### 가장 큰 개수 값을 갖는게 island 
# #### island ocean p를 1hot coding으로 만들면서 생성된 binary feature 중 하나였음
# #### 값이 1일수록 집값에 영향을 주는 요인이 될것이다
# #### 바닷가에 있을 수록 집값이 비싸질 것이다
# 
# #### 두번쨰인 소득 median_income
# #### 많이 벌수록 집값비쌈
# 
# #### 나머지들은 개수값들이 많이 적어지고(영향이 상대적으로 적다고 판단 할 수 있지만
# #### feature간 영향을 주고 받은 경우 등은 값의 크기와 상관없이 영향을 많이 줄 수 있음)
# #### 음의 값으로 가는것 존재

# In[179]:


# 몇개의 샘플에 대해 데이터 변환 및 예측을 해보자
some_data = housing.iloc[:5] #raw data
some_labels = housing_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data) #pipeline으로 변환

print("Predictions:", lin_reg.predict(some_data_prepared).round(decimals=1))#predict함수 호출
print("Labels:", list(some_labels))

# 주어진 labels값 다섯개와 predictions을 비교
# 첫번째값은 85657.9 - 721000 의 차이가 있다 등등 , 값들에 따라 차이값이 다양하게 나와있음


# ### 전체 훈련 데이터셋에 대한 RMSE를 측정해보자

# In[180]:


# mena_squared_error 함수 사용
from sklearn.metrics import mean_squared_error

housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse

#훈련 데이터 셋에 대해 대락 7만불 정도의 에러가 발생  -> 좋은 모델 아님 


# ### 훈련데이터 셋의 RMSE가 다음 경우처럼 큰 경우 -> 과소적합(under-fitting)
# ### 특성들의 불충분한 정보제공, 모델이 충분히 강력하지 못함 등의 이유로 과소적합이 발생한다
# 
# ### 강력한 비선형 모델인 DEcisionTreeRegressor 를 사용해 보자
# #### 조건을 만족하면 왼쪽 노드로 이동
# #### 이러한 트리를 만드는게 학습 과정임

# In[182]:


from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(housing_prepared, housing_labels)

housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse


# #### 선형모델의 경우 에러가 7만에 가까웠지만 비선형의 경우 에러가 0이 나옴
# ### 그러나 이 모델이 선형모델보다 낫다고 판단 할 수 있는가?
# #### 기저함수들을 사용해 복잡한 형태의 함수를 만들때, 기저함수를 너무 많이 사용하면 학습데이터의 경우 완벽 수행을 했지만
# ### 없는 부분에 대해서는 크게 반응하며 오버피팅이 발생했었음
# 
# ### 지금 상황도 오버피팅을 의심해 볼 수 있다  -> 검증필요
# 
# 
# #### 1. 테스트 데이터셋 이용(테스트 데이터에 있는 정보를 계속 들여다봐서 학습 과정에 대해 영향을 미칠 수 있음- 가능하면 모델 런칭 직전까지는 사용을 미루는게 좋음)
# #### 2. 훈련데이터셋의 일부를 검증데이터셋으로 분리해서 검증
# #### 3. k-겹 교차검증
# 
# ### 교차검증(cross-validation)을 사용한 평가
# 
# #### 학습데이터를 다섯개로 쪼개고
# #### 4개만 상용해 training 1개는(파란색) perfomance(mean square error) 를 다섯번 반복해 이 값의 평균을 에러값으로 구함
# 
# 

# In[186]:


from sklearn.model_selection import cross_val_score

scores = cross_val_score(tree_reg, housing_prepared, housing_labels,#tree_req(결정트리)모델사용,학습데이터 전달
                         scoring="neg_mean_squared_error", cv=10) #10번 반복 (겹이 10개) #에러값이 낮을수록 좋은거니까 neg 붙여줌,
tree_rmse_scores = np.sqrt(-scores) #score가 음수값이였으니까 계산위해 다시 -

def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())

display_scores(tree_rmse_scores) #10번 반복했으니까 10개의 score그리고 그값들의 평균 mean이나옴
#mean의 값이 다시 증가한 값인 7만이 나옴, 사용되지 않았던 값들에(새로운 데이터) 대해서는 높게 나옴


# ### 선형회귀 모델에 대한 평가

# In[188]:


lin_scores = cross_val_score(lin_reg, housing_prepared, housing_labels,
                             scoring="neg_mean_squared_error", cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)
display_scores(lin_rmse_scores)


# 
# #### 선형의 경우 위의 비선형을 교차검증 했을떄 7만얼마보다 작은 6만 얼마가 나옴 
# #### -> 선형모델이 새로운 데이터셋에 대해서는 비선형 결정트리 보다 더 효과적이다
# 

# ### RandomForestRegressor 에 대한 평가

# In[190]:


#트리가 여러개 있는 모델임
#트리 개수만큼 prediction 값이 있을거고 이걸 모아서 mean 해야함

from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(housing_prepared, housing_labels)

housing_predictions = forest_reg.predict(housing_prepared)
forest_mse = mean_squared_error(housing_labels, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse#학습 데이터에 대한 에러 그냥 tree 였을때 0 보다 높게 나옴


# In[192]:


from sklearn.model_selection import cross_val_score

forest_scores = cross_val_score(forest_reg, housing_prepared, housing_labels,
                                scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
display_scores(forest_rmse_scores) #이제 교차검증한 값을 구해야함


# ### 5만정도 나옴 -> linear는 6만얼마 그냥 tree는 7만 얼마 , 세개중 가장 효과적이다
# 
# #### 다음 결과를 가지고 효과적인 모델을 선택했다면 이제
# 
# ### 모델 세부튜닝(Fine_Tune your Model)을 해준다
# #### 모델 학습을 위한 최적의 하이퍼파라미터를 찾는 과정
# 
# ### 그리드 탐색(grid search)
# #### 수동으로 하이퍼파라미터 조합을 시도하는 대신 GridSearchCV를 사용하는것이 좋다

# In[197]:


from sklearn.model_selection import GridSearchCV

param_grid = [
    #n_estimators -> 트리의 개수# n_estd와 max_f 하이퍼 파라미터가 주어졌고 각각 3개4개니까 조합은 3*4
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    # then try 6 (2×3) combinations with bootstrap set as False
    #bootstrap은 하나하나 일일이 해보는 것을 말한다.
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
  ]

forest_reg = RandomForestRegressor(random_state=42)
# train across 5 folds, that's a total of (12+6)*5=90 rounds of training #12+6은 별개로 주어지기 때문,#겹까지 합쳐서 총 90번 학습진행
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,#모델설정, 파라미터조합, 몇겹
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)



# In[196]:


grid_search.best_params_ # 가장 좋은 조합찾기


# In[198]:


grid_search.best_estimator_ #그런 조합을 사용했을때 학습한 모델


# In[199]:


#전체적인 결과

cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)


# #### 위의 방법처럼 일일히 파라미터를 적어주는게 아닌
# #### 분포와 몇가지 조합을 정해주면 알아서 파리미터 조합을 만들어내는 방식
# ### RandomizedSearchCV (랜덤탐색)

# In[202]:


from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_distribs = {
        'n_estimators': randint(low=1, high=200), #1에서 200 사이의 값을 uniform하게 샘플링
        'max_features': randint(low=1, high=8),
    }

forest_reg = RandomForestRegressor(random_state=42)
rnd_search = RandomizedSearchCV(forest_reg, param_distributions=param_distribs,
                                n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=42)
rnd_search.fit(housing_prepared, housing_labels)



# In[203]:


cvres = rnd_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params) #결과 프린트


# ### 특성 중요도, 에러분석
# #### linear에선 특성 개수에 따라 중요도를 파악했는데 
# ### 제일 좋았던 모델을 가지고 그 모델에서 특성 중요도를 뽑아낼것이다

# In[206]:


feature_importances = grid_search.best_estimator_.feature_importances_

extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
#cat_encoder = cat_pipeline.named_steps["cat_encoder"] # old solution
cat_encoder = full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs = list(cat_encoder.categories_[0])
attributes = num_attribs + extra_attribs + cat_one_hot_attribs
sorted(zip(feature_importances, attributes), reverse=True)  #여기서는 median income의 중요도가 더 높게나옴


# ### 테스트 데이터셋으로 최종 평가하기

# In[207]:


#final모델에 저장한 뒤
final_model = grid_search.best_estimator_
#테스터 모델로 시험해봄

X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()

X_test_prepared = full_pipeline.transform(X_test)
final_predictions = final_model.predict(X_test_prepared)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)

final_rmse # 마지막으로 얻어진 에러값은 대략 4만7천불


# ### 결과가 마음에 든다면 론칭 ㄱ 아니면 다시 수정
# 
# ### 런칭할때 모델의 예측과 데이터 전처리가 포함된 파이프라인을 만들어 저장하는것이 좋다

# In[214]:


full_pipeline_with_predictor = Pipeline([
        ("preparation", full_pipeline),#파이프라인은 full_p, 변환
        ("linear", LinearRegression()) #선형모델쓸거 예측
    ]) #이 파이프라인을 통해 변환과 예측 한번에

full_pipeline_with_predictor.fit(housing, housing_labels)
full_pipeline_with_predictor.predict(some_data) #some_data(raw data)
#raw data 넣으면 바로 예측값 나옴


# In[216]:


my_model = full_pipeline_with_predictor


# In[217]:


#pkl파일로 만들어 상용에 배포
import joblib
joblib.dump(my_model, "my_model.pkl")
#pkl파일로 저장된걸 load로 읽어들일 수 있음
my_model_loaded = joblib.load("my_model.pkl")


# In[218]:


my_model_loaded.predict(some_data) #모델이 새로운 데이터에 잘 작동하는거 확인


# 
# ### 론칭 후 시스템 모니터링
# ##### - 시간이 지나면 모델이 낙후되면서 성능이 저하
# ##### - 자동모니터링: 추천시스템의 경우, 추천된 상품의 판매량이 줄어드는지?
# ##### - 수동모니터링: 이미지 분류의 경우, 분류된 이미지들 중 일부를 전문가에게 검토시킴
# ##### - 결과가 나빠진 경우
# ###### 1. 데이터 입력의 품질이 나빠졌는지? 센서고장?
# ###### 2. 트렌드의 변화? 계절적 요인?
# ### 유지보수
# #### - 정기적으로 새로운 데이터 수집(레이블)
# #### - 새로운 데이터를 테스트 데이터로, 현재의 테스트 데이터는 학습데이터로 편입
# #### - 다시 학습후, 새로운 테스트 데이터에 기반해 현재 모델과 새 모델을 평가, 비교
# 
# ### 전체 프로세스에 고르게 시간 배분 필요

# In[ ]:




