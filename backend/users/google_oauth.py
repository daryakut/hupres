import os

import httpx
import jwt
from authlib.integrations.starlette_client import OAuth
from authlib.jose import JsonWebKey
from authlib.jose import jwt as authlib_jwt
from fastapi import Request

from common.env import env, BACKEND_URL
from tests.users.fake_google_oauth import get_fake_google_oauth_service
import secrets

GOOGLE_AUTH_CALLBACK_PATH = "/api/users/google-auth-callback"
REDIRECT_URI = f'{BACKEND_URL}{GOOGLE_AUTH_CALLBACK_PATH}'


def generate_state():
    return secrets.token_urlsafe(32)


def get_google_public_keys():
    google_public_keys = httpx.get('https://www.googleapis.com/oauth2/v3/certs').json()
    print('google_public_keys', google_public_keys)
    return google_public_keys.get("keys", [])


class GoogleOAuthService:
    google_oauth: OAuth

    def __init__(self):
        # Manually fetch the server metadata to fix the issuer
        response = httpx.get('https://accounts.google.com/.well-known/openid-configuration')
        metadata = response.json()
        # The issuer in the metadata is wrong. It is 'https://accounts.google.com' but should be 'accounts.google.com'
        metadata['issuer'] = 'accounts.google.com'
        self.google_oauth = OAuth()
        self.google_oauth.register(
            name='google',
            client_id=os.environ['HUPRES_GOOGLE_0AUTH_CLIENT_ID'],
            client_secret=os.environ['HUPRES_GOOGLE_0AUTH_CLIENT_SECRET'],
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_params=None,
            refresh_token_url=None,
            redirect_uri=REDIRECT_URI,
            client_kwargs={'scope': 'openid profile email'},
            # server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            **metadata,
        )

    async def authorize_redirect(self, request: Request, redirect_uri: str):
        return await self.google_oauth.google.authorize_redirect(request, redirect_uri)

    async def authorize_access_token_and_get_email_address(self, request) -> str:
        token = await self.google_oauth.google.authorize_access_token(request)
        print(f"token {token}")

        email_address = self._decode_id_token_email_address(token)
        print(f"email_address {email_address}")

        return email_address

    def _decode_id_token_email_address(self, token: dict):
        # Technically, we don't need to decode the id_token because we already have 'email' in the token itself
        # However, decoding id_token is considered a better security practice
        # If this ever stops working and you don't have time to figure it out, just return token['email']
        id_token = token['id_token']

        kid = jwt.get_unverified_header(id_token)['kid']
        google_public_keys = get_google_public_keys()
        for public_key in google_public_keys:
            if public_key['kid'] != kid:
                continue
            jwk = JsonWebKey()
            jwk_key = jwk.import_key(public_key)
            decoded_key = authlib_jwt.decode(id_token, jwk_key.as_pem())
            return decoded_key['email']
        raise ValueError(f"Could not decode id_token: could not find public key with "
                         f"matching kid {kid} in {google_public_keys}")


google_oauth_service = GoogleOAuthService() if env.is_not_test() else get_fake_google_oauth_service()
