# Modern Contact Form Component Usage

## Overview
The `create_contact_form` component is a modern FastHTML implementation of a contact form with real-time validation, HTMX integration, and a clean UI inspired by React/Tailwind design patterns.

## Component Location
- **File**: `src/components/contact_form.py`
- **Function**: `create_contact_form(data=None)`

## Features
- ✅ Modern card-based design with icon header
- ✅ Real-time client-side validation
- ✅ HTMX-powered form submission (no page reload)
- ✅ Loading states with disabled button
- ✅ Success message with auto-dismiss
- ✅ Support for 5 fields: name, email, phone, subject, message
- ✅ Optional consent checkbox
- ✅ Inline SVG icons (message-circle, send, check-circle)
- ✅ Fully responsive design
- ✅ Smooth animations and transitions

## Usage

### Basic Usage
```python
from src.components import create_contact_form

# Use with default values
form = create_contact_form()

# Use with custom data
form_data = {
    'title': 'Send us a Message',
    'submit_label': 'Send Message',
    'submit_endpoint': '/contact/submit',
    'fields': {
        'name': {
            'label': 'Full Name',
            'placeholder': 'John Doe'
        },
        'email': {
            'label': 'Email Address',
            'placeholder': 'john@example.com'
        },
        # ... more fields
    },
    'consent': {
        'label_prefix': 'I agree to the ',
        'privacy_link_text': 'Privacy Policy',
        'privacy_link_href': '/privacy'
    }
}
form = create_contact_form(form_data)
```

### Integration in Contact Page
The component is integrated in `src/pages/contact/view.py`:

```python
from src.components import create_contact_form

def render():
    contact = get_contact_data()
    return (
        # ... header and info grid
        Section(
            Div(
                create_contact_form(contact.get('form')),
                cls='max-w-3xl mx-auto px-4 sm:px-6 lg:px-8'
            ),
            cls='contact-form-section py-16'
        ),
    )
```

## Data Structure

### YAML Configuration
Configure the form via `data/contact.yaml`:

```yaml
form:
  title: "Отправьте нам сообщение"
  submit_label: "Отправить сообщение"
  submit_endpoint: "/contact/submit"
  fields:
    name:
      label: "Полное имя"
      placeholder: "Иван Иванов"
    email:
      label: "Email адрес"
      placeholder: "ivan@example.com"
    phone:
      label: "Номер телефона"
      placeholder: "+7 (123) 456-7890"
    subject:
      label: "Тема"
      placeholder: "Как мы можем вам помочь?"
    message:
      label: "Сообщение"
      placeholder: "Расскажите подробнее о вашем запросе..."
  consent:
    label_prefix: "Настоящим подтверждаю, что я ознакомлен и согласен с "
    privacy_link_text: "политикой конфиденциальности"
    privacy_link_href: "/privacy"
```

## Form Fields

### Required Fields
- **Name** - Full name input (text)
- **Email** - Email address input with validation (email)
- **Message** - Multi-line message textarea (6 rows)

### Optional Fields
- **Phone** - Phone number input (tel)
- **Subject** - Subject line input (text)
- **Consent** - Privacy policy checkbox

## Server-Side Handling

### Route Configuration
The form submits to `/contact/submit` via HTMX POST:

```python
# src/routes/contact.py
@rt('/contact/submit')
def post(name: str, email: str, phone: str = "", subject: str = "", 
         message: str = "", consent: str = ""):
    # Process form data
    logging.info(f"Contact from: {name} ({email})")
    
    # Return success message
    return Div(
        # Success icon
        Div(...),
        H3("Thank you!"),
        P(f"Your message has been received, {name}."),
        cls='contact-success text-center py-6'
    )
```

## Validation

### Client-Side Validation
The form includes real-time JavaScript validation:

- **Required fields**: Checked on blur and submit
- **Email format**: Regex validation for valid email
- **Checkbox**: Must be checked if required
- **Error display**: Red border + error message below field
- **Auto-clear**: Errors clear when field becomes valid

### Validation Rules
```javascript
// Required field
if (isRequired && !value) {
    showError(field, 'This field is required');
}

// Email validation
if (field.type === 'email' && value) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(value)) {
        showError(field, 'Please enter a valid email address');
    }
}
```

## Styling

### CSS Classes
All styles are defined in `assets/styles/main.css` (lines 2826-3087):

#### Form Container
- `.contact-form-modern` - Main form wrapper
- `.space-y-6` - Vertical spacing between fields
- `.contact-card` - Card wrapper with padding

#### Form Elements
- `.form-field` - Field container
- `.form-label` - Field label
- `.form-input` - Text/email/tel inputs
- `.form-textarea` - Textarea element
- `.form-checkbox` - Checkbox input
- `.form-field-checkbox` - Checkbox container

#### Button
- `.btn-submit` - Submit button with gradient
- `.btn-loading` - Loading state
- Hover effects with transform and shadow

#### States
- `.error` - Error state for inputs
- `.error-message` - Error message text
- `.contact-success` - Success message container

### Color Scheme
- **Primary**: Indigo gradient (#6366f1 → #4f46e5)
- **Success**: Green gradient (#f0fdf4 → #dcfce7)
- **Error**: Red (#ef4444)
- **Border**: Gray (#d1d5db)
- **Focus**: Indigo ring (#6366f1 with opacity)

## Icons

### Available Icons
Inline SVG icons from lucide-react:

- **message-circle**: Form header icon
- **send**: Submit button icon
- **check-circle**: Success message icon

## Behavior

### Form Submission Flow
1. User fills out form
2. Client-side validation on blur/submit
3. If valid, HTMX sends POST to `/contact/submit`
4. Button shows "Sending..." and is disabled
5. Server processes and returns success HTML
6. Success message appears in `#contact-status`
7. Form resets automatically
8. Success message auto-dismisses after 5 seconds

### HTMX Integration
```html
<form 
    hx-post="/contact/submit"
    hx-target="#contact-status"
    hx-swap="innerHTML"
    hx-indicator="#contact-submit-btn">
```

## Responsive Design

### Breakpoints
- **Desktop** (> 768px): Full padding, large text
- **Tablet** (≤ 768px): Medium padding, medium text
- **Mobile** (≤ 480px): Small padding, compact button

### Mobile Optimizations
- Reduced font sizes
- Smaller padding
- Touch-friendly input sizes
- Optimized button size

## Customization

### Change Form Title
Edit `data/contact.yaml`:
```yaml
form:
  title: "Your Custom Title"
```

### Add/Remove Fields
Edit the component to conditionally render fields:
```python
# In contact_form.py
Div(...) if field_config else None
```

### Change Button Color
Edit `assets/styles/main.css`:
```css
.btn-submit {
    background: linear-gradient(135deg, #your-color 0%, #your-color-dark 100%);
}
```

### Customize Validation Messages
Edit the JavaScript in `contact_form.py`:
```javascript
showError(field, 'Your custom error message');
```

## Migration from Old Form

The old contact form (`src/pages/home/contact_form.py`) has been replaced. Key differences:

| Feature | Old Form | New Form |
|---------|----------|----------|
| Design | Basic HTML | Modern card with icons |
| Fields | 3 (name, email, comment) | 5 (name, email, phone, subject, message) |
| Validation | Separate JS file | Inline validation |
| Styling | Custom CSS | Tailwind-like utilities |
| Icons | None | Inline SVG icons |
| Success | Plain text | Animated card with icon |

## Files

### Created
- `src/components/contact_form.py` - Main component

### Modified
- `src/components/__init__.py` - Added export
- `src/pages/contact/view.py` - Integrated new form
- `data/contact.yaml` - Added form configuration
- `assets/styles/main.css` - Added 260+ lines of styles
- `src/routes/contact.py` - Updated to handle new fields

### Deprecated (can be removed)
- `src/pages/home/contact_form.py` - Old form builder
- `src/pages/home/contact_validation.js` - Old validation

## Testing

To test the form:
1. Navigate to `/contact`
2. Verify form renders with all fields
3. Test validation:
   - Leave required fields empty → See errors
   - Enter invalid email → See error
   - Uncheck consent → See error
4. Fill form correctly and submit
5. Verify success message appears
6. Verify form resets
7. Verify success auto-dismisses after 5s

## Troubleshooting

### Form not submitting
- Check HTMX is loaded
- Verify `/contact/submit` route exists
- Check browser console for errors

### Validation not working
- Check JavaScript is loaded
- Verify form has class `contact-form-modern`
- Check browser console for JS errors

### Styling issues
- Verify `main.css` is loaded
- Check for CSS conflicts
- Inspect elements in browser DevTools
