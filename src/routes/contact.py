from fasthtml.common import *
from src.config import get_contact_data
from src.components import Layout
from src.pages.contact.view import render as render_contact
import logging

def register_contact_routes(rt):
    """Register contact form routes."""
    
    @rt('/contact')
    def get():
        """Render the standalone contact page."""
        logging.info("📧 Serving contact page (/contact)")
        data = get_contact_data()
        page_title = data.get('page_title', 'Контакты - Бюрократ')
        return Layout(page_title, *render_contact())
    
    @rt('/contact/submit')
    def post(name: str, email: str, phone: str = "", subject: str = "", message: str = "", comment: str = "", consent: str = ""):
        # Process form submission (e.g., send email, store in DB) - omitted here.
        # Support both old form (comment) and new form (message, subject, phone)
        actual_message = message or comment
        logging.info(f"✉️  Processing contact form submission from: {name} ({email})")
        logging.info(f"   Subject: {subject}, Phone: {phone}")
        logging.info(f"   Message: {actual_message[:50]}...")
        
        data = get_contact_data()
        title = data.get('success', {}).get('title', 'Спасибо!')
        msg_tpl = data.get('success', {}).get('message_template', 'Ваше сообщение получено, {name}. Мы свяжемся с вами в ближайшее время.')
        success_message = msg_tpl.format(name=name)
        
        return Div(
            Div(
                Div(
                    NotStr('''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'''),
                    cls='w-6 h-6 text-green-600'
                ),
                cls='bg-green-100 p-3 rounded-full mb-4 inline-flex'
            ),
            H3(title, cls='text-2xl mb-2 text-green-800'),
            P(success_message, cls='text-gray-600'),
            cls='contact-success text-center py-6'
        )
