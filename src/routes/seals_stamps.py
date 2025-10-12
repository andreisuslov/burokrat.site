from fasthtml.common import *
from src.components import Layout
from src.config import get_seals_stamps_data

def register_seals_stamps_route(rt):
    """Register seals and stamps page route."""
    
    @rt('/seals-and-stamps')
    def get():
        data = get_seals_stamps_data()
        page_data = data.get('page', {})
        
        return Layout(
            data.get('title', 'Печати и штампы | Бюрократ'),
            Section(
                H1(page_data.get('intro', {}).get('heading', 'Печати и штампы')),
                P(page_data.get('intro', {}).get('description', 'Изготовление печатей и штампов любой сложности')),
                cls='page-intro'
            ),
            Section(
                H2(page_data.get('products', {}).get('section_title', 'Наши продукты')),
                Div(
                    *[
                        Div(
                            Div(
                                Img(src=product.get('image', '/assets/images/icon.png'), alt=product.get('title', '')),
                                cls='service-card-image'
                            ),
                            Div(
                                H3(product.get('title', '')),
                                P(product.get('description', '')) if product.get('description') else None,
                                Button(
                                    product.get('button_text', 'Заказать'),
                                    hx_get=product.get('button_action', '/contact-form'),
                                    hx_target='#modal',
                                    hx_swap='innerHTML',
                                    cls='btn btn-primary'
                                ),
                                cls='service-card-content'
                            ),
                            cls='product-card'
                        )
                        for product in page_data.get('products', {}).get('items', [])
                    ],
                    cls='product-grid'
                ),
                cls='products-section'
            ),
            Div(id='modal')
        )
