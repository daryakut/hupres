import os
from enum import Enum

from pydantic import BaseModel

class EnvStage(Enum):
    PROD = 'production'
    DEV = 'development'
    DEV_DOCKER = 'development_docker'
    TEST = 'test'


class Env(BaseModel):
    stage: EnvStage

    def is_not_test(self):
        return self.stage != EnvStage.TEST

    def is_prod(self):
        return self.stage == EnvStage.PROD


_HUPRES_ENV = os.getenv('HUPRES_ENV') or 'test'
env = Env(stage=EnvStage(_HUPRES_ENV))

if env.stage == EnvStage.TEST:
    FRONTEND_URL = "http://localhost:3000"
    BACKEND_URL = "http://localhost:8000"
elif env.stage == EnvStage.DEV:
    FRONTEND_URL = "http://localhost:3000"
    BACKEND_URL = "http://localhost:8000"
elif env.stage == EnvStage.DEV_DOCKER:
    _HUPRES_APP_PORT = os.environ.get('HUPRES_APP_PORT')
    FRONTEND_URL = f"http://localhost:{_HUPRES_APP_PORT}"
    BACKEND_URL = f"http://localhost:{_HUPRES_APP_PORT}"
elif env.stage == EnvStage.PROD:
    _HUPRES_APP_PORT = os.environ.get('HUPRES_APP_PORT')
    _HUPRES_PROD_HOSTNAME = os.getenv('HUPRES_PROD_HOSTNAME')
    FRONTEND_URL = f"{_HUPRES_PROD_HOSTNAME}:{_HUPRES_APP_PORT}"
    BACKEND_URL = f"{_HUPRES_PROD_HOSTNAME}:{_HUPRES_APP_PORT}"
    # FRONTEND_URL = "https://hupres-web.onrender.com"
    # BACKEND_URL = "https://hupres-backend.onrender.com"
else:
    raise Exception(f"Unknown stage: {_HUPRES_ENV}")

print("ENVIRONMENT:", env.stage, BACKEND_URL, FRONTEND_URL)
