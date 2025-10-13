from fasthtml.common import *


def create_values(data):
    """Create values section with value cards grid."""
    values = data.get('values', {})
    
    return Section(
        H2(values.get('heading', 'Наши Ценности')),
        Div(
            *[Div(
                H4(value.get('title', '')),
                P(value.get('description', '')),
                cls='value-card'
            ) for value in values.get('items', [])],
            cls='values-grid'
        ),
        cls='values-section'
    )
