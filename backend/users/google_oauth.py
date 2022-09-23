import os

import httpx
from authlib.integrations.starlette_client import OAuth
import jwt
from authlib.jose import JsonWebKey
from authlib.jose import jwt as authlib_jwt

GOOGLE_AUTH_CALLBACK_PATH = "/users/google-auth-callback"

google_public_keys = httpx.get('https://www.googleapis.com/oauth2/v3/certs').json()

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


def decode_id_token_email_address(token: dict):
    # Technically, we don't need to decode the id_token because we already have 'email' in the token itself
    # However, decoding id_token is considered a better security practice
    # If this ever stops working and you don't have time to figure it out, just return token['email']
    id_token = token['id_token']

    kid = jwt.get_unverified_header(id_token)['kid']
    for public_key in google_public_keys["keys"]:
        if public_key['kid'] != kid:
            continue
        jwk = JsonWebKey()
        jwk_key = jwk.import_key(public_key)
        decoded_key = authlib_jwt.decode(id_token, jwk_key.as_pem())
        return decoded_key['email']
    raise ValueError(f"Could not decode id_token: could not find public key with matching kid ${kid}")
