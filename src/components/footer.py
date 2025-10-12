from fasthtml.common import *
from src.config import get_data
from src.utils.phone_formatter import format_phone_number
from src.components.contact_info import create_company_items, create_social_media_section

def create_footer():
    """Create footer component with contact information."""
    data = get_data()
    footer_data = data.get('footer', {})
    # Find the first simple label item (e.g., «Работаем с 1998 года») to show inside the gold box
    company_items = data['company_info'].get('items', [])
    first_label_item = None
    remaining_items = []
    for it in company_items:
        if first_label_item is None and isinstance(it, dict) and 'label' in it:
            first_label_item = it
            continue
        remaining_items.append(it)

    # Filter out nested client links (e.g., Доставка/Оплата/Гарантия) from the footer
    # Keep the group title (Клиентам) but remove its nested items for a cleaner footer
    filtered_company_items = []
    for it in remaining_items:
        if isinstance(it, dict) and 'for_clients' in it:
            filtered_company_items.append({'for_clients': it.get('for_clients')})
        else:
            filtered_company_items.append(it)

    return [
        Div(
            Div(
                H3('Контактная информация'),
                Div(
                    P(f"Компания \"{data['company_info']['name']}\""),
                    Ul(*( [Li(first_label_item['label'])] if first_label_item else [] )),
                    cls='footer-company-highlight'
                ),
                create_company_items(filtered_company_items),
                create_social_media_section(data['company_info'].get('social_media_links', [])),
                cls='footer-section'
            ),
            Div(
                H4(footer_data.get('sections', {}).get('phones', {}).get('title', 'Телефоны')),
                Ul(*[
                    Li(
                        A(format_phone_number(phone)[0], href=f"tel:{format_phone_number(phone)[1]}"),
                        Span(f" ({format_phone_number(phone)[2]})", cls='phone-note') if format_phone_number(phone)[2] else None
                    )
                    for phone in data['company_info']['phones']
                ], cls='footer-phones'),
                cls='footer-section'
            ),
            Div(
                H4(footer_data.get('sections', {}).get('email', {}).get('title', 'Электронная почта')),
                Ul(*[Li(A(email, href=f"mailto:{email}")) 
                     for email in data['company_info']['emails']], cls='footer-emails'),
                cls='footer-section'
            ),
            Div(
                H4(footer_data.get('sections', {}).get('addresses', {}).get('title', 'Адреса')),
                Div(
                    P(
                        Strong('🏬 ', footer_data.get('sections', {}).get('addresses', {}).get('store_label', 'Магазин: '), cls='location-label'),
                        A(data['company_info']['addresses']['socialist_location']['address'],
                          href=f"https://www.google.com/maps/search/?api=1&query={data['company_info']['addresses']['socialist_location']['address'].replace(' ', '+')}",
                          target='_blank')
                    ),
                    P(f"{footer_data.get('sections', {}).get('addresses', {}).get('working_hours_label', 'Время работы: ')}{data['company_info']['addresses']['socialist_location']['working_hours']['monday']}"),
                    cls='location'
                ),
                Div(
                    P(
                        Strong('🏢 ', footer_data.get('sections', {}).get('addresses', {}).get('office_label', 'Офис: '), cls='location-label'),
                        A(data['company_info']['addresses']['builders_location']['address'],
                          href=f"https://www.google.com/maps/search/?api=1&query={data['company_info']['addresses']['builders_location']['address'].replace(' ', '+')}",
                          target='_blank')
                    ),
                    P(f"{footer_data.get('sections', {}).get('addresses', {}).get('working_hours_label', 'Время работы: ')}{data['company_info']['addresses']['builders_location']['working_hours']['monday']}"),
                    cls='location'
                ),
                cls='footer-section'
            ),
            cls='footer-content'
        ),
        P(
            f"© {footer_data.get('copyright', {}).get('year', '2025')} ",
            data['company_info']['name'],
            footer_data.get('copyright', {}).get('separator', ' · '),
            A(footer_data.get('copyright', {}).get('privacy_link', {}).get('text', 'Политика в отношении обработки персональных данных'), 
              href=footer_data.get('copyright', {}).get('privacy_link', {}).get('url', '/privacy-statemnt'), 
              cls='privacy-link'),
            # Optional agreement link if provided in data
            (footer_data.get('copyright', {}).get('separator', ' · ')
             if footer_data.get('copyright', {}).get('agreement_link') else None),
            (A(
                footer_data.get('copyright', {}).get('agreement_link', {}).get('text', 'Пользовательское соглашение'),
                href=footer_data.get('copyright', {}).get('agreement_link', {}).get('url', '/agreement'),
                cls='privacy-link'
             ) if footer_data.get('copyright', {}).get('agreement_link') else None),
            cls='copyright'
        )
    ]
