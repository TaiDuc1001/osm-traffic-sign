import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import get_access_token

# First go to <BASE_URL>/oauth2/applications and create a new application
# Name can be anything, and the redirect URI should be the same as REDIRECT_URI

CLIENT_ID = '...your client id...'
CLIENT_SECRET = '..your client secret...'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob' # Suggest to use this value
ACCESS_TOKEN = get_access_token('keys/out.txt')

# For development purposes, use the dev server
API_ENDPOINT = 'https://master.apis.dev.openstreetmap.org/api/0.6/'
BASE_URL = 'https://master.apis.dev.openstreetmap.org'
AUTHORIZATION_BASE_URL = 'https://master.apis.dev.openstreetmap.org/oauth2/authorize'
TOKEN_URL = 'https://master.apis.dev.openstreetmap.org/oauth2/token'

# For production, use the production server
API_ENDPOINT = 'https://api.openstreetmap.org/api/0.6/'
BASE_URL = 'https://www.openstreetmap.org'
AUTHORIZATION_BASE_URL = 'https://www.openstreetmap.org/oauth/authorize'
TOKEN_URL = 'https://www.openstreetmap.org/oauth/access_token'
