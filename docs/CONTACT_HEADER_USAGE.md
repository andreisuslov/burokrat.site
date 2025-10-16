# Contact Header Component Usage

## Overview
The `create_contact_header` component is a FastHTML implementation of a modern contact page header with gradient background, inspired by React/Tailwind design patterns.

## Component Location
- **File**: `src/components/contact_header.py`
- **Function**: `create_contact_header(data=None)`

## Usage

### Basic Usage
```python
from src.components import create_contact_header

# Use with default values
header = create_contact_header()

# Use with custom data
header_data = {
    'badge': 'Get In Touch',
    'title': 'Contact Us',
    'description': "Have questions? We'd love to hear from you."
}
header = create_contact_header(header_data)
```

### Integration in Contact Page
The component is already integrated in the contact page at `src/pages/contact/view.py`:

```python
from src.components import create_contact_header

def render():
    contact = get_contact_data()
    return (
        create_contact_header(contact.get('header')),
        # ... other sections
    )
```

## Data Structure
Configure the header via `data/contact.yaml`:

```yaml
header:
  badge: "Свяжитесь с нами"
  title: "Контакты"
  description: "Есть вопросы? Мы будем рады услышать вас. Отправьте нам сообщение, и мы ответим как можно скорее."
```

## Styling
The component uses Tailwind-like utility classes that are defined in `assets/styles/main.css`:
- Gradient background: `bg-gradient-to-br from-indigo-50 via-white to-purple-50`
- Badge styling: `bg-indigo-100 text-indigo-700 rounded-full`
- Responsive padding and typography
- Mobile-responsive breakpoints

## Features
- ✅ Gradient background (indigo to purple)
- ✅ Centered layout with max-width container
- ✅ Badge component for tagline
- ✅ Large heading (text-5xl)
- ✅ Descriptive subtitle
- ✅ Fully responsive design
- ✅ Matches original React component design

## Customization
You can customize the appearance by:
1. Modifying the data in `contact.yaml`
2. Adjusting utility classes in `main.css`
3. Passing different data to the component function
