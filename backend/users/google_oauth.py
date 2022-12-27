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

GOOGLE_PUBLIC_KEYS = {
    "keys": [
        {
            "kid": "9b0285c31bfd8b040e03157b19c4e960bdc10c6f",
            "use": "sig",
            "n": "uCYe4j3rIDaC9U8jCloiD5UP5cQCndcKr570LSxEznqNB0qpmtqDJBU-RuSJbMEYZ853AlezSWca8uqDBAgdIWPod-scaQTOTg049m9hFwQuP7FzXsAjtxiOHub0nrD60Dy7vI1dPoiyiFdox25JUdW6OSPyq2OlFxCPIQy4SpKvebXduA2ZeIY5TWE2wt0mVPo__s9NACn4Ni9GwsPCcgG6yn8oAJ-JW6xCLnz5_CycNlg178Sxj8LWVEisPbdEK9LhSwQ7V3YU7pfLpEAtGWHYrIcH3-Tfz6IkS9-UmAzbdjaGk2W-AXkZW8jiIbfNER7e4ZKLntC4Am4InHkJzw",
            "kty": "RSA",
            "e": "AQAB",
            "alg": "RS256"
        },
        {
            "kid": "456b52c81e36fead259231a6947e040e03ea1262",
            "n": "1yFBscIm7d2VYYx8dSK4R4b5EOLKoFXPdr-B9RVYaFS_XHso47Mdc5_oj8DwYGeeJgvJN6kKrDqRd3W3JmEkA-woKe6e0Vd56sMWvc2s94utfI8AiXBNwXAYnCQWGHnu9faF903JaRDJTeaRTSmbrSMibpshpK2PcOtOk0Fb9CyZm9E8jSMblMa3jhW8vlTnln3r4qgr1nwddbOj0WEmAjwA7G32EdlF5Oz30_HeTiEKpMtLumf0GbmCP23dyc8Ibrl8ahhEdGtBBb8tDCIroB2C_O_QBdYVE8GZW2ZUBSEx7-riMZ5h--2bweM94I6dMSBke9IZ2582Sn8j3lFEWw",
            "alg": "RS256",
            "e": "AQAB",
            "kty": "RSA",
            "use": "sig"
        }
    ]
}


def generate_state():
    return secrets.token_urlsafe(32)


class GoogleOAuthService:
    google_public_keys: dict
    google_oauth: OAuth

    def __init__(self):
        try:
            self.google_public_keys = httpx.get('https://www.googleapis.com/oauth2/v3/certs').json()
        except Exception:
            self.google_public_keys = GOOGLE_PUBLIC_KEYS

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
        for public_key in self.google_public_keys["keys"]:
            if public_key['kid'] != kid:
                continue
            jwk = JsonWebKey()
            jwk_key = jwk.import_key(public_key)
            decoded_key = authlib_jwt.decode(id_token, jwk_key.as_pem())
            return decoded_key['email']
        raise ValueError(f"Could not decode id_token: could not find public key with matching kid {kid}")


google_oauth_service = GoogleOAuthService() if env.is_not_test() else get_fake_google_oauth_service()
