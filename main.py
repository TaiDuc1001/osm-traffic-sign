import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
import argparse
import json
import subprocess

def get_access_token(use_dev_api: bool) -> str:
    command = ['python', 'utils/get_access_token.py']
    if use_dev_api:
        command.append('--use-dev-api')
    return command

def upload(lat: float, lon:float, sign_type: str, use_dev_api: bool, speed_limit: int = None) -> str:
    command = ['python', 'utils/upload.py']
    command.extend(['--lat', str(lat)])
    command.extend(['--lon', str(lon)])
    command.extend(['--sign-type', sign_type])
    if speed_limit:
        command.extend(['--speed-limit', str(speed_limit)])
    if use_dev_api:
        command.append('--use-dev-api')
    print(command)
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
    subprocess.run(get_access_token(args.use_dev_api))
    data = get_data_from_json(args.data_json)
    for item in data:
        lat = item.get('lat')
        lon = item.get('lon')
        sign_type = item.get('sign_type')
        speed_limit = item.get('speed_limit', None)
        subprocess.run(
            upload(
                lat=lat, 
                lon=lon, 
                sign_type=sign_type, 
                use_dev_api=args.use_dev_api, 
                speed_limit=speed_limit
            )
        )