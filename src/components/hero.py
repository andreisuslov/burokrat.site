from fasthtml.common import *


def create_hero(data):
    """Create modern hero section with image and stats."""
    return Section(
        Div(
            Div(
                # Left content column
                Div(
                    # Badge
                    Span(data.get('badge', '✨ Качество и надёжность'), cls='badge'),
                    
                    # Main heading with highlight
                    H1(
                        data.get('title', 'Печати и штампы'), ' ',
                        Span(data.get('highlight', 'для вашего бизнеса'), cls='highlight')
                    ),
                    
                    # Subtitle
                    P(data.get('subtitle', 'Профессиональное изготовление печатей и штампов'), cls='subtitle'),
                    
                    # Button group
                    Div(
                        A(
                            'Наши услуги',
                            href='#services-section',
                            cls='btn btn-primary'
                        ),
                        A(
                            'Связаться с нами',
                            href='#contact-form',
                            cls='btn btn-outline'
                        ),
                        cls='button-group'
                    ),
                    
                    # Stats group
                    Div(
                        *[
                            Div(
                                Div(stat.get('number', ''), cls='stat-number'),
                                Div(stat.get('label', ''), cls='stat-label'),
                            )
                            for stat in data.get('stats', [
                                {'number': '20+', 'label': 'лет опыта'},
                                {'number': '5000+', 'label': 'клиентов'},
                                {'number': '24ч', 'label': 'срочное изготовление'}
                            ])
                        ],
                        cls='stats-group'
                    ),
                    
                    cls='content-column'
                ),
                
                # Right image column
                Div(
                    Div(cls='image-glow'),
                    Img(
                        src=data.get('image', '/assets/images/engraving.svg'),
                        alt='Печати и штампы',
                        cls='hero-image'
                    ),
                    cls='image-column'
                ),
                
                cls='hero-grid'
            ),
            cls='container'
        ),
        cls='section hero-section'
    )
