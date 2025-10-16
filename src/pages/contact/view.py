from fasthtml.common import *
from src.config import get_contact_data, get_data
from src.components import (
    create_contact_header, 
    create_contact_info_grid, 
    create_contact_form,
    create_faq_section,
    create_map_card
)


def create_store_info_sidebar():
    """Create store info sidebar with image and map cards."""
    # Define locations for the map
    locations = [
        {
            'title': 'Офис (Строителей)',
            'address': 'Строителей проспект, 4, г. Барнаул',
            'lat': 53.3606,
            'lon': 83.7636
        },
        {
            'title': 'Магазин (Социалистический)',
            'address': 'Социалистический проспект, 109, г. Барнаул',
            'lat': 53.3482,
            'lon': 83.7765
        }
    ]
    
    return Div(
        # Visit Our Store Card
        Div(
            # Store Image
            Div(
                Img(
                    src='https://images.unsplash.com/photo-1543269865-cbf427effbad?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzNzg4Nzd8MHwxfHNlYXJjaHwxfHxzdGF0aW9uZXJ5JTIwc3RvcmV8ZW58MXx8fHwxNzA5ODExODU5fDA&ixlib=rb-4.0.3&q=80&w=1080',
                    alt='Stationery store interior',
                    cls='w-full h-64 object-cover store-image',
                    onerror="this.src='/assets/images/logo.png'; this.classList.add('object-contain', 'p-8');"
                ),
                cls='overflow-hidden store-image-container'
            ),
            # Store Info
            Div(
                H3('Посетите наш магазин', cls='text-xl mb-2 store-title'),
                P(
                    'Приходите к нам лично! Наши дружелюбные сотрудники готовы помочь вам найти именно то, что вам нужно.',
                    cls='text-gray-600 mb-4 store-description'
                ),
                A(
                    'Как добраться',
                    href='https://www.google.com/maps/search/?api=1&query=Строителей+проспект+4+Барнаул',
                    target='_blank',
                    cls='btn-outline w-full inline-block text-center store-directions-link'
                ),
                cls='p-6 store-info-content'
            ),
            cls='contact-card overflow-hidden visit-store-card',
            id='visit-store-section'
        ),
        
        # Map Card with 2GIS integration
        Div(
            create_map_card(locations),
            cls='map',
            id='map-section'
        ),
        
        cls='space-y-6 store-info-sidebar',
        id='store-sidebar'
    )


def render():
    """Render main content for the Contact page."""
    contact = get_contact_data()
    data = get_data()

    return (
        Div(
            # Contact Header
            Div(
                create_contact_header(contact.get('header')),
                id='contact-header-section',
                cls='contact-page-header'
            ),
            
            # Contact Info Grid
            Div(
                create_contact_info_grid(contact.get('info_grid')),
                id='contact-info-grid-section',
                cls='contact-info-cards'
            ),
            
            # Main Content Section (2-column layout)
            Div(
                Div(
                    # Left Column - Contact Form
                    Div(
                        create_contact_form(contact.get('form')),
                        id='contact-form-section',
                        cls='contact-form-column'
                    ),
                    
                    # Right Column - Store Info Sidebar
                    create_store_info_sidebar(),
                    
                    cls='grid lg:grid-cols-2 gap-12 contact-main-grid'
                ),
                cls='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16 contact-content-wrapper',
                id='contact-main-content'
            ),
            
            # FAQ Section
            Div(
                create_faq_section(data.get('faq')),
                id='contact-faq-section',
                cls='contact-faq-wrapper'
            ),
            
            cls='min-h-screen bg-gray-50 contact-page-container',
            id='contact-page'
        ),
    )
