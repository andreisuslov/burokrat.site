from fasthtml.common import *
from src.components import Layout
from src.config import get_about_data
from src.pages.about.view import render as render_about
import logging


def register_about_route(rt):
    """Register about us page route."""

    @rt('/about')
    def get():
        logging.info("ℹ️  Serving about page (/about)")
        data = get_about_data()
        return Layout(
            data['title'],
            *render_about()
        )
