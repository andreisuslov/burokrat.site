from fasthtml.common import *
from src.components.ui import create_404_page
from src.components import Layout
import logging


def register_404_handler(rt):
    """Register 404 error handler."""
    
    @rt('/404')
    def get():
        logging.info("🚫 Serving 404 page")
        return Layout(
            '404 - Page Not Found',
            Main(
                create_404_page(),
                cls='error-404-page'
            )
        )
