import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("streamlit 超入門")

st.write("プログレスバーの表示")


"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

"Done"""











left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字表示")


if button:
    right_column.write("右カラム")



expander = st.expander("エラー処理")

expander.write("頑張ってください")
img=Image.open("main_image_star-forming_region_carina_nircam_final-5mb.jpg")
expander.image(img,caption="pic",use_column_width=True)


expander2 = st.expander("問い合わせ1")

expander2.write("問い合わせ1内容を書く")



option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
    )

"あなたが好きな数字は",option,"です"



text = st.text_input("趣味は？")

"あなたの趣味：",text



condition = st.slider("あなたの今の調子は？",0,100,50)

"コンディション：",condition


img=Image.open("main_image_star-forming_region_carina_nircam_final-5mb.jpg")
st.image(img,caption="pic",use_column_width=True)


df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.7],
    columns=["lat","lon"]
    )

if st.checkbox("show map"):
    st.map(df)
    






#st.dataframe(df)



