import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import argparse
from utils import create_changeset, create_node, close_changeset, \
                    gen_comment

TRAFFIC_SIGNS = {
    'stop': 'stop',
    'yield': 'give_way',
    'speed_limit': 'maxspeed',
    'no_entry': 'no_entry',
    'one_way': 'oneway',
    'no_parking': 'no_parking',
    'crosswalk': 'crossing',
    'traffic_light': 'traffic_signals'
}

def main(**kwargs):
    headers = kwargs.get('headers', None)
    api_endpoint = kwargs.get('api_endpoint', None)
    lat = kwargs.get('lat', None)
    lon = kwargs.get('lon', None)
    sign_type :str = kwargs.get('sign_type', None)
    comment = gen_comment(type=f'Traffic Sign: {sign_type.capitalize()}', lat=float(lat), lon=float(lon))

    try:
        changeset_id = create_changeset(
            comment=comment, 
            api_endpoint=api_endpoint, 
            headers=headers
        )
        print(f"Changeset created with ID: {changeset_id}")

        tags = {
            'highway': 'traffic_sign',
            'traffic_sign': TRAFFIC_SIGNS.get(sign_type, 'unknown')
        }

        if sign_type == 'speed_limit':
            tags['maxspeed'] = kwargs.get('speed_limit', '50')
        elif sign_type == 'one_way':
            tags['oneway'] = 'yes'

        node_id = create_node(
            changeset_id=changeset_id, 
            lat=lat, lon=lon, tags=tags, 
            api_endpoint=api_endpoint, 
            headers=headers
        )
        print(f"Node created with ID: {node_id}")

        close_changeset(changeset_id, headers, api_endpoint)
        print("Changeset closed successfully")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--use-dev-api', action='store_true', help='Use the development API')
    parser.add_argument('--lat', type=str, required=True)
    parser.add_argument('--lon', type=str, required=True)
    parser.add_argument('--sign-type', type=str, required=True, choices=TRAFFIC_SIGNS.keys())
    parser.add_argument('--speed-limit', type=str, default='50')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.use_dev_api:
        from keys.dev_keys import *
    else:
        from keys.prod_keys import *
        
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/xml'
    }
    main(
        headers=headers, 
        lat=args.lat, 
        lon=args.lon, 
        api_endpoint=API_ENDPOINT,
        sign_type=args.sign_type,
        speed_limit=args.speed_limit
    )