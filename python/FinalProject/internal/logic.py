from decorators import log
from pizza import Pizza


@log("🍕‍Приготовили за {}с!")
def bake(pizza: Pizza):
    """Pizza making"""
    pass


@log("🛵 Доставили за {}с!")
def to_delivery(pizza: Pizza):
    """Pizza delivering"""
    pass


@log("🏠 Забрали за {}с!")
def pickup(pizza: Pizza):
    """Pizza issuance"""
    pass
