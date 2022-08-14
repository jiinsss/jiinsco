#!/usr/bin/env python
# coding: utf-8

# In[350]:


import sys
assert sys.version_info >=(3,5)

import sklearn
assert sklearn.__version__>="0.20"

import numpy as np
import os

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize =14)
mpl.rc('xtick', labelsize =12)
mpl.rc('ytick', labelsize =12)

#그린거 저장 
project_root_dir ="."
chapter_id ="medical_cost"
images_path= os.path.join(project_root_dir,"images",chapter_id)
os.makedirs(images_path, exist_ok =True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path=os.path.join(images_path, fig_id + "."+ fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    
import warnings
warnings.filterwarnings(action="ignore" , message="^internal gelsd")


# In[351]:


#데이터 호출

import os
import tarfile
import urllib

MEDICAL_PATH=os.path.join("datasets","medical")
def fetch_medical_data(medical_path =MEDICAL_PATH):
    if not os.path.isdir(medical_path):
        os.makedirs(medical_path)
        #!kaggle datasets download -d mirichoi0218/insurance
        get_ipython().system('unzip -uq "./datasets/medical/insurance.zip" -d "./datasets/medical"')
    


# In[352]:


fetch_medical_data()


# In[353]:


import pandas as pd
medical=pd.read_csv('./datasets/medical/insurance.csv')


# ### 의료비용을 예측하는 모델을 만들어 보자
# 
# #### 비용이 이산값이 아닌 연속값-> 회귀 -> 평균제곱근을 오차로 선택
# #### 지속적 업데이트가 아님 -> 배치학습
# 
# 

# In[354]:


medical


# In[355]:


medical.info() # 결측치 없음 #범주형필드 sex,smoker,region,


# In[356]:


medical["region"].value_counts()


# In[357]:


medical["sex"].value_counts()


# In[358]:


medical["smoker"].value_counts()


# In[359]:


medical.describe() #숫자형 필드


# In[360]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
medical.hist(bins=50,figsize=(20,15))
save_fig("attribute_histo")
plt.show


# In[361]:


#age 중간에 빈 값들 존재 20대 경계값에 다량 분포(경계값 분할 때문일 수 있음)
#의료비용이 하향분포 되어있음


# ### 테스트 데이터셋 만들기
# #### 충분할 땐 20% 많이없으면 하나의 데이터셋을 훈련과 테스트용으로 분리
# 
# #### scikit -learn에서 기본적으로 제공되는 데이터 분할 함수 사용

# In[362]:


from sklearn.model_selection import train_test_split

train_set, test_set =train_test_split(medical, test_size =0.2, random_state=42)


# In[363]:


len(train_set)


# In[364]:


#테스트 데이터가 전체 비율의 특성을 잘 보여줘야 함
#모든 속성을 샘플링 하기는 힘들고 목표값인 charge를 제외하고
#이 목표값과 가장 연관이 있을 거 같은 데이터들을 가지고 테스트 해봄

#bmi와 medical cost의 양상은 비슷할 것이다
medical["bmi"].hist()


# In[365]:


#연속적인 값은 계층적 샘플링을 하기 어려워서 그룹으로 카테고리화 시켜줌
#판다스 cut 사용

medical["bmi_cat"] = pd.cut(medical["bmi"],bins=[10.,20.,30.,40., 50.,np.inf],labels=[1,2,3,4,5])

medical["bmi_cat"].value_counts()


# In[366]:


medical["bmi_cat"].hist()


# In[367]:


#sklearn을 사용해 계층적 샘플링

from sklearn.model_selection import StratifiedShuffleSplit

split=StratifiedShuffleSplit(n_splits=1,test_size=0.2, random_state=20)

for train_index, test_index in split.split(medical, medical["bmi_cat"]):
    strat_train_set = medical.loc[train_index]
    strat_test_set=medical.loc[test_index]
    
strat_train_set.info() #1070 - 80%


# In[368]:


strat_test_set.info() # 268 -20%


# #### 분할해준 bmi_cat이 테스트 데이터에서도 분포를 유지하고 있는지 확인

# In[369]:


#비율을 보기 위해 전체 데이터 개수로 나눠줌( 전체 값에서의 비율 )

medical["bmi_cat"].value_counts()/len(medical)


# In[370]:


strat_test_set["bmi_cat"].value_counts()/len(strat_test_set) #분포 유지


# #### 테스트 데이터셋에 대한 검증이 끝났으니까 
# #### train데이터와 test데이터의 이해를 위한 탐색과 시각화 진행
# 
# #### bmi cat 삭제하고 원본 데이터 손상 방지를 위해 copy() 로 복사본을 만든다

# In[371]:


for set_ in (strat_train_set, strat_test_set):
    set_.drop("bmi_cat", axis=1, inplace=True)


# In[372]:


medical=strat_train_set.copy() #이제 medical은 train 데이터 카피한거임


# In[373]:


medical


# ### 지역별 데이터 시각화 - train data (흡연과 bmi에 따른 cost 지역별 분포)

# In[374]:


medical["region"].value_counts()


# In[375]:


medical_with_region_axis=medical.copy()
region_x=[]
region_y=[]
smoker_is=[]
for row in medical['region']:
    if row == 'southeast':
        region_x.append(1)
        region_y.append(-1)
    if row == 'northwest':
        region_x.append(-1)
        region_y.append(1)
    if row == 'southwest':
        region_x.append(-1)
        region_y.append(-1)
    if row == 'northeast':
        region_x.append(1)
        region_y.append(1)
for row in medical['smoker']:
    if row == 'yes':
        smoker_is.append(1)
    else:
        smoker_is.append(0)
            
medical_with_region_axis['region_x']=region_x
medical_with_region_axis['region_y']=region_y
medical_with_region_axis['smoker_is']=smoker_is
medical_with_region_axis


# In[376]:


medical_with_region_axis.plot(kind="scatter", x='region_x', y='region_y',alpha=0.5,
                             s=medical_with_region_axis["charges"]/1.5,
                              c="smoker_is",cmap=plt.get_cmap("jet"), colorbar=True
                             )
plt.legend()
plt.title("regional cost & smoke")
plt.ylabel("south & north ", fontsize=14)
plt.xlabel("west & east", fontsize =14)
save_fig("regional cost & smoke")


# In[377]:


medical_with_region_axis.plot(kind="scatter", x='region_x', y='region_y',alpha=0.5,
                             s=medical_with_region_axis["charges"]/1.5,

                              c="bmi",cmap=plt.get_cmap("jet"), colorbar=True
                             )
plt.legend()
plt.ylabel("south & north ", fontsize=14)
plt.xlabel("west & east", fontsize =14)
plt.title("regional cost & bmi")
save_fig("regional cost & bmi")


# In[378]:


#!pip install seaborn
import seaborn as sns

medical_sex = medical.copy()
msb= medical_sex[['sex','charges']].groupby('sex').mean()
msb.plot.bar()
plt.legend()
plt.title("sex & charges")  
#남성이 조금 높다
save_fig("sex & charges")


# In[ ]:





# ### 상관관계 관찰
# 
# #### 위 그래프를 관찰한 결과 지역별 금액과 smoke 사이에 높은 관계성이 예측되었다
# #### 상관관계는 수치형 데이터에서 가능하니까
# #### 흡연 여부를 0과 1로 바꿔서 상관관계를 관찰해 봤다

# In[379]:


smoker_is =[]

for row in medical['smoker']:
    if row == 'yes':
        smoker_is.append(1)
    else:
        smoker_is.append(0)
        
medical["smoker"]=smoker_is
corr_matrix = medical.corr()
corr_matrix["charges"].sort_values(ascending=False) #smoker가 상대적으로 높은 상관관계를 갖는다


# In[380]:


# medical cost인 charges와 연관이 있을것 같은 속성들에 대해 상관관계를 관찰해 보자

from pandas.plotting import scatter_matrix
attributes=["charges","smoker","age","bmi","children"]

scatter_matrix(medical[attributes],figsize=(12,8))
save_fig("scatter_matrix_plot")


# In[381]:


#smoker 
#bmi와 charge 비교적 선형
#age와 charge 비교적 선형
# 조합 X


# ### 데이터 정제
# 
# #### 1. 결측치 예측: imputer, linear regression, fit()
# #### 2. 구한 값들을 결측치에 넣음: imputer, transform()
# #### 3. 새로운 데이터 셋에대한 예측값 생성 : linear regression
# 

# In[382]:


medical.info() #-> 결측치 없음  변환기 필요 없음(결측값을 처리할)
#그러나 sex의 경우 object 형태라 변환 필요


# In[383]:


#목표값인 charges value를 떼고 저장
medical_= medical.drop("charges",axis=1)
medical_labels=medical['charges'].copy()

medical_num =medical_.drop("sex",axis=1)
medical_num= medical_num.drop("region",axis=1)


# In[384]:


medical_num


# In[385]:


from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

num_pipeline=Pipeline([
    ('imputer',SimpleImputer(strategy="median")),
  #  ('attribs_adder',CombinedAttributesAdder()),조합으로 만든 속성이 없어서 하이퍼 파라미터 없음
    ('std_scaler',StandardScaler()),
])


# In[386]:


from sklearn.compose import ColumnTransformer

num_attribs=list(medical_num)
cat_attribs=["sex","region"]

full_pipeline =ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat",OneHotEncoder(), cat_attribs),
    
])

medical_prepared=full_pipeline.fit_transform(medical)


# In[387]:


medical_prepared


# ### 모델훈련
# 
# #### 선형, 비선형, randomForestRegression의 RMSE검증
# 

# #### 선형모델

# In[388]:


#선형모델



from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
lin_reg.fit(medical_prepared,medical_labels)


# In[389]:


len(lin_reg.coef_)
lin_reg.coef_


# In[390]:


cat_encoder=full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs=list(cat_encoder.categories_[0])+list(cat_encoder.categories_[1])
attributes=num_attribs + cat_one_hot_attribs
sorted(zip(lin_reg.coef_,attributes),reverse=True)


# In[391]:


#smoker age bmi 순으로 featire 개수값이 가장 큼


# In[392]:


#RMSE 측정
from sklearn.metrics import mean_squared_error

medical_predictions= lin_reg.predict(medical_prepared)
lin_mse= mean_squared_error(medical_labels, medical_predictions)
lin_rmse=np.sqrt(lin_mse)
lin_rmse


# #### 비선형 모델인 DecisionTreeRegression 

# In[393]:


#RMSE 측정
from sklearn.tree import DecisionTreeRegressor

tree_reg=DecisionTreeRegressor(random_state=42)
tree_reg.fit(medical_prepared, medical_labels)

medical_predictions= tree_reg.predict(medical_prepared)
tree_mse=mean_squared_error(medical_labels, medical_predictions)
tree_rmse=np.sqrt(tree_mse)
tree_mse


# #### 선형 6011 비선형 73028  선형이 더 유리

# #### 오버피팅이 예상되지는 않지만 일단 교차검증

# In[394]:


# 비선형 모델

from sklearn.model_selection import cross_val_score

scores=cross_val_score(tree_reg,medical_prepared, medical_labels,
                      scoring="neg_mean_squared_error",cv=10 #10번반복
                      )
tree_rmse_scores = np.sqrt(-scores)

def display_scores(scores):
    print("scores :", scores)
    print("Mean :" ,scores.mean())
    print("Standard deviation: " ,scores.std())
display_scores(tree_rmse_scores) #6422


# In[395]:


# 선형모델

lin_scores=cross_val_score(lin_reg,medical_prepared,medical_labels,
                          scoring="neg_mean_squared_error",cv=10)
lin_rmse_scores=np.sqrt(-lin_scores)
display_scores(lin_rmse_scores) #6039


# #### 비선형모델 6422 선형모델 6039로 선형이 더 유리

# #### + 또 다른 비선형 모델인 RandomForestRegressor 

# In[396]:


from sklearn.ensemble import RandomForestRegressor

forest_reg= RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(medical_prepared, medical_labels)

medical_predictions =forest_reg.predict(medical_prepared)
forest_mse= mean_squared_error(medical_labels,medical_predictions)
forest_rmse=np.sqrt(forest_mse)
forest_rmse #1805


# #### 선형 6011 비선형 73028 비선형 randomForestRegressor 1805 에러로
# ### 비선형 RandomForestRegressor 모델이 가장 적합함
# 
# #### 모델 세부 튜닝을 해줘야 하는데 하이퍼 파라미터 조합을 할 게 없음
# 

# In[397]:


# 런칭할 때 모델의 예측과 데이터 전처리가 포함된 파이프 라인을 만들어 저장하는게 좋다
full_pipeline_with_predictor =Pipeline([
    ("preperation",full_pipeline),
    ("linear", LinearRegression())
])

full_pipeline_with_predictor.fit(medical,medical_labels)


# In[ ]:





# In[401]:


#raw 데이터 넣어서 예측값 바로 나오는지 확인
some_data=medical_.iloc[:3]
full_pipeline_with_predictor.predict(some_data) #4번째 값이 -값이 나옴 -> 오류?


# In[402]:


my_model= full_pipeline_with_predictor


# In[403]:


#pkl 파일로 만들어 상용에 배포
import joblib
joblib.dump(my_model,"my_model2.pkl")
my_model_loaded=joblib.load("my_model2.pkl")


# In[404]:


#모델이 새로운 데이터에 잘 작동하는지 확인
my_model_loaded.predict(some_data) 


# In[ ]:




