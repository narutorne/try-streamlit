import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('streamlit 超入門')

#st.write('progress bar')
#'Start!'
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
#    latest_iteration.text(f'Iteration {i+1}')
#    bar.progress(i+1)
#    time.sleep(0.01)
    
#'Done!'
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')
    
expander = st.expander('expander')
expander.write('hello')

a = 100
expander.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, a, 300, 40]
})        

#st.write(df)

# st.writeではなく、st.dataframeでもデータフレームを出力できる
# st.dataframeにはデータフレームのオプションを指定できる
expander.dataframe(df.style.highlight_max(axis=0))

# st.table静的な表をつくりたいとき
#st.table(df.style.highlight_max(axis=0))


# マジックコマンド

#"""
# 章
## 節
### 項
#```
#import streamlit as st
#import numpy as np
#import pandas as pd
#```



# チャートを描く
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

expander.line_chart(df)
expander.area_chart(df)
expander.bar_chart(df)

if st.sidebar.checkbox('Show Image'):
    img = Image.open('nature.jpg')
    st.image(img, caption='Nice Nature', use_column_width=True)

option = st.sidebar.selectbox(
    'あなたの好きな数字を選んでください',
    list(range(1,10))
)
'あなたの好きな数字は', option, 'です。'

st.write('Interactive Widgets')
option2 = st.sidebar.text_input('あなたの好きなウマ娘を教えてください。')
'あなたの好きなウマ娘：', option2

# スライダー（最小値、最大値、デフォルト値）
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition





