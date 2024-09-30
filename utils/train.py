import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
data_yaml = 'data.yaml'
results = model.train(data=data_yaml, epochs=3, batch_size=16, img_size=640, device="0,1")