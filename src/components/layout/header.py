from fasthtml.common import *
from src.config import get_navigation_data
from .burger_menu import create_burger_menu, burger_menu_script

def create_header(data):
    """Create header component with logo and navigation."""
    
    nav_data = get_navigation_data()
    nav_items = [
        Li(A(item['label'], href=item['url'])) 
        for item in nav_data['main_menu']
    ]
    
    # Create burger menu components
    burger_button, nav_container = create_burger_menu(nav_items)
    
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
            burger_button,
            nav_container,
            cls='header-content'
        ),
        burger_menu_script()
    ]
