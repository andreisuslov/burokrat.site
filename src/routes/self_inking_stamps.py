from fasthtml.common import *
from src.components import Layout
from src.config import get_self_inking_stamps_data
import logging

def register_self_inking_stamps_route(rt):
    """Register self-inking stamps page route."""
    
    @rt('/self-inking-stamps')
    def get():
        logging.info("🖊️  Serving self-inking stamps page (/self-inking-stamps)")
        data = get_self_inking_stamps_data()
        page_data = data.get('page', {})
        
        return Layout(
            data.get('title', 'Оснастки | Бюрократ'),
            Section(
                H1(page_data.get('intro', {}).get('heading', 'Оснастки для печатей и штампов')),
                P(page_data.get('intro', {}).get('description', 'Широкий выбор оснасток для печатей и штампов')),
                cls='page-intro'
            ),
            Section(
                H2(page_data.get('products', {}).get('section_title', 'Каталог оснасток')),
                Div(
                    P(page_data.get('products', {}).get('description', 'Автоматические оснастки различных размеров')),
                    cls='product-grid'
                ),
                cls='products-section'
            )
        )
