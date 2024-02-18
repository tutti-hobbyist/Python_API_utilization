import streamlit as st

# Input
input_text = st.text_input('文章入力')

# Process
if st.button('実行'):

# Output
  st.write('入力した文章：', input_text)
