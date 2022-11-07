import os
from enum import Enum

from pydantic import BaseModel


class EnvStage(Enum):
    PROD = 'production'
    DEV = 'development'
    TEST = 'test'


class Env(BaseModel):
    stage: EnvStage

    def is_not_test(self):
        return self.stage != EnvStage.TEST


if os.getenv('ENV') == 'development':
    _stage = EnvStage.DEV
    FRONTEND_URL = "http://localhost:3000"
elif os.getenv('ENV') == 'test':
    _stage = EnvStage.TEST
    FRONTEND_URL = "http://localhost:3000"
else:
    _stage = EnvStage.PROD
    FRONTEND_URL = "https://hupres-web.onrender.com"

print("ENVIRONMENT:", _stage, FRONTEND_URL)

env = Env(stage=_stage)
