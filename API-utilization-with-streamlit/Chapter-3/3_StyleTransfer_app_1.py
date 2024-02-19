import streamlit as st
import cv2
import numpy as np

col1, col2 = st.columns(2)

# Input
upload_img = st.sidebar.file_uploader("画像アップロード", type=['png','jpg'])
upload_style_img = st.sidebar.file_uploader("画風画像アップロード", type=['png','jpg'])

# Process
if (upload_img is not None)&(upload_style_img is not None):

    bytes_data = upload_img.getvalue()
    tg_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), 
                            cv2.IMREAD_COLOR)
    bytes_data = upload_style_img.getvalue()
    style_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), 
                            cv2.IMREAD_COLOR)
    
    output_img = cv2.cvtColor(tg_img, cv2.COLOR_BGR2RGB)
    output_style_img = cv2.cvtColor(style_img, cv2.COLOR_BGR2RGB)

# Output
    with col1:
      st.header("対象画像")
      st.image(output_img)

    with col2:
      st.header("画風画像")
      st.image(output_style_img)