from fasthtml.common import *
from src.config import get_data
from src.utils.phone_formatter import format_phone_number
from src.pages.home.contact_form import build_contact_form

def create_service_card(item):
    """Create a service card component."""
    # Get image from YAML data or use default fallback
    image_src = item.get('image', '/assets/images/icon.png')
    
    # If the provided image is an SVG, render it as a mask so we can color it with CSS
    is_svg = str(image_src).lower().endswith('.svg')
    image_node = (
        Span(
            cls='service-icon',
            role='img',
            aria_label=item['label'],
            style=(
                f"background-color: var(--primary-color); "
                f"-webkit-mask: url('{image_src}') no-repeat center / contain; "
                f"mask: url('{image_src}') no-repeat center / contain; "
                f"width: 120px; height: 120px; display: inline-block;"
            )
        ) if is_svg else Img(src=image_src, alt=item['label'])
    )
    
    return A(
        Div(
            image_node,
            cls='service-card-image'
        ),
        Div(
            H3(item['label']),
            P(item.get('description', '')) if item.get('description') else None,
            cls='service-card-content'
        ),
        href=item['url'],
        cls='service-card',
        draggable='false'
    )

def create_company_items(items):
    """Render company info list with optional grouped nested items from YAML."""
    if not items:
        return None
    list_items = []
    for it in items:
        if isinstance(it, dict):
            if 'label' in it:
                list_items.append(Li(it['label']))
            else:
                # Use first non-'items' key as a group title (e.g., 'for_clients')
                keys = [k for k in it.keys() if k != 'items']
                if keys:
                    title_key = keys[0]
                    title_val = it.get(title_key, '')
                    nested = it.get('items', [])
                    nested_list = None
                    if isinstance(nested, list) and nested:
                        nested_list = Ul(
                            *[
                                (lambda _k, _v: Li(A(str(_v), href=f"/clients#{_k}", target='_self')))(
                                    next(iter(d.keys())), next(iter(d.values()))
                                )
                                for d in nested if isinstance(d, dict) and d
                            ]
                        )
                    # Link the group title to /clients and add a class for consistent sizing
                    list_items.append(Li(A(Strong(title_val), href='/clients', target='_self', cls='company-group-title'), nested_list))
        else:
            list_items.append(Li(str(it)))
    return Ul(*list_items)

def create_social_media_section(links):
    """Render social/messenger links if provided."""
    if not links:
        return None
    items = []
    for link in links:
        label = link.get('label', '')
        url = link.get('url', '#')
        kind = label.lower()
        icon_class = 'telegram' if 'teleg' in kind else ('whatsapp' if 'whats' in kind else 'external')
        items.append(
            Li(
                A(
                    Span(label, cls='sr-only'),
                    href=url,
                    target='_blank',
                    cls=f'social-icon {icon_class}',
                    aria_label=label
                )
            )
        )
    return Div(
        H3('Мессенджеры'),
        Ul(*items, cls='social-media-list'),
        cls='social-media'
    )

def create_contact_info():
    """Create contact information section with enhanced layout including company info and social media."""
    data = get_data()
    contact_data = data.get('contact_info', {})
    company_info = data.get('company_info', {})
    
    return Div(
        # Company Info Section
        Div(
            H3(f"Компания \"{company_info.get('name', 'Бюрократ')}\""),
            create_company_items(company_info.get('items', [])),
            cls='company-info'
        ),
        # Contact Grid
        Div(
            # Left column - Phones
            Div(
                H3(contact_data.get('sections', {}).get('phones', {}).get('title', 'Телефоны')),
                Ul(*[
                    Li(
                        A(format_phone_number(phone)[0], href=f"tel:{format_phone_number(phone)[1]}"),
                        Span(f" ({format_phone_number(phone)[2]})", cls='phone-note') if format_phone_number(phone)[2] else None
                    )
                    for phone in company_info.get('phones', [])
                ]),
                cls='contact-phones'
            ),
            # Right column - Addresses
            Div(
                H3(contact_data.get('sections', {}).get('addresses', {}).get('title', 'Адреса')),
                Div(
                    H4(contact_data.get('sections', {}).get('addresses', {}).get('store', {}).get('label', '🏪 Магазин')),
                    P(
                        A(company_info['addresses']['socialist_location']['address'],
                          href=f"https://www.google.com/maps/search/?api=1&query={company_info['addresses']['socialist_location']['address'].replace(' ', '+')}",
                          target='_blank')
                    ),
                    P(Strong(contact_data.get('sections', {}).get('addresses', {}).get('store', {}).get('working_hours_label', 'Часы работы: ')), 
                      company_info['addresses']['socialist_location']['working_hours']['monday']),
                    cls='location-info'
                ),
                Div(
                    H4(contact_data.get('sections', {}).get('addresses', {}).get('office', {}).get('label', '🏢 Офис')),
                    P(
                        A(company_info['addresses']['builders_location']['address'],
                          href=f"https://www.google.com/maps/search/?api=1&query={company_info['addresses']['builders_location']['address'].replace(' ', '+')}",
                          target='_blank')
                    ),
                    P(Strong(contact_data.get('sections', {}).get('addresses', {}).get('office', {}).get('working_hours_label', 'Часы работы: ')), 
                      company_info['addresses']['builders_location']['working_hours']['monday']),
                    cls='location-info'
                ),
                cls='contact-addresses'
            ),
            cls='contact-info-grid'
        ),
        # Social Media Section
        create_social_media_section(company_info.get('social_media_links', [])),
        cls='contact-info-container'
    )

def create_contact(data):
    """Create the contact section component."""
    return build_contact_form(data)
