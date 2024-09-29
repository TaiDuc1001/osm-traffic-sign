import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import requests
import logging
from datetime import datetime
import xml.etree.ElementTree as ET

def get_access_token(out_txt='out.txt'):
    with open(out_txt, 'r') as f:
        for line in f:
            if 'Access token' in line:
                return line.split(':')[-1].strip()
    return None

def gen_comment(type: str, lat: float, lon: float):
    logging.basicConfig(filename='changeset.log', level=logging.INFO, 
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    comment = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {type} sign at {lat}, {lon}"
    logging.info(comment)
    return comment

def create_changeset(comment, api_endpoint, headers):
    changeset_xml = f'''
    <osm>
        <changeset>
            <tag k="created_by" v="Python Script"/>
            <tag k="comment" v="{comment}"/>
        </changeset>
    </osm>
    '''
    
    response = requests.put(f'{api_endpoint}/changeset/create', data=changeset_xml, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to create changeset: {response.text}")
    
def create_node(changeset_id, lat, lon, tags, api_endpoint, headers):
    node_xml = ET.Element('osm')
    node = ET.SubElement(node_xml, 'node', changeset=changeset_id, lat=str(lat), lon=str(lon))
    for key, value in tags.items():
        ET.SubElement(node, 'tag', k=key, v=value)
    
    response = requests.put(f'{api_endpoint}/node/create', data=ET.tostring(node_xml), headers=headers)
    
    if response.status_code == 200:
        return response.text 
    else:
        raise Exception(f"Failed to create node: {response.text}")
    
def close_changeset(changeset_id, headers, api_endpoint):
    response = requests.put(f'{api_endpoint}/changeset/{changeset_id}/close', headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to close changeset: {response.text}")