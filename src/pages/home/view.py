from fasthtml.common import *
from src.config import get_hero_data, get_services_data, get_contact_data, get_shop_categories_data, get_featured_products_data
from src.components import create_hero, create_services, create_contact, create_shop_categories, create_featured_products


def render():
    """Render main content for the Home page."""
    return (
        create_hero(get_hero_data()),
        create_shop_categories({'shop_categories': get_shop_categories_data()}),
        create_featured_products({'featured_products': get_featured_products_data()}),
        create_services(get_services_data()),
        create_contact(get_contact_data()),
    )
