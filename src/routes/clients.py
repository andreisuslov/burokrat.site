from fasthtml.common import *
from src.components import Layout
from src.config import get_clients_data
from src.pages.clients.view import render as render_clients


def register_clients_route(rt):
    """Register clients page route (/clients)."""

    @rt('/clients')
    def get():
        data = get_clients_data()
        return Layout(
            data['title'],
            *render_clients()
        )
