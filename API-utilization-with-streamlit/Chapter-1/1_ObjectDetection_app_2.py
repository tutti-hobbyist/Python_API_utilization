import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# モデルの読み込み
model = YOLO('yolov8n-seg.pt') 

# Input
camera_img = st.camera_input(label='インカメラ画像')

# Process
if camera_img is not None:

    bytes_data = camera_img.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), 
                            cv2.IMREAD_COLOR)
    results = model(cv2_img,conf=0.5)
    output_img = results[0].plot(labels=True,conf=True)
    output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
# Output
    st.image(output_img, caption='出力画像')