from enum import Enum
import os
from pydantic import BaseModel


class EnvStage(Enum):
    PROD = 'PROD'
    TEST = 'TEST'


class Env(BaseModel):
    stage: EnvStage

    def is_not_test(self):
        return self.stage != EnvStage.TEST


_is_development = os.getenv('ENV') == 'development'
_stage = EnvStage.TEST if _is_development else EnvStage.PROD
FRONTEND_URL = "http://localhost:3000" if _is_development else "https://hupres-web.onrender.com"

print("ENVIRONMENT:", _stage, FRONTEND_URL)

env = Env(stage=_stage)
