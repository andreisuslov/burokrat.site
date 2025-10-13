"""Products and Services page route"""
from fasthtml.common import *
from src.components import Layout
from src.config import get_products_services_data
from src.pages.products_services.view import render as render_products_services
import logging


def register_products_services_route(rt):
    """Register products and services page route."""
    
    @rt('/products-and-services')
    def get():
        logging.info("📦 Serving products & services page (/products-and-services)")
        data = get_products_services_data()
        return Layout(
            data['title'],
            render_products_services()
        )

