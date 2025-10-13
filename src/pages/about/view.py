from fasthtml.common import *
from src.config import get_about_data
from src.components import create_our_history, create_expertise, create_locations, create_cta, create_values


def render():
    """Render main content for the About page."""
    data = get_about_data()

    return (
        create_our_history(data),
        create_expertise(data),
        create_values(data),
        create_locations(data),
        create_cta(data),
    )
