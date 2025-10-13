from fasthtml.common import *
from src.components import Layout
from src.config import get_privacy_data
from src.pages.privacy.view import render as render_privacy
import logging


def register_privacy_route(rt):
    """Register privacy statement page route."""

    # Primary route
    @rt('/privacy-statement')
    def get():
        logging.info("🔒 Serving privacy statement page (/privacy-statement)")
        data = get_privacy_data()
        return Layout(
            data['title'],
            *render_privacy()
        )

    # Alias route for requested slug (typo kept intentionally)
    @rt('/privacy-statemnt')
    def get_alias():
        logging.info("🔒 Redirecting from /privacy-statemnt alias")
        return get()

    # Simple alias for shorter path
    @rt('/privacy')
    def get_privacy_root():
        logging.info("🔒 Redirecting from /privacy alias")
        return get()
