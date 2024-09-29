import os
import argparse
import json

def get_access_token(use_dev_api: bool) -> str:
    command = f'''
        python utils/get_access_token.py
    '''
    if use_dev_api:
        command += ' --use-dev-api'
    return command

def upload(lat: float, lon:float, name: str, use_dev_api: bool) -> str:
    command = f'''
        python utils/upload.py --lat {lat} --lon {lon} --name {name}
    '''
    if use_dev_api:
        command += ' --use-dev-api'
    return command

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--use-dev-api', action='store_true', help='Use the development API')
    parser.add_argument('--data-json', type=str, required=True, help='Path to the JSON file containing the data')
    return parser.parse_args()

def get_data_from_json(data_json):
    with open(data_json, 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    args = parse_args()
    os.system(get_access_token(args.use_dev_api))
    data = get_data_from_json(args.data_json)
    for item in data:
        lat = item.get('lat')
        lon = item.get('lon')
        name = item.get('name')
        os.system(upload(lat, lon, name))