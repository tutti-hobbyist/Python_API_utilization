import streamlit as st

st.title('計算アプリ')

# Input
a = st.number_input('数字１')
b = st.number_input('数字２')
method = st.sidebar.selectbox( "計算方法",['足し算','掛け算'])

# Process
if method == '足し算':
    c = a + b
elif method == '掛け算':
    c = a * b

# Output
st.title(f'{method}結果')
st.text(c)