from fasthtml.common import *
from .dropdown import create_dropdown


def create_products_page(data):
    """Create full products page with filters, search, and product grid."""
    
    # Extract data
    page_title = data.get('page_title', 'Наши товары')
    page_subtitle = data.get('page_subtitle', '')
    filters_title = data.get('filters_title', 'Фильтры')
    categories_title = data.get('categories_title', 'Категории')
    price_range_title = data.get('price_range_title', 'Диапазон цен')
    in_stock_only = data.get('in_stock_only', 'Только в наличии')
    clear_filters = data.get('clear_filters', 'Очистить все фильтры')
    search_placeholder = data.get('search_placeholder', 'Поиск товаров...')
    sort_label = data.get('sort_label', 'Рекомендуемые')
    showing_text = data.get('showing_text', 'Показано')
    of_text = data.get('of_text', 'из')
    products_text = data.get('products_text', 'товаров')
    add_to_cart_text = data.get('add_to_cart_text', 'Добавить в корзину')
    
    categories = data.get('categories', [])
    products = data.get('products', [])
    
    # Badge color mapping
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
    
    # Create category checkboxes
    category_items = []
    for cat in categories:
        cat_id = cat.get('id', '')
        cat_name = cat.get('name', '')
        checked = cat.get('checked', False)
        
        checkbox = Label(
            Input(
                type='checkbox',
                name='category',
                value=cat_id,
                checked=checked,
                cls='category-checkbox'
            ),
            Span(cat_name),
            cls='category-label'
        )
        category_items.append(checkbox)
    
    # Create filters sidebar
    filters_sidebar = Div(
        H3(filters_title, cls='filters-title'),
        
        # Categories section
        Div(
            H4(categories_title, cls='filter-section-title'),
            Div(
                *category_items,
                cls='category-list'
            ),
            cls='filter-section'
        ),
        
        # Price range section
        Div(
            H4(price_range_title, cls='filter-section-title'),
            Div(
                Div(
                    Div(cls='slider-track'),
                    Div(cls='slider-range', id='slider-range'),
                    Input(
                        type='range',
                        min='0',
                        max='100',
                        value='0',
                        cls='price-slider price-slider-min',
                        id='price-min'
                    ),
                    Input(
                        type='range',
                        min='0',
                        max='100',
                        value='100',
                        cls='price-slider price-slider-max',
                        id='price-max'
                    ),
                    cls='price-slider-container'
                ),
                Div(
                    Span('$0', cls='price-value', id='price-min-value'),
                    Span('$100', cls='price-value', id='price-max-value'),
                    cls='price-values'
                ),
                cls='price-range-controls'
            ),
            cls='filter-section'
        ),
        
        # In stock filter
        Div(
            Label(
                Input(
                    type='checkbox',
                    name='in-stock',
                    cls='stock-checkbox'
                ),
                Span(in_stock_only),
                cls='stock-label'
            ),
            cls='filter-section'
        ),
        
        # Clear filters button
        Button(clear_filters, cls='btn-clear-filters'),
        
        cls='filters-sidebar'
    )
    
    # Create search icon
    search_icon = '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>'''
    
    # Create star icon for ratings
    star_icon = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'''
    
    # Create product cards
    product_cards = []
    for product in products:
        product_id = product.get('id', '')
        name = product.get('name', '')
        price = product.get('price', 0)
        image = product.get('image', '')
        rating = product.get('rating', 0)
        reviews = product.get('reviews', 0)
        badge = product.get('badge', '')
        category = product.get('category', '')
        in_stock = product.get('in_stock', True)
        
        badge_class = badge_colors.get(badge, 'badge-default')
        
        # Create rating display
        rating_display = Div(
            NotStr(star_icon),
            Span(str(rating), cls='rating-value'),
            Span(f'({reviews} отзывов)', cls='review-count'),
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
            data_product_id=str(product_id),
            data_category=category,
            data_in_stock='true' if in_stock else 'false'
        )
        product_cards.append(card)
    
    # Create main content area
    main_content = Div(
        # Search and sort bar
        Div(
            Div(
                Span(NotStr(search_icon), cls='search-icon'),
                Input(
                    type='text',
                    placeholder=search_placeholder,
                    cls='search-input',
                    id='product-search'
                ),
                cls='search-box'
            ),
            create_dropdown(
                options=[
                    {'value': 'featured', 'label': sort_label},
                    {'value': 'price-asc', 'label': 'Цена: по возрастанию'},
                    {'value': 'price-desc', 'label': 'Цена: по убыванию'},
                    {'value': 'rating', 'label': 'Рейтинг'}
                ],
                selected_value='featured',
                dropdown_id='product-sort',
                variant='default',
                size='medium',
                width='short',
                custom_class='sort-select'
            ),
            cls='search-sort-bar'
        ),
        
        # Results count
        Div(
            Span(f'{showing_text} {len(products)} {of_text} {len(products)} {products_text}', cls='results-count'),
            cls='results-info'
        ),
        
        # Products grid
        Div(
            *product_cards,
            cls='products-grid',
            id='products-grid'
        ),
        
        cls='products-main-content'
    )
    
    # Create full page layout
    return Section(
        Div(
            # Page header
            Div(
                H1(page_title, cls='products-page-title'),
                P(page_subtitle, cls='products-page-subtitle'),
                cls='products-page-header'
            ),
            
            # Products layout with sidebar and main content
            Div(
                filters_sidebar,
                main_content,
                cls='products-layout'
            ),
            
            cls='products-page-container'
        ),
        # Include the product filters JavaScript
        Script(src='/assets/scripts/product-filters.js'),
        cls='products-page-section section'
    )
