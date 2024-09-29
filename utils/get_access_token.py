import webbrowser
import requests
import urllib.parse
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Get access token for the user')
    parser.add_argument('--use-dev-api', action='store_true', help='Use the development API')
    return parser.parse_args()

def main():
    scope = 'read_prefs write_api'
    auth_params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': scope
    }
    authorization_url = f"{AUTHORIZATION_BASE_URL}?{urllib.parse.urlencode(auth_params)}"

    print(f"Please go to this URL and authorize the application: {authorization_url}")
    webbrowser.open(authorization_url)

    authorization_code = input('Enter the authorization code: ')

    token_params = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=token_params)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        if access_token:
            print(f"Access token obtained: {access_token}")
            
            headers = {'Authorization': f'Bearer {access_token}'}
            user_details_url = f'{API_ENDPOINT}user/details'
            user_response = requests.get(user_details_url, headers=headers)
            
            if user_response.status_code == 200:
                print("Successfully retrieved user details")
            else:
                print(f"Failed to get user details. Status code: {user_response.status_code}")
                print(user_response.text)
        else:
            print("Access token not found in the response")
            print(f"Full response: {token_data}")
    else:
        print(f"Failed to obtain access token. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    args = parse_args()
    if args.use_dev_api:
        from dev_keys import *
    else:
        from prod_keys import *

    main()