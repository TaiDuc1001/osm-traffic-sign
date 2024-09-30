import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ultralytics import YOLO
import xml.etree.ElementTree as ET
import logging
from datetime import datetime
import json

def get_location(image):
    meta_prefix = 'data/inference/meta/'
    meta_file = os.path.join(meta_prefix, f'{os.path.splitext(os.path.basename(image))[0]}.xml')
    tree = ET.parse(meta_file)
    root = tree.getroot()
    gps = root.find('gps')
    lat = float(gps.find('latitude').text)
    lon = float(gps.find('longitude').text)
    return lat, lon

def write_json(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f)

def write_to_log(message):
    with open('changeset.log', 'a') as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {message}\n')

def main():
    logging.basicConfig(filename='changeset.log', level=logging.INFO, 
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    model = YOLO('yolov8n.pt')
    image_prefix = 'data/inference/images/'
    images = [os.path.join(image_prefix, f) for f in os.listdir(image_prefix) if f.endswith(('png', 'jpg', 'jpeg'))]
    results = model.predict(images)
    id2name = {
        '0': 'person',
        '1': 'bicycle',
    }
    data = []
    for image, result in zip(images, results):
        img_cls_id = result.boxes.cls
        img_cls_name = id2name[str(img_cls_id)]
        lat, lon = get_location(image)
        comment = f"{img_cls_name} sign at {lat}, {lon}"
        write_to_log(comment)
        data.append({'image': image, 'sign_type': img_cls_name, 'lat': lat, 'lon': lon})
    write_json('data.json', data)