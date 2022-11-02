from enum import Enum


class Pronounce(Enum):
    """Instead of the gender, this is what western world uses. Hopefully these choices is enough"""
    HE_HIM = 'HE_HIM'
    SHE_HER = 'SHE_HER'
    THEY_THEM = 'THEY_THEM'
    PREFER_NOT_TO_SAY = 'PREFER_NOT_TO_SAY'
