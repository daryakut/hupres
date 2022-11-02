from enum import Enum


class Sign(Enum):
    # It's important to start with 0 because we want indexes in the array to match the enum values
    FIRE = 'FIRE'
    EARTH = 'EARTH'
    METAL = 'METAL'
    WATER = 'WATER'
    WOOD = 'WOOD'
