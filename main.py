import os
def get_access_token() -> str:
    command = f'''
        python get_access_token.py
    '''
    return command

def upload(lat, lon, name) -> str:
    command = f'''
        python upload.py --lat {lat} --lon {lon} --name {name}
    '''
    return command

if __name__ == '__main__':
    os.system(get_access_token())
    lat = 37.7749
    lon = -122.4194
    name = 'Example of Traffic Sign'
    os.system(upload(lat, lon, name))