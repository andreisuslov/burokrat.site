from fasthtml.common import *
from src.components import Layout
import logging

def register_engraving_route(rt):
    """Register engraving page route."""
    
    @rt('/engraving')
    def get():
        logging.info("🔨 Serving engraving page (/engraving)")
        return Layout(
            'Гравировка | Бюрократ',
            Section(
                H1('Профессиональные услуги гравировки'),
                P('Гравировка на различных материалах'),
                cls='page-intro'
            ),
            Section(
                H2('Виды гравировки'),
                Ul(
                    Li('Гравировка на металле'),
                    Li('Гравировка на пластике'),
                    Li('Гравировка на дереве'),
                    Li('Лазерная гравировка'),
                ),
                cls='services-list'
            )
        )
