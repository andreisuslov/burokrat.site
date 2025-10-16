"""Products and Services page view"""
from fasthtml.common import *
from src.config import get_db_products_services_data  # Changed to database version
from src.components import create_products_page

def render():
    """Render main content for the Products and Services page."""
    data = get_db_products_services_data()  # Changed to database version
    return create_products_page(data)
