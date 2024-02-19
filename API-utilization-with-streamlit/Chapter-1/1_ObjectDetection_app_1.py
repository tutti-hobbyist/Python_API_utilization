import streamlit as st
import cv2
import numpy as np

# Input
camera_img = st.camera_input(label='インカメラ画像')

# Process
if camera_img is not None:

  bytes_data = camera_img.getvalue()
  cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8),
                          cv2.IMREAD_COLOR)
  output_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

# Output
  st.image(output_img, caption='出力画像')