import streamlit as st
import spacy
import pandas as pd

nlp = spacy.load('ja_ginza')
pos_dic = {'名詞':'NOUN', '代名詞':'PRON', 
           '固有名詞':'PROPN','動詞':'VERB'}

# Input
uploaded_file = st.file_uploader("CSVを選択", type='csv')
select_pos = st.sidebar.multiselect('品詞選択',
                ['名詞','代名詞','固有名詞','動詞'],
                ['名詞'])

# Process
if uploaded_file is not None:
  data = pd.read_csv(uploaded_file)
  tg_col = st.selectbox('対象列選択',data.columns)
  if tg_col is not None:
    data = data.dropna()
    input_text = data[tg_col]
    input_text = ' '.join(input_text)
    if st.button('実行'):
      doc = nlp(input_text)
      output_word = []
      tg_pos = [pos_dic[x] for x in select_pos]
      for token in doc:
        if token.pos_ in tg_pos:
          output_word.append(token.lemma_)
      output_df = pd.DataFrame({'Word':output_word})
      output_df = output_df.groupby('Word',as_index=False).size()
      output_df.sort_values('size',ascending=False,inplace=True)
      output_df.set_index('Word', inplace=True)

# Output
      st.dataframe(data)
      st.bar_chart(output_df.head(10))