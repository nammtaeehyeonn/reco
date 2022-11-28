import streamlit as st
import numpy as np
import pandas as pd


def Recommend(title, cos_sim):
    
    title_idx = dict(zip(df['Title'], df.index))
    # 도서 제목 입력하면 인덱스를 리턴
    idx = title_idx[title]

    # 도서 줄거리 유사도 전부 가져오기
    sim = list(enumerate(cos_sim[idx]))

    # 유사도에 따라 정렬하기
    sim = sorted(sim, key=lambda x: x[1], reverse=True)

    # 유사도 탐5 가져오기
    sim = sim[1:6]

    # 유사도 탑5 인덱스 가져오기
    rec_idx = [idx[0] for idx in sim]

    # 유사도 탑10 제목 가져오기
    # print(sim)                       # (인덱스, 유사도)
    return df.iloc[rec_idx]

df = pd.read_csv('book.csv')
cos_sim = np.load('sim.npy')

############################################ streamlit
st.title('book')

title = st.text_input("책 제목을 입력해주세요")


if title:
    ans = Recommend(title, cos_sim)
    ans.reset_index(drop = True, inplace = True)
    
    col1, col2 = st.columns(2)
    
    with col1:
    st.header(ans.Title[0])
    st.image(ans.image[0], width = 100)
    
    with col2:
    st.header(ans.Title[1])
    st.image(ans.image[1], width = 100)
    
    col1, col2 = st.columns(2)
    
    with col1:
    st.header(ans.Title[0])
    st.image(ans.image[0], width = 100)
    
    with col2:
    st.header(ans.Title[1])
    st.image(ans.image[1], width = 100)
    
#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         st.header('')
#         st.image(urls[0], width = 100)

#     with col2:
#         st.header('')
#         st.image(urls[1], width = 100)

#     with col3:
#         st.header('')
#         st.image(urls[2], width = 100)

#     with col4:
#         st.header('')
#         st.image(urls[3], width = 100)

#     with col5:
#         st.header('')
#         st.image(urls[4], width = 100)
    
   
# ###########################################





# # title = df.loc[df['Title'].str.contains(title), 'Title']
# # print(title)

