import streamlit as st
import spacy

nlp = spacy.load('ja_ginza')
col1, col2 = st.columns(2)

# Input
with col1:
  input_text1 = st.text_input('文章１')
with col2:
  input_text2 = st.text_input('文章２')

# Process
if st.button('実行'):
  doc1 = nlp(input_text1)
  doc2 = nlp(input_text2)
  similarity = doc1.similarity(doc2)

# Output
  st.write(f'類似度：{round(similarity, 2)}')