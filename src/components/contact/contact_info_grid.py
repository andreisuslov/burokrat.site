from fasthtml.common import *


def create_icon_svg(icon_type):
    """Create inline SVG icons similar to lucide-react."""
    icons = {
        'map-pin': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>''',
        'phone': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>''',
        'clock': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>''',
        'mail': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>''',
    }
    return NotStr(icons.get(icon_type, icons['map-pin']))


def create_contact_card(item):
    """Create a single contact info card."""
    icon = item.get('icon', 'map-pin')
    title = item.get('title', '')
    content = item.get('content', '')
    color = item.get('color', 'bg-indigo-100 text-indigo-600')
    link = item.get('link', None)
    
    # Create content element with proper line breaks
    content_element = P(
        content,
        cls='text-gray-600 whitespace-pre-line'
    )
    
    # If there's a link, wrap content in anchor
    if link:
        content_element = A(
            content,
            href=link,
            target='_blank',
            cls='text-gray-600 whitespace-pre-line hover:text-indigo-600 transition-colors'
        )
    
    return Div(
        # Icon container
        Div(
            Div(
                create_icon_svg(icon),
                cls='w-6 h-6'
            ),
            cls=f'{color} w-12 h-12 rounded-xl flex items-center justify-center mb-4'
        ),
        
        # Title
        H3(title, cls='mb-2'),
        
        # Content
        content_element,
        
        cls='contact-card p-6 hover:shadow-lg transition-shadow'
    )


def create_contact_info_grid(items=None):
    """
    Create contact info grid component.
    
    Args:
        items: List of contact info items, each with:
            - icon: Icon type ('map-pin', 'phone', 'clock', 'mail')
            - title: Card title
            - content: Card content (supports newlines)
            - color: Tailwind color classes for icon background
            - link: Optional URL to make content clickable
    """
    if items is None:
        # Default items as example
        items = [
            {
                'icon': 'map-pin',
                'title': 'Visit Us (Stroiteley)',
                'content': 'Prospekt Stroiteley, 4\nBarnaul, Altayskiy kray, 656002',
                'color': 'bg-indigo-100 text-indigo-600',
                'link': 'https://www.google.com/maps/search/?api=1&query=Prospekt+Stroiteley+4+Barnaul'
            },
            {
                'icon': 'phone',
                'title': 'Call Us',
                'content': '+7 (3852) 62-82-82\n+7 (3852) 25-14-91',
                'color': 'bg-green-100 text-green-600',
            },
            {
                'icon': 'clock',
                'title': 'Working Hours',
                'content': 'Monday - Sunday\n09:30 - 18:30',
                'color': 'bg-purple-100 text-purple-600',
            },
            {
                'icon': 'mail',
                'title': 'Email Us',
                'content': 'L628282@yandex.ru\ns628282@gmail.com',
                'color': 'bg-orange-100 text-orange-600',
            },
        ]
    
    return Div(
        Div(
            *[create_contact_card(item) for item in items],
            cls='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6'
        ),
        cls='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 mb-16'
    )
