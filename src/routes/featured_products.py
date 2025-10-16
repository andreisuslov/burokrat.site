from fasthtml.common import *
from src.components import Layout, create_featured_products
from src.config import get_db_featured_products_data  # Changed to database version
import logging


def register_featured_products_route(rt):
    """Register featured products demo page route."""
    
    @rt('/featured-products')
    def get():
        logging.info("⭐ Serving featured products page (/featured-products) [FROM DATABASE]")
        data = {'featured_products': get_db_featured_products_data()}  # Changed to database version
        
        return Layout(
            'Избранные товары | Бюрократ',
            Section(
                Div(
                    H1('Избранные товары', cls='page-title'),
                    P('Тщательно отобранные товары, любимые нашими покупателями', cls='page-subtitle'),
                    cls='page-intro'
                ),
                cls='section'
            ),
            create_featured_products(data)
        )
