from fasthtml.common import *
from src.components import Layout
from src.config import get_stationery_data

def register_stationery_route(rt):
    """Register stationery page route."""
    
    @rt('/stationery')
    def get():
        data = get_stationery_data()
        page_data = data.get('page', {})
        
        return Layout(
            data.get('title', 'Канцелярские товары | Бюрократ'),
            Section(
                H1(page_data.get('intro', {}).get('heading', 'Канцелярские товары')),
                P(page_data.get('intro', {}).get('description', 'Широкий ассортимент канцелярских товаров для офиса и дома')),
                cls='page-intro'
            ),
            Section(
                H2(page_data.get('categories', {}).get('section_title', 'Категории товаров')),
                Div(
                    *[
                        Div(
                            Div(
                                Img(src=category.get('image', '/assets/images/icon.png'), alt=category.get('title', '')),
                                cls='service-card-image'
                            ),
                            Div(
                                H3(category.get('title', '')),
                                P(category.get('description', '')) if category.get('description') else None,
                                cls='service-card-content'
                            ),
                            cls='category-card'
                        )
                        for category in page_data.get('categories', {}).get('items', [])
                    ],
                    cls='category-grid'
                ),
                cls='categories-section'
            )
        )
