from fasthtml.common import *


def create_shop_categories(data):
    """Create shop by category section with icon cards."""
    categories_data = data.get('shop_categories', {})
    title = categories_data.get('title', 'Shop by Category')
    subtitle = categories_data.get('subtitle', '')
    categories = categories_data.get('categories', [])
    
    # Map color classes to actual color values
    color_map = {
        'bg-blue-500': '#3b82f6',
        'bg-purple-500': '#a855f7',
        'bg-pink-500': '#ec4899',
        'bg-indigo-500': '#6366f1',
        'bg-orange-500': '#f97316',
        'bg-teal-500': '#14b8a6',
    }
    
    category_cards = []
    for category in categories:
        icon_src = category.get('icon', '')
        name = category.get('name', '')
        description = category.get('description', '')
        color_class = category.get('color', 'bg-blue-500')
        color_value = color_map.get(color_class, '#3b82f6')
        url = category.get('url', '#')
        
        # Create icon with colored background
        icon_node = Div(
            Span(
                cls='category-icon-inner',
                role='img',
                aria_label=name,
                style=(
                    f"background-color: {color_value}; "
                    f"-webkit-mask: url('{icon_src}') no-repeat center / contain; "
                    f"mask: url('{icon_src}') no-repeat center / contain;"
                )
            ),
            cls='category-icon'
        )
        
        # Create category card
        card = A(
            icon_node,
            Div(
                H3(name, cls='category-name'),
                P(description, cls='category-description'),
                cls='category-content'
            ),
            href=url,
            cls='category-card',
            draggable='false'
        )
        category_cards.append(card)
    
    return Section(
        Div(
            H2(title, cls='shop-categories-title'),
            P(subtitle, cls='shop-categories-subtitle'),
            Div(
                *category_cards,
                cls='categories-grid'
            ),
            cls='shop-categories-container'
        ),
        cls='shop-categories-section section'
    )
