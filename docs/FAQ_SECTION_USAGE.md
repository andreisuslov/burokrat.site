# FAQ Section Component Usage

## Overview
The `create_faq_section` component is a FastHTML implementation of an accordion-based FAQ section with smooth animations and interactive behavior, inspired by React/shadcn-ui design patterns.

## Component Location
- **File**: `src/components/faq_section.py`
- **Function**: `create_faq_section(data=None)`

## Features
- ✅ Accordion-style collapsible items
- ✅ Smooth expand/collapse animations
- ✅ Auto-close other items when opening one
- ✅ Chevron icon rotation animation
- ✅ Hover effects on questions
- ✅ Clean, modern design with rounded corners
- ✅ Fully responsive layout
- ✅ Click outside to close all items
- ✅ Accessible keyboard navigation

## Usage

### Basic Usage
```python
from src.components import create_faq_section

# Use with default values
faq = create_faq_section()

# Use with custom data
faq_data = {
    'title': 'Frequently Asked Questions',
    'subtitle': 'Find quick answers to common questions',
    'items': [
        {
            'question': 'What services do you offer?',
            'answer': 'We provide a variety of services including...'
        },
        {
            'question': 'How long does it take?',
            'answer': 'Standard turnaround time is 1-2 business days...'
        },
        # ... more items
    ]
}
faq = create_faq_section(faq_data)
```

### Integration in Pages
```python
from fasthtml.common import *
from src.components import create_faq_section
from src.config import get_data

def render():
    data = get_data()
    faq_data = data.get('faq', {})
    
    return (
        # ... other sections
        create_faq_section(faq_data),
        # ... more sections
    )
```

## Data Structure

### Configuration Object
```python
{
    'title': str,      # Section title
    'subtitle': str,   # Section subtitle
    'items': [         # List of FAQ items
        {
            'question': str,  # Question text
            'answer': str     # Answer text
        },
        # ... more items
    ]
}
```

### YAML Configuration
Create `data/faq.yaml`:

```yaml
title: "Часто задаваемые вопросы"
subtitle: "Найдите быстрые ответы на распространенные вопросы"

items:
  - question: "Какие услуги печати вы предлагаете?"
    answer: "Мы предоставляем широкий спектр полиграфических услуг, включая стандартную печать документов, копирование, печать визиток, брошюр, флаеров и многое другое."
  
  - question: "Как быстро вы можете изготовить печать или штамп?"
    answer: "Стандартное время изготовления печати или штампа составляет 1-2 рабочих дня. Мы также предлагаем срочное изготовление за 24 часа."
  
  - question: "Какие документы нужны для заказа печати?"
    answer: "Для изготовления печати организации необходимы: свидетельство о регистрации (ОГРН/ОГРНИП), ИНН, устав или положение."
  
  # ... more FAQs
```

## Accordion Behavior

### Interaction
1. **Click question** → Opens answer, closes other open items
2. **Click same question again** → Closes answer
3. **Click outside accordion** → Closes all items
4. **Hover question** → Changes text color to indigo

### Animation
- **Expand**: Smooth height transition with max-height
- **Icon rotation**: 180° rotation when active
- **Color change**: Gray → Indigo when active

### JavaScript Functions
```javascript
toggleAccordion(itemId)
// - Closes all other accordions
// - Toggles current accordion
// - Rotates chevron icon
// - Adds/removes 'active' class
```

## Styling

### CSS Classes
All styles are defined in `assets/styles/main.css` (lines 3088-3236):

#### Section Container
- `.faq-section` - White background, vertical padding
- `.faq-accordion` - Accordion container with spacing

#### Accordion Items
- `.accordion-item` - Individual FAQ item with border and rounded corners
- `.accordion-trigger` - Clickable question button
- `.accordion-content` - Collapsible answer container
- `.accordion-content-inner` - Answer text wrapper

#### States
- `.accordion-trigger:hover` - Hover state (indigo color)
- `.accordion-trigger.active` - Active/open state
- `.accordion-content.active` - Expanded content

#### Icons
- `.accordion-icon-wrapper` - Icon container with rotation
- `.accordion-icon` - Chevron down SVG icon

### Color Scheme
- **Default text**: Gray-900 (#111827)
- **Hover/Active**: Indigo-600 (#6366f1)
- **Answer text**: Gray-600 (#4b5563)
- **Background**: Gray-50 (#f9fafb)
- **Border**: Gray-200 (#e5e7eb)

### Typography
- **Title**: 2.25rem (36px), bold
- **Subtitle**: 1.25rem (20px), gray-600
- **Question**: 1.125rem (18px), semi-bold
- **Answer**: 1rem (16px), line-height 1.75

## Responsive Design

### Desktop (> 768px)
- Full text sizes
- 3rem bottom margin for header
- 1.25rem padding for accordion items

### Tablet (≤ 768px)
- Smaller title (1.875rem)
- Reduced question size (1rem)
- 2rem bottom margin for header

### Mobile (≤ 480px)
- Compact title (1.5rem)
- Smaller question text (0.9375rem)
- Reduced horizontal padding

## Accessibility

### Keyboard Support
- **Tab**: Navigate between questions
- **Enter/Space**: Toggle accordion
- **Focus visible**: Outline on keyboard focus

### ARIA Attributes (can be added)
```python
Button(
    ...,
    aria_expanded='false',
    aria_controls=item_id,
    role='button'
)
```

## Customization

### Change Colors
Edit `assets/styles/main.css`:
```css
.accordion-trigger:hover {
    color: #your-color;
}

.accordion-trigger.active {
    color: #your-active-color;
}
```

### Change Animation Speed
Edit the component JavaScript:
```javascript
// In faq_section.py, modify transition duration
content.style.transition = 'max-height 0.5s ease'; // Slower
```

Or in CSS:
```css
.accordion-content {
    transition: max-height 0.5s ease, padding 0.5s ease;
}
```

### Add Icons to Questions
Modify `create_faq_item()`:
```python
Button(
    Span('🔍', cls='mr-2'),  # Add icon
    Span(question, cls='pr-4'),
    # ... rest of code
)
```

### Multi-Open Mode
To allow multiple items open at once, modify the JavaScript:
```javascript
// Remove the "close all others" logic
// Keep only the toggle logic for current item
```

## Advanced Features

### Add Categories
Group FAQs by category:
```python
def create_faq_section_with_categories(data):
    categories = data.get('categories', [])
    
    return Div(
        *[
            Div(
                H3(cat['name'], cls='category-title'),
                Div(
                    *[create_faq_item(faq, idx) 
                      for idx, faq in enumerate(cat['items'])],
                    cls='faq-accordion space-y-4'
                ),
                cls='faq-category mb-8'
            )
            for cat in categories
        ],
        cls='faq-section'
    )
```

### Search Functionality
Add a search box to filter FAQs:
```python
Div(
    Input(
        type='text',
        placeholder='Search FAQs...',
        id='faq-search',
        oninput='filterFAQs(this.value)',
        cls='search-input'
    ),
    cls='mb-6'
)
```

### Analytics Tracking
Track which FAQs are opened:
```javascript
function toggleAccordion(itemId) {
    // ... existing code
    
    // Track analytics
    if (content.classList.contains('active')) {
        gtag('event', 'faq_opened', {
            'question': trigger.textContent.trim()
        });
    }
}
```

## Example Integration

### Add to Contact Page
```python
# src/pages/contact/view.py
from src.components import create_faq_section

def render():
    contact = get_contact_data()
    faq_data = get_data().get('faq', {})
    
    return (
        create_contact_header(contact.get('header')),
        create_contact_info_grid(contact.get('info_grid')),
        create_contact_form(contact.get('form')),
        create_faq_section(faq_data),  # Add FAQ section
        # ... other sections
    )
```

### Add to Home Page
```python
# src/pages/home/view.py
def render():
    data = get_data()
    
    return (
        create_hero(data.get('hero')),
        create_services(data.get('services')),
        create_faq_section(data.get('faq')),  # Add FAQ section
        create_cta(data.get('cta')),
    )
```

## Testing

To test the FAQ section:
1. Navigate to page with FAQ component
2. Verify:
   - All questions are visible
   - Clicking a question opens the answer
   - Answer expands smoothly
   - Chevron icon rotates 180°
   - Question text turns indigo
   - Clicking another question closes the first
   - Clicking same question again closes it
   - Clicking outside closes all items
3. Test responsive:
   - Resize to mobile width
   - Verify text sizes adjust
   - Verify padding adjusts

## Performance

### Optimization Tips
- Use `will-change: max-height` for smoother animations
- Limit number of FAQs per page (10-15 recommended)
- Consider lazy loading for very long FAQ lists
- Use CSS containment for better rendering

### Bundle Size
- Component: ~2KB (Python)
- JavaScript: ~1KB (inline)
- CSS: ~3KB
- **Total**: ~6KB

## Browser Support
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers
- ⚠️ IE11 (requires polyfills)

## Troubleshooting

### Accordion not opening
- Check JavaScript is loaded
- Verify `toggleAccordion` function exists
- Check browser console for errors

### Animation jerky
- Ensure `max-height` is set correctly
- Check for CSS conflicts
- Verify transition property is applied

### Icons not showing
- Check SVG is properly escaped in NotStr()
- Verify icon CSS classes are applied
- Inspect element in DevTools

## Files

### Created
- `src/components/faq_section.py` - Component
- `data/faq.yaml` - Sample FAQ data
- `FAQ_SECTION_USAGE.md` - This documentation

### Modified
- `src/components/__init__.py` - Added export
- `assets/styles/main.css` - Added ~150 lines of styles

## See Also
- Accordion pattern: https://www.w3.org/WAI/ARIA/apg/patterns/accordion/
- shadcn/ui Accordion: https://ui.shadcn.com/docs/components/accordion
