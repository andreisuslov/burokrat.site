from fasthtml.common import *
from src.config import get_data, get_contact_data
from src.components import create_service_card
from src.pages.home.contact_form import build_contact_form


def render():
    """Render main content for the Home page."""
    data = get_data()
    contact = get_contact_data()

    return (
        Section(
            Div(
                H1(data['title']),
                P(data['description']),
                cls='hero'
            ),
            cls='hero-section'
        ),
        Section(
            H2('Наши услуги'),
            Div(
                *[create_service_card(item) for item in data['navigation']['main_menu'] if item['url'] != '/about'],
                cls='service-grid'
            ),
            cls='services-section',
            id='services-section'
        ),
        build_contact_form(contact),
    )
