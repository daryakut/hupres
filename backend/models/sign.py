from __future__ import annotations

from enum import Enum

from common.utils import check_not_none


class Sign(Enum):
    FIRE = 'FIRE'
    EARTH = 'EARTH'
    METAL = 'METAL'
    WATER = 'WATER'
    WOOD = 'WOOD'

    @staticmethod
    def from_index(index) -> Sign:
        sign = _INDEX_TO_SIGN.get(index)
        check_not_none(sign, f'No sign found for index {index}')
        return sign


_INDEX_TO_SIGN = {
    0: Sign.FIRE,
    1: Sign.EARTH,
    2: Sign.METAL,
    3: Sign.WATER,
    4: Sign.WOOD,
}
