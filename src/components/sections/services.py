"""Services section component"""
from fasthtml.common import *
from src.components.contact import create_service_card


def create_services(data):
    """Create the services section component."""
    
    return Section(
        Div(
            H2('Наши услуги'),
            Div(
                *[create_service_card(item) for item in data['main_menu'] if item['url'] != '/about'],
                cls='service-grid'
            ),
            cls='container'
        ),
        cls='section services-section',
        id='services-section'
    )
