from fasthtml.common import *
from src.config import get_contact_data
from src.pages.home.contact_form import build_contact_form
from src.components import create_contact_info


def render():
    """Render main content for the Contact page."""
    contact = get_contact_data()

    return (
        # Hero Section
        Section(
            Div(
                H1(contact['title']),
                P(contact['intro']),
                cls='hero'
            ),
            cls='hero-section'
        ),
        
        # Contact Form Section
        build_contact_form(contact),
        
        # Contact Info Section
        Section(
            H2('Контактная информация'),
            create_contact_info(),
            cls='contact-info-section'
        ),
    )
