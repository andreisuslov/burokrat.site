"""
Burokrat.site - Main Application Entry Point
A modular FastHTML application for a Russian seals and stamps company.
"""

from fasthtml.common import *
from src.config import load_page_data
from src.routes import register_all_routes

# Initialize FastHTML app
app, rt = fast_app(
    hdrs=(
        Link(rel='stylesheet', href='/assets/styles/main.css'),
        Script(src='https://unpkg.com/htmx.org@1.9.10'),
    ),
    live=True
)

# Load configuration data
load_page_data()

# Register all routes
register_all_routes(rt)

if __name__ == '__main__':
    serve(port=8080)
