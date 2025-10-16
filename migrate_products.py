#!/usr/bin/env python3
"""Migrate products and categories from YAML files to database"""
import sys
import yaml
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.db import get_db_session, create_db_and_tables
from src.models import Product, Category
from sqlmodel import select


def load_yaml_data():
    """Load data from YAML files"""
    data_dir = Path(__file__).parent / "data"
    
    with open(data_dir / "shop_categories.yaml", 'r', encoding='utf-8') as f:
        shop_categories = yaml.safe_load(f)
    
    with open(data_dir / "products_services.yaml", 'r', encoding='utf-8') as f:
        products_data = yaml.safe_load(f)
    
    with open(data_dir / "featured_products.yaml", 'r', encoding='utf-8') as f:
        featured_data = yaml.safe_load(f)
    
    return shop_categories, products_data, featured_data


def migrate_categories(session, shop_categories, products_data):
    """Migrate categories to database"""
    print("\n📂 Migrating Categories...")
    print("=" * 80)
    
    # First, create "all" category
    all_category = Category(
        id="all",
        name="Все товары",
        description="Все доступные товары",
        icon="",
        color="bg-gray-500",
        url="/products",
        sort_order=0,
        active=True
    )
    session.add(all_category)
    print(f"✅ Created category: {all_category.name} ({all_category.id})")
    
    # Map from category name patterns to IDs
    category_mapping = {
        "Письменные принадлежности": "writing-instruments",
        "Блокноты и журналы": "notebooks-journals",
        "Художественные принадлежности": "art-supplies",
        "Офисные принадлежности": "office-essentials",
        "Товары для рукоделия": "craft-supplies",
        "Настольные аксессуары": "desk-accessories"
    }
    
    # Migrate from shop_categories.yaml
    for idx, cat_data in enumerate(shop_categories.get('categories', []), start=1):
        cat_name = cat_data.get('name', '')
        cat_id = category_mapping.get(cat_name, cat_name.lower().replace(' ', '-'))
        
        category = Category(
            id=cat_id,
            name=cat_name,
            description=cat_data.get('description', ''),
            icon=cat_data.get('icon', ''),
            color=cat_data.get('color', 'bg-blue-500'),
            url=cat_data.get('url', f'/products/{cat_id}'),
            sort_order=idx,
            active=True
        )
        session.add(category)
        print(f"✅ Created category: {category.name} ({category.id})")
    
    # Also add categories from products_services.yaml that might be missing
    for cat_data in products_data.get('categories', []):
        cat_id = cat_data.get('id')
        if cat_id and cat_id != 'all':
            # Check if it exists
            existing = session.get(Category, cat_id)
            if not existing:
                category = Category(
                    id=cat_id,
                    name=cat_data.get('name', cat_id),
                    description='',
                    icon='',
                    color='bg-blue-500',
                    url=f'/products/{cat_id}',
                    sort_order=100,
                    active=True
                )
                session.add(category)
                print(f"✅ Created additional category: {category.name} ({category.id})")
    
    session.commit()
    print(f"\n{'=' * 80}")


def migrate_products(session, products_data, featured_data):
    """Migrate products to database"""
    print("\n📦 Migrating Products...")
    print("=" * 80)
    
    # Get featured product IDs
    featured_ids = {p.get('id') for p in featured_data.get('products', [])}
    
    # Migrate products from products_services.yaml
    for prod_data in products_data.get('products', []):
        product_id = prod_data.get('id')
        
        product = Product(
            id=product_id,
            name=prod_data.get('name', ''),
            category_id=prod_data.get('category', 'all'),
            price=float(prod_data.get('price', 0)),
            image=prod_data.get('image', ''),
            rating=float(prod_data.get('rating', 0)),
            reviews=int(prod_data.get('reviews', 0)),
            badge=prod_data.get('badge', ''),
            in_stock=prod_data.get('in_stock', True),
            description=prod_data.get('description', ''),
            featured=product_id in featured_ids,
            active=True,
            sort_order=product_id if product_id else 0
        )
        session.add(product)
        
        featured_mark = "⭐" if product.featured else "  "
        print(f"{featured_mark} Created product: {product.name} (${product.price})")
    
    session.commit()
    print(f"\n{'=' * 80}")


def show_migration_summary(session):
    """Show summary of migrated data"""
    print("\n📊 Migration Summary")
    print("=" * 80)
    
    # Count categories
    categories = session.exec(select(Category)).all()
    print(f"Categories: {len(categories)}")
    for cat in categories:
        print(f"  - {cat.name} ({cat.id})")
    
    # Count products
    total_products = len(session.exec(select(Product)).all())
    featured_products = len(session.exec(
        select(Product).where(Product.featured == True)
    ).all())
    
    print(f"\nProducts: {total_products}")
    print(f"Featured Products: {featured_products}")
    
    # Products by category
    print("\nProducts by Category:")
    for cat in categories:
        if cat.id == 'all':
            continue
        count = len(session.exec(
            select(Product).where(Product.category_id == cat.id)
        ).all())
        print(f"  - {cat.name}: {count} products")
    
    print("=" * 80)


def clear_existing_data(session):
    """Clear existing products and categories"""
    print("\n🗑️  Clearing existing data...")
    
    # Delete products first (foreign key constraint)
    products = session.exec(select(Product)).all()
    for product in products:
        session.delete(product)
    
    # Delete categories
    categories = session.exec(select(Category)).all()
    for category in categories:
        session.delete(category)
    
    session.commit()
    print("✅ Existing data cleared")


def main():
    """Main migration function"""
    print("\n🚀 Product Migration Tool")
    print("=" * 80)
    print("This will migrate products and categories from YAML to database")
    print("=" * 80)
    
    # Check for --force flag for non-interactive mode
    force_mode = '--force' in sys.argv
    
    # Initialize database
    print("\n📊 Initializing database...")
    create_db_and_tables()
    
    # Get session
    session = get_db_session()
    
    try:
        # Check if data already exists
        existing_products = len(session.exec(select(Product)).all())
        existing_categories = len(session.exec(select(Category)).all())
        
        if existing_products > 0 or existing_categories > 0:
            print(f"\n⚠️  Warning: Database already contains data")
            print(f"   Categories: {existing_categories}")
            print(f"   Products: {existing_products}")
            
            if force_mode:
                print("🔄 Force mode enabled - clearing existing data...")
                clear_existing_data(session)
            else:
                response = input("\nClear existing data and re-import? (yes/no): ")
                if response.lower() != 'yes':
                    print("❌ Migration cancelled")
                    return
                
                clear_existing_data(session)
        
        # Load YAML data
        print("\n📄 Loading YAML files...")
        shop_categories, products_data, featured_data = load_yaml_data()
        print("✅ YAML files loaded")
        
        # Migrate data
        migrate_categories(session, shop_categories, products_data)
        migrate_products(session, products_data, featured_data)
        
        # Show summary
        show_migration_summary(session)
        
        print("\n✅ Migration completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()
