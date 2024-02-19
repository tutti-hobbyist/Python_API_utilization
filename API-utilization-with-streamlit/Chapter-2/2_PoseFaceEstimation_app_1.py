import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from io import BytesIO, BufferedReader

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(static_image_mode=True,
min_detection_confidence=0.5, model_complexity=2)

# Input
upload_img = st.file_uploader("画像アップロード", type=['png','jpg'])

# Process
if upload_img is not None:

    bytes_data = upload_img.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8),
    cv2.IMREAD_COLOR)
    img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    output_img = img.copy()
    mp_drawing.draw_landmarks(output_img,results.pose_landmarks,
                              mp_pose.POSE_CONNECTIONS,)

    ret, enco_img = cv2.imencode(".png",
                                 cv2.cvtColor(output_img,cv2.COLOR_BGR2RGB))
    BytesIO_img = BytesIO(enco_img.tostring())
    BufferedReader_img = BufferedReader(BytesIO_img)

# Output
    st.image(output_img, caption='出力画像')
    st.download_button(label='ダウンロード',data=BufferedReader_img,
                       file_name="output.png",mime="image/png")