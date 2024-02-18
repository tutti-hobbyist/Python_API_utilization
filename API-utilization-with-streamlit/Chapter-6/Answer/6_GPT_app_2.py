import streamlit as st
import os
import openai

os.environ["OPENAI_API_KEY"] = "＜ご自身のAPIキーを入力＞"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Input
input_text = st.text_input('メールのシーン入力')

# Process
if st.button('実行'):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "user", "content": f'{input_text}メールの文案を200文字くらいで作成して'}
  ]
  )

# Output
  st.write(completion["choices"][0]["message"]["content"])
