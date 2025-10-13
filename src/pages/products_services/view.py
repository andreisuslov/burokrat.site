"""Products and Services page view"""
from fasthtml.common import *
from src.config import get_products_services_data
from src.components import create_products_page

def render():
    """Render main content for the Products and Services page."""
    data = get_products_services_data()
    return create_products_page(data)
