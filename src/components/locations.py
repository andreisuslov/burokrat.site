from fasthtml.common import *


def create_locations(data):
    """Create locations section with office cards."""
    locations = data.get('locations', {})
    
    return Section(
        H2(locations.get('heading', 'Наши офисы')),
        P(locations.get('subtitle', ''), cls='section-subtitle'),
        Div(
            *[Div(
                H3(f"{office.get('icon', '')} {office.get('name', '')}"),
                P(Strong(office.get('address', ''))),
                P(office.get('description', '')),
                P(Strong('Пн-Пт: '), office.get('hours', {}).get('weekdays', '')),
                P(Strong('Сб-Вс: '), office.get('hours', {}).get('weekend', '')),
                A('Открыть на карте', 
                  href=f"https://www.google.com/maps/search/?api=1&query={office.get('maps_query', '')}",
                  target='_blank',
                  cls='btn btn-primary'),
                cls='location-card-about'
            ) for office in locations.get('offices', [])],
            cls='locations-grid-about'
        ),
        cls='locations-section-about'
    )
