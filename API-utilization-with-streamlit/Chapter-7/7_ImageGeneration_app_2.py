import streamlit as st
import os
import openai
import base64
from PIL import Image
from io import BytesIO, BufferedReader

os.environ["OPENAI_API_KEY"] = "＜ご自身のAPIキーを入力＞"
openai.api_key = os.getenv("OPENAI_API_KEY")


# Input
input_text = st.text_input('指示入力')
create_num = st.sidebar.number_input('生成枚数',value=1,step=1)

# Process
if st.button('実行'):
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0,
  messages=[
    {"role": "system", "content": "あなたはプロの翻訳家です。次の（文章）を英語に翻訳してください。"},
    {"role": "user", "content": f'{input_text}'}
    ]
  )
  eng_prompt = completion["choices"][0]["message"]["content"]

  image = openai.Image.create(
    prompt=eng_prompt,
    size="256x256",
    n=create_num,
    response_format="b64_json"
  )

# Output
  uq_num = 1
  for data in image["data"]:
    img = base64.b64decode(data["b64_json"])
    byte_img = BytesIO(img)
    img = Image.open(byte_img)
    st.image(img)
    
    BufferedReader_img = BufferedReader(byte_img)
    st.download_button(label='ダウンロード',data=BufferedReader_img,
                       file_name="output.png",mime="image/png",key=uq_num)
    uq_num += 1
