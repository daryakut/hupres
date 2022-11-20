import requests
from typing import List
from quizzes.charts.chart_types import SomaType, ProductId, PreparedSomaType, ChartInfo, Property, Profile, Gender, ELEMENTS
from quizzes.charts.product import get_hidden_entities


class ENetworkError(Exception):
    """
    Raised in _make_request() where http response is not 200
    """
    def __init__(self, response: requests.Response):
        super().__init__(f'Bad network response: code {response.status_code} ("{response.text}")')


class EServerError(Exception):
    """
    Raised in _make_request() where http response is 200 but the server script returns "status": "ERR"
    """
    def __init__(self, response: dict):
        super().__init__(f'Bad server response: {response["info"]}')


DEFAULT_GENDER = Gender.NONE

# ZZZ is important because that's what is used in localization files
NAME_PLACEHOLDER = 'ZZZ'

URL_DATA = 'http://diag.ho.ua/calc'
URL_NAMES = 'http://diag.ho.ua/db/names'

DEFAULT_ELEMENT_COUNT = 3
DEFAULT_LANG = 'ru'

STATUS_OK = 'OK'


def _make_request(url: str, response_field: str, **params) -> list | dict:
    response = requests.get(url, params=params)
    if not response.ok:
        raise ENetworkError(response)
    data = response.json()
    if data['status'] != STATUS_OK:
        raise EServerError(data)
    return data[response_field]


def get_chart_info(product_id: ProductId, soma_type: SomaType, respondent_name='',
                   gender=DEFAULT_GENDER, lang=DEFAULT_LANG, debug_mode=False) -> ChartInfo:
    """
    The most important function of this package: return text and chart information by a somatype given

    :param product_id: id of the product (see get_products())
    :param soma_type: list of int values in the fixed order (see ELEMENTS)
    :param respondent_name: name of the respondent if specified
    :param gender: one of Gender values
    :param lang: language for text fields
    :param debug_mode: reserved to future use
    :return: list of Profile instances
    """
    # First, get hidden entities for the product specified:
    # hidden profiles - we must exclude their id from query params
    # hidden properties of visible profiles - we must exclude them from the query result
    bad_profiles, bad_props = get_hidden_entities(product_id)

    # Get a whole collection of profiles & properties available
    response = get_names(lang)

    # Filter the collection: rid off hidden profiles and hidden properties in visible profiles
    good_profiles = dict()
    for profile in response:
        profile_id = int(profile['id'])
        if profile_id not in bad_profiles:
            good_profiles[profile_id] = {
                'id': profile_id,
                'name': profile['name'],
                'props': [
                    int(p['id']) for p in profile['props'] if int(p['id']) not in bad_props.get(profile_id, [])
                ]
            }

    # Prepare the "elem" array query params
    elements = {
        f'elem[{key}]': value for key, value in prepare_soma_type(soma_type).items()
    }

    # Query params
    params = {
        **elements,
        'prof[]': list(good_profiles),
        'debug': '1' if debug_mode else '0',
        'lang': lang,
        'gender': gender
    }
    charts = _make_request(URL_DATA, 'charts', **params)
    result = []
    for chart in charts:
        profile_id = int(chart['id'])
        valid_props = good_profiles[profile_id]['props']
        data = chart['data']
        props = []
        for index, prop_id in enumerate(data['ids']):
            if int(prop_id) in valid_props:
                text = data['texts'][index]
                text = text.replace(NAME_PLACEHOLDER, respondent_name)
                props.append(
                    Property(int(prop_id), data['values'][index], data['names'][index], text)
                )
        result.append(
            Profile(profile_id, chart['name'], props)
        )
    return result


def get_names(lang=DEFAULT_LANG) -> List[dict]:
    """
    Get a collection of all profiles & properties available

    :param lang: language for text fields
    :return: list of dicts describing profiles and their properties
    """
    return _make_request(URL_NAMES, 'names', lang=lang)


def prepare_soma_type(soma_type: SomaType, element_count: int = DEFAULT_ELEMENT_COUNT) -> PreparedSomaType:
    """
    Prepare a calculated soma_type to use it as a query param

    :param soma_type:
    :param element_count:
    :return:
    """
    # [-2, 10, 26, 5, 1] => [('M', 26), ('E', 10), ('W', 5), ('T', 1), ('F', -2)]
    elements = sorted(zip(ELEMENTS, soma_type), key=lambda item: item[1], reverse=True)
    if element_count < len(soma_type):
        # if element_count is 3 then elements become [('M', 26), ('E', 10), ('W', 5)]
        elements = elements[:element_count]
    # for [('M', 26), ('E', 10), ('W', 5)] summary is 26 + 10 + 5 == 42
    summary = sum([value for _, value in elements])
    # for [('M', 26), ('E', 10), ('W', 5)] percentage is [('M', 63), ('E', 24), ('W', 12)]
    percentage = [(el, round((value * 100) / summary)) for el, value in elements]
    # Back checking: percents_summary must be 100
    percents_summary = sum([value for _, value in percentage])
    deviation = percents_summary - 100
    if deviation:
        # if percents < 100 we increase the smallest value else decrease the biggest
        index = 0 if deviation > 0 else -1
        percentage[index] = percentage[index][0], percentage[index][1] - deviation
    # [('M', 63), ('E', 24), ('W', 13)] => {'E': 24, 'M': 63, 'W': 13}
    return dict(percentage)
