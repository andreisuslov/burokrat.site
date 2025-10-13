from fasthtml.common import *


def create_cta(data):
    """Create call-to-action section with heading, description, and buttons."""
    cta = data.get('cta', {})
    
    return Section(
        Div(
            H2(cta.get('heading', '')),
            P(cta.get('description', '')),
            Div(
                *[A(btn.get('label', ''), href=btn.get('url', ''), cls=f"btn btn-{btn.get('type', 'primary')}") 
                  for btn in cta.get('buttons', [])],
                cls='cta-buttons'
            ),
            cls='cta-content'
        ),
        cls='cta-section'
    )
