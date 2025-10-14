from fasthtml.common import *
from src.config import get_contact_data
from src.components import Layout
from src.pages.contact.view import render as render_contact
from src.services.email_service import get_email_service
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
    def post(name: str, email: str, phone: str = "", subject: str = "", message: str = "", comment: str = "", company: str = "", consent: str = ""):
        # Support both old form (comment) and new form (message, subject, phone)
        actual_message = message or comment
        logging.info(f"✉️  Processing contact form submission from: {name} ({email})")
        logging.info(f"   Subject: {subject}, Phone: {phone}")
        logging.info(f"   Message: {actual_message[:50]}...")
        
        # Prepare form data for email
        form_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': actual_message,
            'company': company
        }
        
        # Send email via SendGrid
        email_service = get_email_service()
        success, error_message = email_service.send_contact_form_email(form_data)
        
        data = get_contact_data()
        
        if success:
            # Success response
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
        else:
            # Error response
            error_title = data.get('error', {}).get('title', 'Ошибка')
            error_msg_tpl = data.get('error', {}).get('message', 'Не удалось отправить сообщение. Пожалуйста, попробуйте позже или свяжитесь с нами по телефону.')
            
            return Div(
                Div(
                    Div(
                        NotStr('''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'''),
                        cls='w-6 h-6 text-red-600'
                    ),
                    cls='bg-red-100 p-3 rounded-full mb-4 inline-flex'
                ),
                H3(error_title, cls='text-2xl mb-2 text-red-800'),
                P(error_msg_tpl, cls='text-gray-600'),
                cls='contact-error text-center py-6'
            )
