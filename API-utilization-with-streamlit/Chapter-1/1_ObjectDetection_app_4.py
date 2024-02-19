import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import pandas as pd

# モデルの読み込み
model = YOLO('yolov8n.pt') 

# Input
upload_file = st.file_uploader("動画アップロード", type='mp4')

# Process
if upload_file is not None:

    temp_file = tempfile.NamedTemporaryFile(delete=False) 
    temp_file.write(upload_file.read())

    cap = cv2.VideoCapture(temp_file.name)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    writer = cv2.VideoWriter('./data/output/object_detection_app_results.mp4',
                              cv2.VideoWriter_fourcc(*'MP4V',),fps,
                              frameSize=(int(width),int(height)))
    num = 0
    nums = []
    persons = []
    while cap.isOpened():
      if num > count :break
      ret, img = cap.read()

      if ret:
        results = model(img,conf=0.5,classes=[0])
        img = results[0].plot(labels=False,conf=True)
        categories = results[0].boxes.cls
        person_num = len(categories)
        writer.write(img) 
      nums.append(num)
      persons.append(person_num)
      num = num + 1
    cap.release()
    writer.release()

    person_data = pd.DataFrame({'frame':nums, 'count':persons})
    person_data['sec'] = person_data['frame'] / fps
    person_data = person_data[['sec','count']]

# Output
    st.line_chart(person_data,x="sec",y="count")
    st.dataframe(person_data)