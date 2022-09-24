from enum import Enum

from pydantic import BaseModel


class EnvStage(Enum):
    PROD = 'PROD'
    TEST = 'TEST'


class Env(BaseModel):
    stage: EnvStage

    def is_not_test(self):
        return self.stage != EnvStage.TEST


env = Env(stage=EnvStage.PROD)
