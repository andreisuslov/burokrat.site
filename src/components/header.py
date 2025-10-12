from fasthtml.common import *
from src.config import get_data

def create_header():
    """Create header component with logo and navigation."""
    data = get_data()
    
    nav_items = [
        Li(A(item['label'], href=item['url'])) 
        for item in data['navigation']['main_menu']
    ]
    
    return [
        Div(
            H1(
                A(
                    Img(src='/assets/images/logo.png', 
                        alt=data['company_info']['name'], 
                        cls='logo-image', 
                        title=data['company_info']['name']),
                    href='/',
                    cls='logo-link'
                )
            ),
            Button(
                Span(cls='burger-bar'),
                Span(cls='burger-bar'),
                cls='burger-btn',
                id='burgerBtn',
                aria_label='Menu'
            ),
            Nav(
                Ul(*nav_items, cls='nav-menu'),
                cls='nav-container',
                id='navContainer'
            ),
            cls='header-content'
        ),
        Script(src='/assets/scripts/header-nav.js')
    ]
