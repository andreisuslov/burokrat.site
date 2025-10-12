from fasthtml.common import *
from src.config import get_clients_data


def render():
    """Render main content for the Clients page (Доставка, Оплата, Гарантия)."""
    data = get_clients_data()

    return (
        Section(
            Div(
                H1(data['title']),
                P(data.get('intro', '')),
                cls='page-intro'
            ),
            Div(
                P('Компания "Бюрократ"'),
                P('Работаем с 1998 года'),
                cls='clients-highlight'
            )
        ),
        Section(
            Div(
                *[
                    Div(
                        H2(section.get('heading', '')),
                        *[P(p) for p in section.get('paragraphs', [])],
                        cls='clients-section',
                        id=section.get('id', '')
                    )
                    for section in data.get('sections', [])
                ],
            ),
            cls='clients-content'
        ),
    )
