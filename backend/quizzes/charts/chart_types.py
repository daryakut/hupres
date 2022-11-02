"""
Types and helper classes
"""

from typing import Dict, List, Tuple

ProductId = int
ProfileId = int
PropertyId = int
HiddenProfiles = List[ProfileId]
HiddenProperties = Dict[ProfileId, List[PropertyId]]
HiddenEntities = Tuple[HiddenProfiles, HiddenProperties]
Products = Dict[ProductId, str]
SomaType = List[int]
PreparedSomaType = Dict[str, int]

ELEMENTS = ['F', 'E', 'M', 'W', 'T']  # Fire, Earth, Metal, Water, Tree


class Gender:
    MALE = 'M'
    FEMALE = 'F'
    NONE = '-'


class Property:
    id: PropertyId
    value: float
    name: str
    text: str

    def __init__(self, prop_id: PropertyId, value: float, name: str, text: str):
        self.id = prop_id
        self.name = name
        self.text = text
        self.value = value


Properties = List[Property]


class Profile:
    id: ProfileId
    name: str
    properties: Properties

    def __init__(self, prof_id: ProfileId, name: str, props: Properties):
        self.id = prof_id
        self.name = name
        self.properties = props


ChartInfo = List[Profile]


def export_chart_info(chart_info: ChartInfo) -> list:
    return [
        {
            'id': profile.id,
            'name': profile.name,
            'properties': [
                {'id': p.id, 'name': p.name, 'value': p.value, 'text': p.text} for p in profile.properties
            ]
        } for profile in chart_info
    ]