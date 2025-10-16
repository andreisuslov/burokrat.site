# Contact Page Components Usage

This document describes the modern contact page components created in FastHTML, inspired by React/Tailwind design patterns.

## Components Overview

### 1. Contact Header (`create_contact_header`)
A gradient header section with badge, title, and description.

**Location**: `src/components/contact_header.py`

**Features**:
- Gradient background (indigo → white → purple)
- Centered badge with custom text
- Large heading (text-5xl)
- Descriptive subtitle
- Fully responsive

### 2. Contact Info Grid (`create_contact_info_grid`)
A responsive grid of contact information cards with icons.

**Location**: `src/components/contact_info_grid.py`

**Features**:
- 4-column responsive grid (1 col mobile, 2 tablet, 4 desktop)
- Card-based design with hover effects
- SVG icons (map-pin, phone, clock, mail)
- Customizable colors
- Optional clickable links
- Negative top margin for overlap effect

### 3. Contact Form (`create_contact_form`)
A modern contact form with real-time validation and HTMX integration.

**Location**: `src/components/contact_form.py`

**Features**:
- Card-based design with icon header
- 5 fields: name, email, phone, subject, message
- Real-time client-side validation
- HTMX-powered submission (no page reload)
- Loading states and success animations
- Optional consent checkbox
- Auto-dismiss success message

## Complete Integration Example

### Contact Page Structure
```python
# src/pages/contact/view.py
from fasthtml.common import *
from src.config import get_contact_data
from src.components import (
    create_contact_header, 
    create_contact_info_grid,
    create_contact_form
)

def render():
    contact = get_contact_data()
    
    return (
        # 1. Header with gradient background
        create_contact_header(contact.get('header')),
        
        # 2. Info grid (overlaps header with -mt-8)
        create_contact_info_grid(contact.get('info_grid')),
        
        # 3. Modern contact form
        Section(
            Div(
                create_contact_form(contact.get('form')),
                cls='max-w-3xl mx-auto px-4 sm:px-6 lg:px-8'
            ),
            cls='contact-form-section py-16'
        ),
        
        # 4. Additional contact info
        Section(
            H2('Контактная информация'),
            create_contact_info(),
            cls='contact-info-section'
        ),
    )
```

### YAML Configuration
```yaml
# data/contact.yaml

# Header configuration
header:
  badge: "Свяжитесь с нами"
  title: "Контакты"
  description: "Есть вопросы? Мы будем рады услышать вас."

# Info grid configuration
info_grid:
  - icon: "map-pin"
    title: "Офис (Строителей)"
    content: "Строителей проспект, 4\nг. Барнаул, Алтайский край"
    color: "bg-indigo-100 text-indigo-600"
    link: "https://www.google.com/maps/search/?api=1&query=..."
  
  - icon: "map-pin"
    title: "Магазин (Социалистический)"
    content: "Социалистический проспект, 109\nг. Барнаул"
    color: "bg-blue-100 text-blue-600"
    link: "https://maps.google.com/..."
  
  - icon: "phone"
    title: "Позвоните нам"
    content: "+7 (3852) 62-82-82\n+7 (3852) 25-14-91"
    color: "bg-green-100 text-green-600"
  
  - icon: "clock"
    title: "Часы работы"
    content: "Понедельник - Воскресенье\n09:30 - 18:30"
    color: "bg-purple-100 text-purple-600"

# Form configuration
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

## Visual Layout

```
┌─────────────────────────────────────────────────┐
│          GRADIENT HEADER SECTION                │
│  ┌──────────────────────────────────┐          │
│  │  [Badge: "Свяжитесь с нами"]     │          │
│  │                                   │          │
│  │         Контакты (H1)            │          │
│  │                                   │          │
│  │  Есть вопросы? Мы будем рады...  │          │
│  └──────────────────────────────────┘          │
└─────────────────────────────────────────────────┘
        │
        │ (overlaps with -mt-8)
        ▼
┌─────────────────────────────────────────────────┐
│          CONTACT INFO GRID                      │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐       │
│  │ 📍   │  │ 📍   │  │ 📞   │  │ 🕐   │       │
│  │Office│  │Store │  │Phone │  │Hours │       │
│  │      │  │      │  │      │  │      │       │
│  └──────┘  └──────┘  └──────┘  └──────┘       │
└─────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────┐
│          CONTACT FORM CARD                      │
│  ┌──────────────────────────────────┐          │
│  │ 💬 Отправьте нам сообщение       │          │
│  │                                   │          │
│  │  [Name Input]                    │          │
│  │  [Email Input]                   │          │
│  │  [Phone Input]                   │          │
│  │  [Subject Input]                 │          │
│  │  [Message Textarea]              │          │
│  │  ☑ Privacy consent               │          │
│  │                                   │          │
│  │  [📤 Send Message Button]        │          │
│  └──────────────────────────────────┘          │
└─────────────────────────────────────────────────┘
```

## Styling

All styles are defined in `assets/styles/main.css`:

### Contact Header Styles
- Lines 2523-2648: Gradient backgrounds, typography, spacing
- Responsive breakpoints for mobile/tablet

### Contact Info Grid Styles
- Lines 2650-2824: Card styles, grid layout, colors
- Hover effects and transitions
- Responsive grid columns

### Contact Form Styles
- Lines 2826-3087: Form inputs, buttons, validation states
- Animations for errors and success
- Gradient button with hover effects
- Responsive adjustments

## Color Schemes

### Available Icon Colors
- **Indigo**: `bg-indigo-100 text-indigo-600`
- **Blue**: `bg-blue-100 text-blue-600`
- **Green**: `bg-green-100 text-green-600`
- **Purple**: `bg-purple-100 text-purple-600`
- **Orange**: `bg-orange-100 text-orange-600`

## Icons

Available SVG icons (inline, from lucide-react):

### Info Grid Icons
- `map-pin` - Location marker
- `phone` - Phone handset
- `clock` - Clock face
- `mail` - Envelope

### Form Icons
- `message-circle` - Form header icon
- `send` - Submit button icon
- `check-circle` - Success message icon

## Responsive Behavior

### Mobile (< 768px)
- Header: Smaller text sizes, reduced padding
- Grid: 1 column, reduced spacing
- Form: Compact padding, smaller inputs

### Tablet (768px - 1023px)
- Header: Medium text sizes
- Grid: 2 columns
- Form: Medium padding

### Desktop (≥ 1024px)
- Header: Full text sizes, full padding
- Grid: 4 columns
- Form: Full padding, centered with max-width

## Customization Tips

### Change Gradient Colors
Edit `assets/styles/main.css`:
```css
.from-indigo-50 {
    --gradient-from: #your-color;
}
```

### Add New Icons
Edit `src/components/contact_info_grid.py`:
```python
icons = {
    'your-icon': '''<svg>...</svg>''',
}
```

### Adjust Overlap
Change the negative margin in CSS:
```css
.-mt-8 {
    margin-top: -2rem;  /* Adjust this value */
}
```

## Files Modified/Created

### Created
- `src/components/contact_header.py` - Header component
- `src/components/contact_info_grid.py` - Info grid component
- `src/components/contact_form.py` - Modern form component
- `CONTACT_HEADER_USAGE.md` - Header documentation
- `CONTACT_INFO_GRID_USAGE.md` - Grid documentation
- `CONTACT_FORM_USAGE.md` - Form documentation
- `CONTACT_COMPONENTS_USAGE.md` (this file) - Combined documentation

### Modified
- `src/components/__init__.py` - Added exports for all 3 components
- `src/pages/contact/view.py` - Integrated all components
- `src/routes/contact.py` - Updated to handle new form fields
- `data/contact.yaml` - Added configuration for all components
- `assets/styles/main.css` - Added ~560 lines of styles

### Deprecated (can be removed)
- `src/pages/home/contact_form.py` - Old form builder
- `src/pages/home/contact_validation.js` - Old validation script

## Testing

To test the components:
1. Start the development server: `python app.py`
2. Navigate to `/contact`
3. Verify header:
   - Gradient background displays correctly
   - Badge, title, and description are visible
4. Verify info grid:
   - 4 cards show on desktop (2 on tablet, 1 on mobile)
   - Cards overlap header slightly (-mt-8)
   - Hover effects work on cards
   - Map links are clickable
5. Verify form:
   - All 5 fields render correctly
   - Form has message-circle icon in header
   - Real-time validation works (try invalid email)
   - Submit button shows loading state
   - Success message appears after submission
   - Form resets after successful submission
   - Success message auto-dismisses after 5s
6. Test responsive:
   - Resize browser to mobile width
   - Verify all components adapt properly

## See Also
- `CONTACT_HEADER_USAGE.md` - Detailed header component docs
- `CONTACT_INFO_GRID_USAGE.md` - Detailed grid component docs
- `CONTACT_FORM_USAGE.md` - Detailed form component docs
