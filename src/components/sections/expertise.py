from fasthtml.common import *


def create_expertise(data):
    """Create expertise section with items grid."""
    expertise = data.get('expertise', {})
    
    return Section(
        H2(expertise.get('heading', 'Экспертиза')),
        Div(
            Div(
                *[Div(
                    H3(f"{item.get('icon', '')} {item.get('title', '')}"),
                    P(item.get('description', '')),
                    cls='expertise-card'
                ) for item in expertise.get('items', [])],
                cls='expertise-grid'
            )
        ),
        cls='expertise-section'
    )
