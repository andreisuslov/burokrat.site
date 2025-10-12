from fasthtml.common import *
from src.components import Layout
from src.config import get_privacy_data
from src.pages.privacy.view import render as render_privacy


def register_privacy_route(rt):
    """Register privacy statement page route."""

    # Primary route
    @rt('/privacy-statement')
    def get():
        data = get_privacy_data()
        return Layout(
            data['title'],
            *render_privacy()
        )

    # Alias route for requested slug (typo kept intentionally)
    @rt('/privacy-statemnt')
    def get_alias():
        return get()

    # Simple alias for shorter path
    @rt('/privacy')
    def get_privacy_root():
        return get()
