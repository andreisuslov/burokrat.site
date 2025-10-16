"""Products and Services page route"""
from fasthtml.common import *
from src.components import Layout
from src.config import get_db_products_services_data  # Changed to database version
from src.pages.products_services.view import render as render_products_services
import logging


def register_products_services_route(rt):
    """Register products and services page route."""
    
    @rt('/products-and-services')
    def get():
        logging.info("📦 Serving products & services page (/products-and-services) [FROM DATABASE]")
        data = get_db_products_services_data()  # Changed to database version
        return Layout(
            data['title'],
            render_products_services()
        )

