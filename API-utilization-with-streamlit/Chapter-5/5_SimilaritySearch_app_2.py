import streamlit as st
import spacy
import pandas as pd

nlp = spacy.load('ja_ginza')

# Input
input_text = st.text_input('検索')
uploaded_file = st.file_uploader("CSVを選択", type='csv')

# Process
if uploaded_file is not None:
  tg_data = pd.read_csv(uploaded_file)
  tg_col = st.selectbox('対象列選択',tg_data.columns)
  if tg_col is not None:
    if st.button('実行'):
      tg_data = tg_data.dropna()
      tg_data.reset_index(drop=True, inplace=True)
      tg_data['similarity'] = 0
      doc1 = nlp(input_text)
      for i in range(len(tg_data)):
        doc2 = nlp(tg_data[tg_col][i])
        similarity = doc1.similarity(doc2)
        tg_data['similarity'][i] = similarity
      tg_data.sort_values('similarity',ascending=False,inplace=True)
      tg_data.set_index(tg_col, inplace=True)

# Output
      st.dataframe(tg_data[['similarity']])
