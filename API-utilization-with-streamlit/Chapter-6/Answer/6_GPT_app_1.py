import streamlit as st
import os
import openai

os.environ["OPENAI_API_KEY"] = "＜ご自身のAPIキーを入力＞"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Input
input_text = st.text_input('指示入力')

# Process
if st.button('実行'):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "system", "content": "あなたはプロのプログラマーです。"},
      {"role": "user", "content": input_text}
  ]
  )

# Output
  st.write(completion["choices"][0]["message"]["content"])
