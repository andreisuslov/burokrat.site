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
    
    # Prepare error messages from contact data
    error_messages = {
        'name': contact['fields']['name']['error'],
        'email': contact['fields']['email']['error'],
        'comment': contact['fields']['comment']['error'],
        'consent': contact['consent']['error']
    }
    
    # Load validation script
    validation_script = load_validation_script(error_messages)
    
    return Section(
        Div(
            H2(contact['title']),
            P(contact['intro']),
            Form(
                Div(
                    Label(contact['fields']['name']['label'], fr='contact-name'),
                    Input(
                        type='text',
                        name='name',
                        id='contact-name',
                        placeholder=contact['fields']['name']['placeholder'],
                        required=True
                    ),
                    cls='form-group'
                ),
                Div(
                    Label(contact['fields']['email']['label'], fr='contact-email'),
                    Input(
                        type='email',
                        name='email',
                        id='contact-email',
                        placeholder=contact['fields']['email']['placeholder'],
                        required=True
                    ),
                    cls='form-group'
                ),
                Div(
                    Label(contact['fields']['comment']['label'], fr='contact-comment'),
                    Textarea(
                        name='comment',
                        id='contact-comment',
                        placeholder=contact['fields']['comment']['placeholder'],
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
                        contact['consent']['label_prefix'],
                        A(
                            contact['consent']['privacy_link_text'],
                            href=contact['consent']['privacy_link_href']
                        ),
                        fr='contact-consent'
                    ),
                    cls='form-group consent-row'
                ),
                Button(contact['submit']['label'], type='submit', cls='btn btn-primary'),
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
