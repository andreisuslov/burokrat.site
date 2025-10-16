import yaml
from pathlib import Path
from typing import Optional
from sqlmodel import select

_data = {}

def load_yaml_file(filename):
    """Load a YAML file from the data directory."""
    data_dir = Path(__file__).parent.parent.parent / 'data'
    file_path = data_dir / filename
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_page_data():
    """Load main page data from YAML file."""
    global _data
    _data['main'] = load_yaml_file('main_page.yaml')
    return _data

def load_about_data():
    """Load about page data from YAML file."""
    global _data
    if 'about' not in _data:
        _data['about'] = load_yaml_file('about.yaml')
    return _data['about']

def get_data():
    """Get main page data with FAQ."""
    main_data = _data.get('main', {})
    # Add FAQ data if available
    if 'faq' not in main_data:
        main_data['faq'] = get_faq_data()
    return main_data

def get_about_data():
    """Get about page data."""
    if 'about' not in _data:
        load_about_data()
    return _data['about']

def load_privacy_data():
    """Load privacy page data from YAML file."""
    global _data
    if 'privacy' not in _data:
        _data['privacy'] = load_yaml_file('privacy.yaml')
    return _data['privacy']

def get_privacy_data():
    """Get privacy page data."""
    if 'privacy' not in _data:
        load_privacy_data()
    return _data['privacy']

def load_contact_data():
    """Load contact page data from YAML file."""
    global _data
    if 'contact' not in _data:
        _data['contact'] = load_yaml_file('contact.yaml')
    return _data['contact']

def get_contact_data():
    """Get contact page data."""
    if 'contact' not in _data:
        load_contact_data()
    return _data['contact']

def load_seals_stamps_data():
    """Load seals and stamps page data from YAML file."""
    global _data
    if 'seals_stamps' not in _data:
        _data['seals_stamps'] = load_yaml_file('seals_stamps.yaml')
    return _data['seals_stamps']

def get_seals_stamps_data():
    """Get seals and stamps page data."""
    if 'seals_stamps' not in _data:
        load_seals_stamps_data()
    return _data['seals_stamps']

def load_self_inking_stamps_data():
    """Load self-inking stamps page data from YAML file."""
    global _data
    if 'self_inking_stamps' not in _data:
        _data['self_inking_stamps'] = load_yaml_file('self_inking_stamps.yaml')
    return _data['self_inking_stamps']

def get_self_inking_stamps_data():
    """Get self-inking stamps page data."""
    if 'self_inking_stamps' not in _data:
        load_self_inking_stamps_data()
    return _data['self_inking_stamps']

def load_stationery_data():
    """Load stationery page data from YAML file."""
    global _data
    if 'stationery' not in _data:
        _data['stationery'] = load_yaml_file('stationery.yaml')
    return _data['stationery']

def get_stationery_data():
    """Get stationery page data."""
    if 'stationery' not in _data:
        load_stationery_data()
    return _data['stationery']

def load_clients_data():
    """Load clients page data from YAML file."""
    global _data
    if 'clients' not in _data:
        _data['clients'] = load_yaml_file('clients.yaml')
    return _data['clients']

def get_clients_data():
    """Get clients page data."""
    if 'clients' not in _data:
        load_clients_data()
    return _data['clients']

def load_agreement_data():
    """Load agreement page data from YAML file."""
    global _data
    if 'agreement' not in _data:
        _data['agreement'] = load_yaml_file('agreement.yaml')
    return _data['agreement']

def get_agreement_data():
    """Get agreement page data."""
    if 'agreement' not in _data:
        load_agreement_data()
    return _data['agreement']

def load_hero_data():
    """Load hero section data from YAML file."""
    global _data
    if 'hero' not in _data:
        _data['hero'] = load_yaml_file('hero.yaml')
    return _data['hero']

def get_hero_data():
    """Get hero section data."""
    if 'hero' not in _data:
        load_hero_data()
    return _data['hero']

def get_header_data():
    """Get header data (from main page data)."""
    return get_data()

def get_footer_data():
    """Get footer data (merged from main page and about data for locations)."""
    main_data = get_data()
    about_data = get_about_data()
    # Merge locations from about data into main data
    footer_data = main_data.copy()
    footer_data['locations'] = about_data.get('locations', {})
    return footer_data

def get_services_data():
    """Get services data (from navigation data)."""
    return get_navigation_data()

def load_navigation_data():
    """Load navigation data from YAML file."""
    global _data
    if 'navigation' not in _data:
        _data['navigation'] = load_yaml_file('navigation.yaml')
    return _data['navigation']

def get_navigation_data():
    """Get navigation data."""
    if 'navigation' not in _data:
        load_navigation_data()
    return _data['navigation']

def load_products_services_data():
    """Load products and services page data from YAML file."""
    global _data
    if 'products_services' not in _data:
        _data['products_services'] = load_yaml_file('products_services.yaml')
    return _data['products_services']

def get_products_services_data():
    """Get products and services page data."""
    if 'products_services' not in _data:
        load_products_services_data()
    return _data['products_services']

def load_shop_categories_data():
    """Load shop categories data from YAML file."""
    global _data
    if 'shop_categories' not in _data:
        _data['shop_categories'] = load_yaml_file('shop_categories.yaml')
    return _data['shop_categories']

def get_shop_categories_data():
    """Get shop categories data."""
    if 'shop_categories' not in _data:
        load_shop_categories_data()
    return _data['shop_categories']

def load_featured_products_data():
    """Load featured products data from YAML file."""
    global _data
    if 'featured_products' not in _data:
        _data['featured_products'] = load_yaml_file('featured_products.yaml')
    return _data['featured_products']

def get_featured_products_data():
    """Get featured products data."""
    if 'featured_products' not in _data:
        load_featured_products_data()
    return _data['featured_products']

def load_faq_data():
    """Load FAQ data from YAML file."""
    global _data
    if 'faq' not in _data:
        _data['faq'] = load_yaml_file('faq.yaml')
    return _data['faq']

def get_faq_data():
    """Get FAQ data."""
    if 'faq' not in _data:
        load_faq_data()
    return _data['faq']


# ============================================================================
# DATABASE FUNCTIONS - Products and Categories
# ============================================================================

def get_products_from_db(
    category_id: Optional[str] = None,
    featured_only: bool = False,
    active_only: bool = True,
    limit: Optional[int] = None
):
    """Get products from database
    
    Args:
        category_id: Filter by category ID (e.g., 'writing-instruments')
        featured_only: Only return featured products
        active_only: Only return active products
        limit: Maximum number of products to return
        
    Returns:
        List of product dictionaries
    """
    from src.db import get_db_session
    from src.models import Product
    
    session = get_db_session()
    try:
        statement = select(Product)
        
        if active_only:
            statement = statement.where(Product.active == True)
        
        if category_id and category_id != 'all':
            statement = statement.where(Product.category_id == category_id)
        
        if featured_only:
            statement = statement.where(Product.featured == True)
        
        statement = statement.order_by(Product.sort_order, Product.id)
        
        if limit:
            statement = statement.limit(limit)
        
        products = session.exec(statement).all()
        
        # Convert to dictionaries
        return [
            {
                'id': p.id,
                'name': p.name,
                'category': p.category_id,
                'price': p.price,
                'image': p.image,
                'rating': p.rating,
                'reviews': p.reviews,
                'badge': p.badge,
                'in_stock': p.in_stock,
                'description': p.description
            }
            for p in products
        ]
    finally:
        session.close()


def get_categories_from_db(active_only: bool = True):
    """Get categories from database
    
    Args:
        active_only: Only return active categories
        
    Returns:
        List of category dictionaries
    """
    from src.db import get_db_session
    from src.models import Category
    
    session = get_db_session()
    try:
        statement = select(Category)
        
        if active_only:
            statement = statement.where(Category.active == True)
        
        statement = statement.order_by(Category.sort_order, Category.id)
        
        categories = session.exec(statement).all()
        
        # Convert to dictionaries
        return [
            {
                'id': c.id,
                'name': c.name,
                'description': c.description,
                'icon': c.icon,
                'color': c.color,
                'url': c.url,
                'checked': c.id == 'all'  # For compatibility with existing templates
            }
            for c in categories
        ]
    finally:
        session.close()


def get_db_products_services_data():
    """Get products and services data from database (replaces YAML version)"""
    # Get metadata from YAML (page titles, labels, etc.)
    yaml_data = get_products_services_data()
    
    # Override products and categories with database data
    yaml_data['products'] = get_products_from_db()
    yaml_data['categories'] = get_categories_from_db()
    
    return yaml_data


def get_db_shop_categories_data():
    """Get shop categories data from database (replaces YAML version)"""
    # Get title/subtitle from YAML
    yaml_data = get_shop_categories_data()
    
    # Override categories with database data (exclude 'all' category)
    db_categories = [c for c in get_categories_from_db() if c['id'] != 'all']
    yaml_data['categories'] = db_categories
    
    return yaml_data


def get_db_featured_products_data():
    """Get featured products data from database (replaces YAML version)"""
    # Get metadata from YAML (title, subtitle, CTA, etc.)
    yaml_data = get_featured_products_data()
    
    # Override products with database data (featured only)
    yaml_data['products'] = get_products_from_db(featured_only=True)
    
    return yaml_data
