import streamlit as st


st.markdown("<h1 style='text-align: center; color: #008080;'>사용자 정보 기반 메뉴 추천</h1>", unsafe_allow_html=True)

st.markdown("#### 안녕하세요, 팀25의 '오늘 뭐먹지'입니다.\
            <br>사용자 정보를 기반으로 메뉴를 추천해드립니다!", unsafe_allow_html=True)

reason=st.selectbox(
    '음식을 선택하는 이유를 선택해주세요',
    ('스트레스','지루함','우울함','배고픔','게으름','날씨','행복','여가생활','해당없음')
    )
    
fav=st.selectbox(
    '좋아하는 음식 종류를 선택해주세요',
    ('이탈리안/양식','아시안','중국음식','패스트푸드','한식','베이커리/스낵류','건강식','일식')
    )

fruit=st.selectbox(
    '과일 섭취량을 선택해주세요',
    ('전혀섭취하지않는다','섭취하지않는다','보통이다','섭취한다','많이섭취한다')
    )
pay=st.selectbox(
    '음식에 지불하는/지불할 비용을 선택해주세요',
    ('5천원미만','5천원~1만원','1만원~2만원','2만원~3만원','3만원~4만원','4만원이상')
    )   
veggies=st.selectbox(
    '야채 섭취량을 선택해주세요',
    ('전혀섭취하지않는다','섭취하지않는다','보통이다','섭취한다','많이섭취한다')
)

st.write('선택하신 결과 :',reason,'/',fav,'/',fruit,'/',pay,'/',veggies)

import pandas as pd
import numpy as np

data=pd.read_csv('food1119.csv')
data.columns=['number',
              'reasons',
              'cuisine',
              'fruit',
              'pay',
              'veggies',
             'result']
data2=data[['reasons','cuisine','fruit','pay','veggies','result']]
df=data[['reasons','cuisine','fruit','pay','veggies']]
a=np.array([])
if reason=="스트레스":
    a=np.append(a,1)
    a=a.astype(int)
elif reason=="지루함":
    a=np.append(a,2)
    a=a.astype(int)
elif reason=="우울함":
    a=np.append(a,3)
    a=a.astype(int)
elif reason=="배고픔":
    a=np.append(a,4)
    a=a.astype(int)
elif reason=="게으름":
    a=np.append(a,5)
    a=a.astype(int)
elif reason=="날씨":
    a=np.append(a,6)
    a=a.astype(int)
elif reason=="행복":
    a=np.append(a,7)
    a=a.astype(int)
elif reason=="여가생활":
    a=np.append(a,8)
    a=a.astype(int)
elif reason=="해당없음":
    a=np.append(a,9)
    a=a.astype(int) 

if fav=="이탈리안/양식":
    a=np.append(a,1)
    a=a.astype(int)
elif fav=="아시안":
    a=np.append(a,2)
    a=a.astype(int)
elif fav=="중국음식":
    a=np.append(a,3)
    a=a.astype(int)
elif fav=="패스트푸드":
    a=np.append(a,4)
    a=a.astype(int)
elif fav=="한식":
    a=np.append(a,5)
    a=a.astype(int)
elif fav=="베이커리/스낵류":
    a=np.append(a,6)
    a=a.astype(int)
elif fav=="건강식":
    a=np.append(a,7)
    a=a.astype(int)
elif fav=="일식":
    a=np.append(a,8)
    a=a.astype(int)

if fruit=="전혀섭취하지않는다":
    a=np.append(a,1)
    a=a.astype(int)
elif fruit=="섭취하지않는다":
    a=np.append(a,2)
    a=a.astype(int)
elif fruit=="보통이다":
    a=np.append(a,3)
    a=a.astype(int)
elif fruit=="섭취한다":
    a=np.append(a,4)
    a=a.astype(int)
elif fruit=="많이섭취한다":
    a=np.append(a,5)
    a=a.astype(int)

if pay=="5천원미만":
    a=np.append(a,1)
    a=a.astype(int)
elif pay=="5천원~1만원":
    a=np.append(a,2)
    a=a.astype(int)
elif pay=="1만원~2만원":
    a=np.append(a,3)
    a=a.astype(int)
elif pay=="2만원~3만원":
    a=np.append(a,4)
    a=a.astype(int)
elif pay=="3만원~4만원":
    a=np.append(a,5)
    a=a.astype(int)
elif pay=="4만원이상":
    a=np.append(a,6)
    a=a.astype(int)

if veggies=="전혀섭취하지않는다":
    a=np.append(a,1)
    a=a.astype(int)
elif veggies=="섭취하지않는다":
    a=np.append(a,2)
    a=a.astype(int)
elif veggies=="보통이다":
    a=np.append(a,3)
    a=a.astype(int)
elif veggies=="섭취한다":
    a=np.append(a,4)
    a=a.astype(int)
elif veggies=="많이섭취한다":
    a=np.append(a,5)
    a=a.astype(int)

user_similarity_scores=df.dot(a) / (np.linalg.norm(df,axis=1)*np.linalg.norm(a))
best_similarity=user_similarity_scores.idxmax()
result=data2.iloc[best_similarity]['result']
st.markdown("<h1 style='text-align: center; color: #808000;'>-----------------</h1>", unsafe_allow_html=True)
st.markdown("##### 오늘의 추천메뉴는 \'{}\'입니다.".format(result))

 
     



