from fasthtml.common import *
from src.components import Layout, create_featured_products
from src.config import get_featured_products_data
import logging


def register_featured_products_route(rt):
    """Register featured products demo page route."""
    
    @rt('/featured-products')
    def get():
        logging.info("⭐ Serving featured products page (/featured-products)")
        data = {'featured_products': get_featured_products_data()}
        
        return Layout(
            'Featured Products | Burokrat',
            Section(
                Div(
                    H1('Featured Products Demo', cls='page-title'),
                    P('This is a demo page showcasing the featured products component.', cls='page-subtitle'),
                    cls='page-intro'
                ),
                cls='section'
            ),
            create_featured_products(data)
        )
