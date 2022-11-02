"""
Functionality related to "products": getting products and hidden entities for a product
"""
from quizzes.charts.chart_types import ProductId, HiddenEntities, HiddenProperties, HiddenProfiles, Products
from quizzes.charts.db_stub import hidden_props, hidden_profs, products


def get_hidden_entities(product_id: ProductId) -> HiddenEntities:
    """
    Get hidden entities - profiles and properties for a specified product

    :param product_id: id of the product
    :return: tuple contains profiles and properties
    """
    return get_hidden_profiles(product_id), get_hidden_properties(product_id)


def get_hidden_profiles(product_id: ProductId) -> HiddenProfiles:
    """
    Get hidden profiles for a specified product

    :param product_id: id of the product
    :return: HiddenProfiles (list of int)
    """
    return hidden_profs.get(product_id, [])


def get_hidden_properties(product_id: ProductId) -> HiddenProperties:
    """
    Get hidden properties for a specified product

    :param product_id: id of the product
    :return: HiddenProperties (dict with profile id as a key and list of property id as a value)
    """
    return hidden_props.get(product_id, {})


def get_products() -> Products:
    """
    Returns products (id and name for each product)

    :return: Products (dict with id as a key and name as a value)
    """
    return products
