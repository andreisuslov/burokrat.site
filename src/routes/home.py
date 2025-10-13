from fasthtml.common import *
from src.config import get_data
from src.components import Layout
from src.pages.home.view import render as render_home
import logging


def register_home_route(rt):
    """Register home page route."""

    @rt('/')
    def get():
        logging.info("🏠 Serving home page (/)")
        data = get_data()
        return Layout(
            data['title'],
            *render_home()
        )
