"""Contact form component builder"""
from fasthtml.common import *
from pathlib import Path
import json


def load_validation_script(error_messages):
    """Load and populate the contact validation JavaScript with error messages"""
    script_path = Path(__file__).parent / 'contact_validation.js'
    with open(script_path, 'r', encoding='utf-8') as f:
        script_template = f.read()
    
    # Build the error messages object
    error_messages_json = json.dumps({
        'name': error_messages['name'],
        'email': error_messages['email'],
        'comment': error_messages['comment'],
        'consent': error_messages['consent']
    }, ensure_ascii=False)
    
    # Replace placeholder with actual error messages
    script = script_template.replace('ERROR_MESSAGES_PLACEHOLDER', error_messages_json)
    
    return script


def build_contact_form(contact):
    """Build the contact form section with all fields and validation"""
    
    # Handle both old and new data structures
    # New structure has 'form' key, old structure has fields at top level
    if 'form' in contact:
        form_data = contact['form']
        fields = form_data['fields']
        consent = form_data.get('consent', {})
        submit_label = form_data.get('submit_label', 'Отправить')
    else:
        fields = contact['fields']
        consent = contact.get('consent', {})
        submit_label = contact.get('submit', {}).get('label', 'Отправить')
    
    # Prepare error messages from contact data (with defaults if not present)
    error_messages = {
        'name': fields.get('name', {}).get('error', 'Пожалуйста, введите ваше имя'),
        'email': fields.get('email', {}).get('error', 'Пожалуйста, введите корректный email'),
        'comment': fields.get('message', fields.get('comment', {})).get('error', 'Пожалуйста, введите сообщение'),
        'consent': consent.get('error', 'Вы должны согласиться с условиями')
    }
    
    # Load validation script
    validation_script = load_validation_script(error_messages)
    
    return Section(
        Div(
            H2(contact['title']),
            P(contact['intro']),
            Form(
                Div(
                    Label(fields['name']['label'], fr='contact-name'),
                    Input(
                        type='text',
                        name='name',
                        id='contact-name',
                        placeholder=fields['name']['placeholder'],
                        required=True
                    ),
                    cls='form-group'
                ),
                Div(
                    Label(fields['email']['label'], fr='contact-email'),
                    Input(
                        type='email',
                        name='email',
                        id='contact-email',
                        placeholder=fields['email']['placeholder'],
                        required=True
                    ),
                    cls='form-group'
                ),
                Div(
                    Label(fields.get('message', fields.get('comment', {}))['label'], fr='contact-comment'),
                    Textarea(
                        name='comment',
                        id='contact-comment',
                        placeholder=fields.get('message', fields.get('comment', {}))['placeholder'],
                        rows=4,
                        required=True
                    ),
                    cls='form-group'
                ),
                Div(
                    Input(
                        type='checkbox',
                        name='consent',
                        id='contact-consent',
                        required=True
                    ),
                    Label(
                        consent['label_prefix'],
                        A(
                            consent['privacy_link_text'],
                            href=consent['privacy_link_href']
                        ),
                        fr='contact-consent'
                    ),
                    cls='form-group consent-row'
                ),
                Button(submit_label, type='submit', cls='btn btn-primary'),
                hx_post='/contact/submit',
                hx_target='#contact-status',
                hx_swap='innerHTML',
                novalidate=True,
                cls='contact-form'
            ),
            Div(id='contact-status', cls='contact-status'),
            Script(validation_script),
            cls='contact-form-content'
        ),
        cls='contact-form-section',
        id='contact-form'
    )
