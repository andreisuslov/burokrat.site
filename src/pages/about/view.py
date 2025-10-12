from fasthtml.common import *
from src.config import get_about_data


def render():
    """Render main content for the About page."""
    data = get_about_data()

    return (
        # Hero Section
        Section(
            Div(
                H1(data['hero']['heading']),
                P(data['hero']['subtitle']),
                cls='hero'
            ),
            cls='hero-section'
        ),

        # Family Story Section
        Section(
            Div(
                Div(
                    H2(data['story']['heading']),
                    *[P(paragraph) for paragraph in data['story']['paragraphs']],
                    cls='about-text'
                ),
                Div(
                    *[Div(
                        H3(stat['value']),
                        P(stat['label']),
                        cls='stat-card'
                    ) for stat in data['stats']],
                    cls='stats-grid'
                ),
                cls='about-content-grid'
            ),
            cls='about-story-section'
        ),

        # Expertise Section
        Section(
            H2(data['expertise']['heading']),
            Div(
                Div(
                    *[Div(
                        H3(f"{item['icon']} {item['title']}"),
                        P(item['description']),
                        cls='expertise-card'
                    ) for item in data['expertise']['items']],
                    cls='expertise-grid'
                )
            ),
            cls='expertise-section'
        ),

        # Values Section
        Section(
            H2(data['values']['heading']),
            Div(
                *[Div(
                    H4(value['title']),
                    P(value['description']),
                    cls='value-card'
                ) for value in data['values']['items']],
                cls='values-grid'
            ),
            cls='values-section'
        ),

        # Locations Section
        Section(
            H2(data['locations']['heading']),
            P(data['locations']['subtitle'], cls='section-subtitle'),
            Div(
                *[Div(
                    H3(f"{office['icon']} {office['name']}"),
                    P(Strong(office['address'])),
                    P(office['description']),
                    P(Strong('Пн-Пт: '), office['hours']['weekdays']),
                    P(Strong('Сб-Вс: '), office['hours']['weekend']),
                    A('Открыть на карте', 
                      href=f"https://www.google.com/maps/search/?api=1&query={office['maps_query']}",
                      target='_blank',
                      cls='btn btn-primary'),
                    cls='location-card-about'
                ) for office in data['locations']['offices']],
                cls='locations-grid-about'
            ),
            cls='locations-section-about'
        ),

        # CTA Section
        Section(
            Div(
                H2(data['cta']['heading']),
                P(data['cta']['description']),
                Div(
                    *[A(btn['label'], href=btn['url'], cls=f"btn btn-{btn['type']}") 
                      for btn in data['cta']['buttons']],
                    cls='cta-buttons'
                ),
                cls='cta-content'
            ),
            cls='cta-section'
        ),
    )
