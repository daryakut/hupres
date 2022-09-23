import os

import httpx
from authlib.integrations.starlette_client import OAuth

GOOGLE_AUTH_CALLBACK_PATH = "/users/google-auth-callback"

# Manually fetch the server metadata to fix the issuer
response = httpx.get('https://accounts.google.com/.well-known/openid-configuration')
metadata = response.json()
# The issuer in the metadata is wrong. It is 'https://accounts.google.com' but should be 'accounts.google.com'
metadata['issuer'] = 'accounts.google.com'

google_oauth = OAuth()
google_oauth.register(
    name='google',
    client_id=os.environ['HUPRES_GOOGLE_0AUTH_CLIENT_ID'],
    client_secret=os.environ['HUPRES_GOOGLE_0AUTH_CLIENT_SECRET'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri=f'https://f4d9-2607-fea8-86e5-fc00-2457-6377-7d54-1aff.ngrok-free.app/{GOOGLE_AUTH_CALLBACK_PATH}',
    client_kwargs={'scope': 'openid profile email'},
    # server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    **metadata,
)
