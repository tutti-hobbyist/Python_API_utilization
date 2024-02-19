import streamlit as st
import spacy

nlp = spacy.load('ja_ginza')
pos_dic = {'名詞':'NOUN', '代名詞':'PRON', 
           '固有名詞':'PROPN','動詞':'VERB'}

# Input
input_text = st.text_input('文章入力')
select_pos = st.sidebar.multiselect('品詞選択',
                ['名詞','代名詞','固有名詞','動詞'],
                ['名詞'])

# Process
if st.button('実行'):
  doc = nlp(input_text)
  output_word = []
  tg_pos = [pos_dic[x] for x in select_pos]
  for token in doc:
    if token.pos_ in tg_pos:
      output_word.append(token.lemma_)

# Output
  st.write('入力した文章：', input_text)
  st.write(output_word)