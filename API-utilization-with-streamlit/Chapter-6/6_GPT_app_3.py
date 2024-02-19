import streamlit as st
import os
import openai

os.environ["OPENAI_API_KEY"] = "＜ご自身のAPIキーを入力＞"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Input
input_area = st.text_area("ブレーンストーミングのテーマを入力してください") # 文字入力(複数行)
input_text1 = st.text_input("参加者Aの属性を入力してください") # 文字入力(1行)
input_text2 = st.text_input("参加者Bの属性を入力してください") # 文字入力(1行)
input_text3 = st.text_input("参加者Cの属性を入力してください") # 文字入力(1行)

# Process
if st.button('実行'):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "user", "content": f"""
      これから下記の＜参加者＞の3名で、＜テーマ＞でブレーンストーミングを実施してください。
      また、一人複数回発言しながらブレーンストーミングを続けてください。
      ユーザーの入力を待たずに続けてください。
      最後にブレーンストーミングの結果をまとめるようにしてください。
      ###参加者
      -参加者A：{input_text1}
      -参加者B：{input_text2}
      -参加者C：{input_text3}
      ###テーマ
      -{input_area}
      ###出力形式
      -参加者は発言の中で積極的に他者の意見にメンション（例：@〇〇さん）をつけて意見を言うようにしてください。
      -出力例：〇〇さんの提案に私は賛成/反対です。なぜなら・・
      -参加者の発言の後は、必ず改行するようにしてください。"""}  
    ]
  )

# Output
  st.write(completion["choices"][0]["message"]["content"])