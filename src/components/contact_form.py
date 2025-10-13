from fasthtml.common import *


def create_icon_svg_form(icon_type):
    """Create inline SVG icons for the contact form."""
    icons = {
        'message-circle': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>''',
        'send': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>''',
        'check-circle': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>''',
    }
    return NotStr(icons.get(icon_type, icons['message-circle']))


def create_contact_form(data=None):
    """
    Create modern contact form component.
    
    Args:
        data: Dictionary with form configuration:
            - title: Form title (default: "Send us a Message")
            - fields: Dictionary of field configurations
            - submit_label: Submit button text
            - submit_endpoint: Form submission endpoint
    """
    if data is None:
        data = {}
    
    # Get configuration
    title = data.get('title', 'Send us a Message')
    fields = data.get('fields', {})
    submit_label = data.get('submit_label', 'Send Message')
    submit_endpoint = data.get('submit_endpoint', '/contact/submit')
    consent = data.get('consent', {})
    
    # Field configurations with defaults
    name_field = fields.get('name', {})
    email_field = fields.get('email', {})
    phone_field = fields.get('phone', {})
    subject_field = fields.get('subject', {})
    message_field = fields.get('message', {})
    
    return Div(
        # Form header with icon
        Div(
            Div(
                Div(
                    create_icon_svg_form('message-circle'),
                    cls='w-6 h-6 text-indigo-600'
                ),
                cls='bg-indigo-100 p-2 rounded-lg'
            ),
            H2(title, cls='text-3xl'),
            cls='flex items-center gap-3 mb-6'
        ),
        
        # Form
        Form(
            # Name field
            Div(
                Label(
                    name_field.get('label', 'Full Name'),
                    ' *',
                    fr='contact-name',
                    cls='form-label'
                ),
                Input(
                    type='text',
                    name='name',
                    id='contact-name',
                    placeholder=name_field.get('placeholder', 'John Doe'),
                    required=True,
                    cls='form-input mt-2'
                ),
                cls='form-field'
            ),
            
            # Email field
            Div(
                Label(
                    email_field.get('label', 'Email Address'),
                    ' *',
                    fr='contact-email',
                    cls='form-label'
                ),
                Input(
                    type='email',
                    name='email',
                    id='contact-email',
                    placeholder=email_field.get('placeholder', 'john@example.com'),
                    required=True,
                    cls='form-input mt-2'
                ),
                cls='form-field'
            ),
            
            # Phone field (optional)
            Div(
                Label(
                    phone_field.get('label', 'Phone Number'),
                    fr='contact-phone',
                    cls='form-label'
                ),
                Input(
                    type='tel',
                    name='phone',
                    id='contact-phone',
                    placeholder=phone_field.get('placeholder', '+7 (123) 456-7890'),
                    cls='form-input mt-2'
                ),
                cls='form-field'
            ) if phone_field else None,
            
            # Subject field
            Div(
                Label(
                    subject_field.get('label', 'Subject'),
                    ' *',
                    fr='contact-subject',
                    cls='form-label'
                ),
                Input(
                    type='text',
                    name='subject',
                    id='contact-subject',
                    placeholder=subject_field.get('placeholder', 'How can we help you?'),
                    required=True,
                    cls='form-input mt-2'
                ),
                cls='form-field'
            ) if subject_field else None,
            
            # Message field
            Div(
                Label(
                    message_field.get('label', 'Message'),
                    ' *',
                    fr='contact-message',
                    cls='form-label'
                ),
                Textarea(
                    name='message',
                    id='contact-message',
                    placeholder=message_field.get('placeholder', 'Tell us more about your inquiry...'),
                    rows=6,
                    required=True,
                    cls='form-textarea mt-2'
                ),
                cls='form-field'
            ),
            
            # Consent checkbox (if provided)
            Div(
                Input(
                    type='checkbox',
                    name='consent',
                    id='contact-consent',
                    required=True,
                    cls='form-checkbox'
                ),
                Label(
                    consent.get('label_prefix', 'I agree to the '),
                    A(
                        consent.get('privacy_link_text', 'Privacy Policy'),
                        href=consent.get('privacy_link_href', '/privacy'),
                        cls='text-indigo-600 hover:text-indigo-700'
                    ),
                    fr='contact-consent',
                    cls='form-label-inline'
                ),
                cls='form-field-checkbox'
            ) if consent else None,
            
            # Submit button
            Button(
                Div(
                    create_icon_svg_form('send'),
                    cls='w-5 h-5'
                ),
                Span(submit_label),
                type='submit',
                cls='btn-submit w-full gap-2',
                id='contact-submit-btn'
            ),
            
            # Form status message
            Div(id='contact-status', cls='contact-status mt-4'),
            
            hx_post=submit_endpoint,
            hx_target='#contact-status',
            hx_swap='innerHTML',
            hx_indicator='#contact-submit-btn',
            cls='contact-form-modern space-y-6'
        ),
        
        # Add validation script
        Script("""
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form-modern');
    const submitBtn = document.getElementById('contact-submit-btn');
    
    if (!form || !submitBtn) return;
    
    // Handle HTMX events
    form.addEventListener('htmx:beforeRequest', function() {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Sending...</span>';
        submitBtn.classList.add('btn-loading');
    });
    
    form.addEventListener('htmx:afterRequest', function(evt) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = `
            <div class="w-5 h-5">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>
            </div>
            <span>Send Message</span>
        `;
        submitBtn.classList.remove('btn-loading');
        
        // If successful, reset form
        if (evt.detail.successful) {
            form.reset();
            
            // Auto-dismiss success message after 5 seconds
            setTimeout(function() {
                const status = document.getElementById('contact-status');
                if (status) {
                    status.style.transition = 'opacity 0.5s ease-out';
                    status.style.opacity = '0';
                    setTimeout(function() {
                        status.innerHTML = '';
                        status.style.opacity = '1';
                    }, 500);
                }
            }, 5000);
        }
    });
    
    // Real-time validation
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            if (this.classList.contains('error')) {
                validateField(this);
            }
        });
    });
    
    function validateField(field) {
        const value = field.value.trim();
        const isRequired = field.hasAttribute('required');
        
        // Remove previous error
        field.classList.remove('error');
        const errorMsg = field.parentNode.querySelector('.error-message');
        if (errorMsg) errorMsg.remove();
        
        // Check if empty and required
        if (isRequired && !value) {
            showError(field, 'This field is required');
            return false;
        }
        
        // Email validation
        if (field.type === 'email' && value) {
            const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
            if (!emailRegex.test(value)) {
                showError(field, 'Please enter a valid email address');
                return false;
            }
        }
        
        // Checkbox validation
        if (field.type === 'checkbox' && isRequired && !field.checked) {
            showError(field, 'You must agree to continue');
            return false;
        }
        
        return true;
    }
    
    function showError(field, message) {
        field.classList.add('error');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
    }
    
    // Validate on submit
    form.addEventListener('submit', function(e) {
        let isValid = true;
        inputs.forEach(input => {
            if (!validateField(input)) {
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            const firstError = form.querySelector('.error');
            if (firstError) firstError.focus();
        }
    });
});
        """),
        
        cls='contact-card p-8'
    )
