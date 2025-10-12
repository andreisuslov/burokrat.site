from fasthtml.common import *
from src.config import get_contact_data
from src.components import Layout
from src.pages.contact.view import render as render_contact

def register_contact_routes(rt):
    """Register contact form routes."""
    
    @rt('/contact')
    def get():
        """Render the standalone contact page."""
        data = get_contact_data()
        page_title = data.get('page_title', 'Контакты - Бюрократ')
        return Layout(page_title, *render_contact())
    
    @rt('/contact/submit')
    def post(name: str, email: str, comment: str, consent: str = ""):
        # Process form submission (e.g., send email, store in DB) - omitted here.
        data = get_contact_data()
        title = data.get('success', {}).get('title', 'Спасибо!')
        msg_tpl = data.get('success', {}).get('message_template', 'Ваше сообщение получено, {name}.')
        message = msg_tpl.format(name=name)
        return Div(
            H3(title),
            P(message),
            cls='contact-success'
        )
