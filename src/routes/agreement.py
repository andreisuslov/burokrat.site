from fasthtml.common import *
from src.components import Layout
from src.config import get_agreement_data
from src.pages.agreement.view import render as render_agreement


def register_agreement_route(rt):
    """Register agreement page route (/agreement)."""

    @rt('/agreement')
    def get():
        data = get_agreement_data()
        return Layout(
            data.get('title', 'Пользовательское соглашение'),
            *render_agreement()
        )
