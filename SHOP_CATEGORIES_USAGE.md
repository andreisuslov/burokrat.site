# Shop by Category Component Usage

This component displays a grid of category cards with icons, matching the design you provided.

## Files Created

1. **Component**: `src/components/shop_categories.py`
2. **Data**: `data/shop_categories.yaml`
3. **Icons**: 6 SVG files in `assets/images/`:
   - `pen.svg` (Lucide Pen icon)
   - `book-open.svg` (Lucide BookOpen icon)
   - `palette.svg` (Lucide Palette icon)
   - `briefcase.svg` (Lucide Briefcase icon)
   - `scissors.svg` (Lucide Scissors icon)
   - `sparkles.svg` (Lucide Sparkles icon)
4. **CSS**: Added styles to `assets/styles/main.css`

## How to Use in a Page

### Option 1: Add to an existing page

Edit the page's view file (e.g., `src/pages/home/view.py`):

```python
from fasthtml.common import *
from src.config import get_hero_data, get_services_data, get_contact_data, get_shop_categories_data
from src.components import create_hero, create_services, create_contact, create_shop_categories


def render():
    """Render main content for the Home page."""
    return (
        create_hero(get_hero_data()),
        create_shop_categories({'shop_categories': get_shop_categories_data()}),  # Add this line
        create_services(get_services_data()),
        create_contact(get_contact_data()),
    )
```

### Option 2: Create a new shop page

1. Create a new route file: `src/routes/shop.py`

```python
from fasthtml.common import *
from src.config import get_data, get_shop_categories_data
from src.components import Layout, create_shop_categories


def register_shop_route(rt):
    """Register shop page route."""
    
    @rt('/shop')
    def get():
        data = get_data()
        shop_data = {'shop_categories': get_shop_categories_data()}
        
        return Layout(
            'Shop | Burokrat',
            create_shop_categories(shop_data)
        )
```

2. Register the route in your main app file (`app.py`):

```python
from src.routes.shop import register_shop_route

# ... existing code ...

register_shop_route(rt)
```

## Customizing the Data

Edit `data/shop_categories.yaml` to customize:
- Title and subtitle
- Category names, descriptions, and URLs
- Icon colors (using the color classes)

## Component Features

- **Responsive Grid**: 1 column on mobile, 2 on tablet, 3 on desktop
- **Lucide Icons**: SVG icons with colored backgrounds using CSS masks
- **Hover Effects**: Cards lift slightly and show shadow on hover
- **Accessible**: Proper ARIA labels and semantic HTML
- **Customizable Colors**: Each category has its own color from a predefined palette

## Color Options

Available color classes in the YAML file:
- `bg-blue-500`: #3b82f6
- `bg-purple-500`: #a855f7
- `bg-pink-500`: #ec4899
- `bg-indigo-500`: #6366f1
- `bg-orange-500`: #f97316
- `bg-teal-500`: #14b8a6
