from fasthtml.common import *

def create_burger_menu(nav_items):
    """
    Create a responsive burger menu component.
    
    This component automatically switches between horizontal navigation (desktop)
    and a dropdown burger menu (mobile) based on available space.
    
    Features:
    - Automatic responsive behavior via JavaScript
    - Animated burger icon (transforms to X when active)
    - Dropdown menu with smooth transitions
    - Click outside to close
    - Auto-close when clicking nav links
    
    Args:
        nav_items: List of navigation items (Li elements with A tags)
    
    Returns:
        Tuple of (burger_button, nav_container) components
    """
    
    burger_button = Button(
        Img(src='/assets/images/pen-burger.svg', alt='', cls='burger-bar-top'),
        Img(src='/assets/images/pencil-burger.svg', alt='', cls='burger-bar-bottom'),
        cls='burger-btn',
        id='burgerBtn',
        aria_label='Menu'
    )
    
    nav_container = Nav(
        Ul(*nav_items, cls='nav-menu'),
        cls='nav-container',
        id='navContainer'
    )
    
    return burger_button, nav_container


def burger_menu_script():
    """
    Returns the Script tag for burger menu functionality.
    
    This script handles:
    - Responsive layout detection (switches to burger when content overflows)
    - Burger button toggle behavior
    - Click outside to close
    - Auto-close on navigation link clicks
    - Dropdown positioning
    """
    return Script(src='/assets/scripts/header-nav.js')
