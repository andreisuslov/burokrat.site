from fasthtml.common import *


def create_featured_products(data):
    """Create featured products section with product cards."""
    featured_data = data.get('featured_products', {})
    title = featured_data.get('title', 'Избранные товары')
    subtitle = featured_data.get('subtitle', 'Тщательно отобранные товары, любимые нашими покупателями')
    products = featured_data.get('products', [])
    cta_text = featured_data.get('cta_text', 'Посмотреть все товары')
    cta_url = featured_data.get('cta_url', '/products')
    add_to_cart_text = featured_data.get('add_to_cart_text', 'Добавить в корзину')
    
    # Badge color mapping (supports both English and Russian)
    badge_colors = {
        'Bestseller': 'badge-bestseller',
        'Бестселлер': 'badge-bestseller',
        'New': 'badge-new',
        'Новинка': 'badge-new',
        'Premium': 'badge-premium',
        'Премиум': 'badge-premium',
        'Popular': 'badge-popular',
        'Популярный': 'badge-popular',
    }
    
    product_cards = []
    for product in products:
        product_id = product.get('id', '')
        name = product.get('name', '')
        price = product.get('price', 0)
        image = product.get('image', '')
        rating = product.get('rating', 0)
        badge = product.get('badge', '')
        badge_class = badge_colors.get(badge, 'badge-default')
        
        # Create star rating display
        star_icon = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'''
        
        rating_display = Div(
            NotStr(star_icon),
            Span(str(rating), cls='rating-value'),
            cls='product-rating'
        )
        
        # Create badge if exists
        badge_element = Span(badge, cls=f'product-badge {badge_class}') if badge else None
        
        # Create product card
        card = Div(
            Div(
                badge_element if badge_element else None,
                Img(
                    src=image,
                    alt=name,
                    cls='product-image',
                    loading='lazy'
                ),
                cls='product-image-container'
            ),
            Div(
                rating_display,
                H3(name, cls='product-name'),
                Div(
                    Span(f'${price:.2f}', cls='product-price'),
                    Button(add_to_cart_text, cls='btn-add-cart'),
                    cls='product-footer'
                ),
                cls='product-content'
            ),
            cls='product-card',
            data_product_id=str(product_id)
        )
        product_cards.append(card)
    
    return Section(
        Div(
            Div(
                H2(title, cls='featured-products-title'),
                P(subtitle, cls='featured-products-subtitle'),
                cls='featured-products-header'
            ),
            Div(
                *product_cards,
                cls='products-grid'
            ),
            Div(
                A(
                    cta_text,
                    href=cta_url,
                    cls='btn btn-outline view-all-btn'
                ),
                cls='featured-products-cta'
            ),
            cls='featured-products-container'
        ),
        cls='featured-products-section section'
    )
