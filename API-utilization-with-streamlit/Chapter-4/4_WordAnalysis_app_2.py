import streamlit as st
import spacy

nlp = spacy.load('ja_ginza')

# Input
input_text = st.text_input('文章入力')

# Process
if st.button('実行'):
  doc = nlp(input_text)
  output_word = []
  for token in doc:
    output_word.append(token)

# Output
  st.write('入力した文章：', input_text)
  st.write(output_word)
  