# Contact Info Grid Component Usage

## Overview
The `create_contact_info_grid` component is a FastHTML implementation of a modern contact information grid with cards, inspired by React/Tailwind design patterns. It displays contact information in a responsive grid layout with icons, titles, and content.

## Component Location
- **File**: `src/components/contact_info_grid.py`
- **Function**: `create_contact_info_grid(items=None)`

## Features
- ✅ Responsive grid layout (1 column mobile, 2 columns tablet, 4 columns desktop)
- ✅ Card-based design with hover effects
- ✅ Inline SVG icons (map-pin, phone, clock, mail)
- ✅ Customizable icon background colors
- ✅ Support for multi-line content
- ✅ Optional clickable links
- ✅ Negative top margin for overlap effect with header

## Usage

### Basic Usage
```python
from src.components import create_contact_info_grid

# Use with default values
grid = create_contact_info_grid()

# Use with custom data
items = [
    {
        'icon': 'map-pin',
        'title': 'Visit Us',
        'content': 'Street Address\nCity, State, ZIP',
        'color': 'bg-indigo-100 text-indigo-600',
        'link': 'https://maps.google.com/...'
    },
    # ... more items
]
grid = create_contact_info_grid(items)
```

### Integration in Contact Page
The component is already integrated in the contact page at `src/pages/contact/view.py`:

```python
from src.components import create_contact_info_grid

def render():
    contact = get_contact_data()
    return (
        create_contact_header(contact.get('header')),
        create_contact_info_grid(contact.get('info_grid')),
        # ... other sections
    )
```

## Data Structure

### Item Properties
Each item in the grid accepts the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `icon` | string | No | Icon type: 'map-pin', 'phone', 'clock', 'mail' (default: 'map-pin') |
| `title` | string | Yes | Card title/heading |
| `content` | string | Yes | Card content (supports `\n` for line breaks) |
| `color` | string | No | Tailwind color classes for icon background (default: 'bg-indigo-100 text-indigo-600') |
| `link` | string | No | Optional URL to make content clickable |

### YAML Configuration
Configure the grid via `data/contact.yaml`:

```yaml
info_grid:
  - icon: "map-pin"
    title: "Офис (Строителей)"
    content: "Строителей проспект, 4\nг. Барнаул, Алтайский край, 656002"
    color: "bg-indigo-100 text-indigo-600"
    link: "https://www.google.com/maps/search/?api=1&query=..."
  
  - icon: "phone"
    title: "Позвоните нам"
    content: "+7 (3852) 62-82-82\n+7 (3852) 25-14-91"
    color: "bg-green-100 text-green-600"
  
  - icon: "clock"
    title: "Часы работы"
    content: "Понедельник - Воскресенье\n09:30 - 18:30"
    color: "bg-purple-100 text-purple-600"
  
  - icon: "mail"
    title: "Email"
    content: "info@example.com"
    color: "bg-orange-100 text-orange-600"
```

## Available Icons
The component includes inline SVG icons from lucide-react:

- **map-pin**: Location/address icon
- **phone**: Phone/call icon
- **clock**: Time/hours icon
- **mail**: Email icon

## Available Color Schemes
Pre-defined color combinations for icon backgrounds:

- `bg-indigo-100 text-indigo-600` - Indigo (default)
- `bg-blue-100 text-blue-600` - Blue
- `bg-green-100 text-green-600` - Green
- `bg-purple-100 text-purple-600` - Purple
- `bg-orange-100 text-orange-600` - Orange

## Styling
The component uses Tailwind-like utility classes defined in `assets/styles/main.css`:

### Key Classes
- `.contact-card` - Card container with border and hover effect
- `.grid` - Grid layout
- `.grid-cols-1`, `.md:grid-cols-2`, `.lg:grid-cols-4` - Responsive columns
- `.-mt-8` - Negative margin for overlap effect
- `.hover:shadow-lg` - Hover shadow effect

### Responsive Breakpoints
- **Mobile** (< 768px): 1 column
- **Tablet** (768px - 1023px): 2 columns
- **Desktop** (≥ 1024px): 4 columns

## Customization

### Adding New Icons
To add a new icon, edit `src/components/contact_info_grid.py`:

```python
def create_icon_svg(icon_type):
    icons = {
        'map-pin': '''<svg>...</svg>''',
        'phone': '''<svg>...</svg>''',
        'your-new-icon': '''<svg>...</svg>''',  # Add here
    }
    return NotStr(icons.get(icon_type, icons['map-pin']))
```

### Adding New Color Schemes
To add a new color scheme, edit `assets/styles/main.css`:

```css
.bg-red-100 {
    background-color: #fee2e2;
}

.text-red-600 {
    color: #dc2626;
}
```

## Example Output
The component renders a grid of cards, each containing:
1. Colored icon container (rounded square)
2. Title (bold heading)
3. Content (multi-line text, optionally clickable)

Cards have a subtle border and shadow on hover for a modern, interactive feel.
