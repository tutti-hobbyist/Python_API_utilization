import streamlit as st
import cv2
import numpy as np
import torch
from PIL import Image

model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2")
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint")

# Input
upload_img = st.sidebar.file_uploader("画像アップロード", type=['png','jpg'])

# Process
if upload_img is not None:

    bytes_data = upload_img.getvalue()
    tg_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), 
                            cv2.IMREAD_COLOR)
    tg_img = cv2.cvtColor(tg_img, cv2.COLOR_BGR2RGB)
    tg_img = Image.fromarray(tg_img)
    output_img = face2paint(model, tg_img, size=512)

# Output
    st.title("変換結果")
    st.image(output_img)
