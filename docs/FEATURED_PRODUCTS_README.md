# Featured Products Component

A modern, responsive featured products component for displaying product cards with images, ratings, prices, and badges.

## Features

- **Responsive Grid Layout**: Automatically adjusts from 1 column (mobile) to 4 columns (desktop)
- **Product Cards**: Each card includes:
  - Product image with hover zoom effect
  - Badge (Bestseller, New, Premium, Popular)
  - Star rating display
  - Product name
  - Price
  - "Add to Cart" button
- **Modern Design**: Clean, professional styling with smooth animations
- **Customizable**: Easy to modify colors, spacing, and content via YAML data file

## Files Created

1. **Component**: `/src/components/featured_products.py`
2. **Data File**: `/data/featured_products.yaml`
3. **Styles**: Added to `/assets/styles/main.css` (lines 1900-2148)
4. **Demo Route**: `/src/routes/featured_products.py`

## Usage

### View the Demo

Visit: `http://localhost:8080/featured-products`

### Integrate into a Page

```python
from src.components import create_featured_products
from src.config import get_featured_products_data

# In your page render function
def render():
    data = {'featured_products': get_featured_products_data()}
    return (
        # ... other components
        create_featured_products(data),
        # ... other components
    )
```

### Customize Data

Edit `/data/featured_products.yaml`:

```yaml
title: "Избранные товары"
subtitle: "Отобранные товары любимыми нашими клиентами"
cta_text: "Посмотреть все товары"
cta_url: "/products"

products:
  - id: 1
    name: "Наименование товара"
    price: 99.99
    image: "https://example.com/image.jpg"
    rating: 4.9
    badge: "Бестселлер"
```

## Badge Colors

- **Бестселлер**: Indigo gradient (#6366f1 → #4f46e5)
- **Новинка**: Blue gradient (#3b82f6 → #2563eb)
- **Премиум**: Purple gradient (#8b5cf6 → #7c3aed)
- **Популярный**: Indigo gradient (#6366f1 → #4f46e5)

## Responsive Breakpoints

- **Mobile** (< 640px): 1 column
- **Tablet** (640px - 1023px): 2 columns
- **Desktop** (≥ 1024px): 4 columns

## Star Icon

The component uses an inline SVG star icon from Lucide icons for the rating display.

## Styling Classes

Main CSS classes:
- `.featured-products-section` - Main section wrapper
- `.product-card` - Individual product card
- `.product-badge` - Badge overlay
- `.product-rating` - Star rating display
- `.btn-add-cart` - Add to cart button

## Integration Notes

The component is fully integrated into the application:
- ✅ Component exported in `/src/components/__init__.py`
- ✅ Data loader functions added to `/src/config/data_loader.py`
- ✅ Config exports updated in `/src/config/__init__.py`
- ✅ Demo route registered in `/src/routes/__init__.py`
- ✅ CSS styles added to main stylesheet

## Future Enhancements

Potential improvements:
- Add shopping cart functionality
- Implement product detail pages
- Add product filtering/sorting
- Include product variants (size, color)
- Add wishlist functionality
- Implement lazy loading for images
