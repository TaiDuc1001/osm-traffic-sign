import argparse
from dev_keys import *
from utils import create_changeset, create_node, close_changeset, \
                    gen_comment

def main(**kwargs):
    headers = kwargs.get('headers', None)
    api_endpoint = kwargs.get('api_endpoint', None)
    lat = kwargs.get('lat', None)
    lon = kwargs.get('lon', None)
    name = kwargs.get('name', None)
    comment = gen_comment(type='Stop', lat=lat, lon=lon)

    try:
        changeset_id = create_changeset(
            comment=comment, 
            api_endpoint=api_endpoint, 
            headers=headers
        )
        print(f"Changeset created with ID: {changeset_id}")

        tags = {
            'name': name,
            'amenity': 'cafe',
            'description': 'A sample point of interest'
        }
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
    parser.add_argument('--lat', type=float, required=True)
    parser.add_argument('--lon', type=float, required=True)
    parser.add_argument('--name', type=str, required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/xml'
    }
    main(
        headers=headers, 
        lat=args.lat, 
        lon=args.lon, 
        api_endpoint=API_ENDPOINT,
        name=args.name
    )