from fasthtml.common import *


def create_our_history(data):
    """Create our history section with story and stats."""
    story = data.get('story', {})
    stats = data.get('stats', [])
    
    return Section(
        Div(
            Div(
                H2(story.get('heading', 'Наша История')),
                *[P(paragraph) for paragraph in story.get('paragraphs', [])],
                cls='about-text'
            ),
            Div(
                *[Div(
                    H3(stat.get('value', '')),
                    P(stat.get('label', '')),
                    cls='stat-card'
                ) for stat in stats],
                cls='stats-grid'
            ),
            cls='about-content-grid'
        ),
        cls='about-story-section'
    )
