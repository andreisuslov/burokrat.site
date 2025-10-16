# Products Database Migration - Complete Guide

## 🎉 Migration Complete!

All products and categories have been successfully migrated from YAML files to the SQLModel database.

## ✅ What Was Implemented

### 1. Database Models

**Product Model** (`src/models/product.py`):
- id, name, category_id
- price, image, rating, reviews
- badge, in_stock, description
- featured, active, sort_order
- created_at, updated_at

**Category Model** (`src/models/product.py`):
- id (slug like "writing-instruments")
- name, description
- icon, color, url
- sort_order, active

### 2. Data Migration Script

**`migrate_products.py`** - Imports YAML data to database:
- Reads from `data/featured_products.yaml`
- Reads from `data/products_services.yaml`
- Reads from `data/shop_categories.yaml`
- Creates categories and products
- Marks featured products
- Shows migration summary

### 3. Database Functions

**New functions in `src/config/data_loader.py`**:
- `get_products_from_db()` - Query products with filters
- `get_categories_from_db()` - Get all categories
- `get_db_products_services_data()` - Products page data
- `get_db_shop_categories_data()` - Categories data
- `get_db_featured_products_data()` - Featured products

### 4. Updated Routes

All product routes now use database instead of YAML:
- **Home page** (`src/pages/home/view.py`) - Featured products & categories
- **Products page** (`src/routes/products_services.py`) - All products
- **Featured products** (`src/routes/featured_products.py`) - Featured only

### 5. Enhanced Database Utilities

**`db_utils.py`** now supports:
```bash
python3 db_utils.py products    # List all products
python3 db_utils.py categories  # List all categories
python3 db_utils.py stats       # Show full statistics
```

## 📊 Current Database State

```
Categories: 7
├── Все товары (all)
├── Письменные принадлежности (writing-instruments)
├── Блокноты и журналы (notebooks-journals)
├── Художественные принадлежности (art-supplies)
├── Офисные принадлежности (office-essentials)
├── Товары для рукоделия (craft-supplies)
└── Настольные аксессуары (desk-accessories)

Products: 12 total, 4 featured
├── Writing Instruments: 4 products
├── Notebooks & Journals: 2 products
├── Art Supplies: 2 products
├── Office Essentials: 1 product
├── Craft Supplies: 1 product
└── Desk Accessories: 2 products
```

## 🚀 Usage Examples

### Query Products in Code

```python
from src.config import get_products_from_db, get_categories_from_db

# Get all products
all_products = get_products_from_db()

# Get products by category
pens = get_products_from_db(category_id='writing-instruments')

# Get featured products only
featured = get_products_from_db(featured_only=True)

# Get limited number of products
top_5 = get_products_from_db(limit=5)

# Get all categories
categories = get_categories_from_db()
```

### Add New Products

```python
from src.db import get_db_session
from src.models import Product

session = get_db_session()

new_product = Product(
    name="Элитная перьевая ручка",
    category_id="writing-instruments",
    price=149.99,
    image="https://...",
    rating=4.9,
    reviews=50,
    badge="Новинка",
    in_stock=True,
    featured=True,
    active=True
)

session.add(new_product)
session.commit()
session.close()
```

### Update Products

```python
from src.db import get_db_session
from src.models import Product

session = get_db_session()

# Get product by ID
product = session.get(Product, 1)

# Update fields
product.price = 79.99
product.in_stock = False

session.commit()
session.close()
```

### Query with Filters

```python
from src.db import get_db_session
from src.models import Product
from sqlmodel import select

session = get_db_session()

# Get products with high rating
statement = select(Product).where(
    Product.rating >= 4.8,
    Product.in_stock == True
).order_by(Product.rating.desc())

top_rated = session.exec(statement).all()
session.close()
```

## 🔧 Command Line Tools

### View Database Contents

```bash
# Show statistics
python3 db_utils.py stats

# List all products
python3 db_utils.py products

# List all categories
python3 db_utils.py categories

# List contact submissions
python3 db_utils.py list
```

### Re-migrate Data

If you need to re-import products from YAML:

```bash
python3 migrate_products.py
```

The script will ask for confirmation before clearing existing data.

## 📁 File Structure

```
burokrat.site/
├── data/
│   ├── burokrat.db                    # SQLite database
│   ├── featured_products.yaml         # Source data (backup)
│   ├── products_services.yaml         # Source data (backup)
│   └── shop_categories.yaml           # Source data (backup)
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── contact.py                 # Contact model
│   │   └── product.py                 # Product & Category models
│   ├── config/
│   │   ├── __init__.py
│   │   └── data_loader.py             # Database query functions
│   ├── routes/
│   │   ├── products_services.py       # Products page (uses DB)
│   │   └── featured_products.py       # Featured page (uses DB)
│   └── pages/
│       └── home/
│           └── view.py                # Home page (uses DB)
├── migrate_products.py                # Migration script
└── db_utils.py                        # Database utilities
```

## 🎯 Key Benefits

### 1. Dynamic Content Management
- Add/edit products without redeploying
- Update prices and inventory in real-time
- Mark products as featured on-the-fly

### 2. Better Performance
- Indexed queries for fast lookups
- Efficient filtering and sorting
- Pagination support built-in

### 3. Scalability
- Easy to add new fields
- Support for relationships (categories, tags, etc.)
- Ready for admin panel

### 4. Data Integrity
- Type validation with Pydantic
- Foreign key constraints
- Automatic timestamps

## 🔍 Database Schema

### Products Table

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| id | INTEGER | No | Primary key (auto-increment) |
| name | VARCHAR(255) | No | Product name |
| category_id | VARCHAR(100) | No | Foreign key to categories |
| price | FLOAT | No | Product price |
| image | VARCHAR(1000) | No | Image URL |
| rating | FLOAT | No | Rating (0-5) |
| reviews | INTEGER | No | Number of reviews |
| badge | VARCHAR(100) | Yes | Badge text (e.g., "Новинка") |
| in_stock | BOOLEAN | No | Availability status |
| description | TEXT | Yes | Product description |
| featured | BOOLEAN | No | Show on homepage |
| active | BOOLEAN | No | Product is active |
| sort_order | INTEGER | No | Display order |
| created_at | DATETIME | No | Creation timestamp |
| updated_at | DATETIME | No | Last update timestamp |

### Categories Table

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| id | VARCHAR(100) | No | Primary key (slug) |
| name | VARCHAR(255) | No | Category name |
| description | VARCHAR(500) | Yes | Category description |
| icon | VARCHAR(255) | Yes | Icon path |
| color | VARCHAR(100) | Yes | Color class |
| url | VARCHAR(255) | Yes | Category URL |
| sort_order | INTEGER | No | Display order |
| active | BOOLEAN | No | Category is active |

## 🚦 Migration Status

- ✅ Product model created
- ✅ Category model created
- ✅ Migration script created
- ✅ Database populated (7 categories, 12 products)
- ✅ Config loaders updated
- ✅ Routes updated to use database
- ✅ Home page using database
- ✅ Products page using database
- ✅ Featured products using database
- ✅ Database utilities updated

## 📝 YAML Files Status

The original YAML files are **still in place** as backups and for metadata:
- `featured_products.yaml` - Page titles, CTA text
- `products_services.yaml` - Filter labels, UI text
- `shop_categories.yaml` - Section titles, subtitles

The new database functions load page metadata from YAML but **override the products and categories with database data**.

## 🔄 Workflow

### Current Setup:
1. Database contains all product data
2. Pages load products from database
3. YAML files provide UI text/labels
4. Best of both worlds!

### To Add a New Product:
```python
from src.db import get_db_session
from src.models import Product

session = get_db_session()
product = Product(
    name="New Product",
    category_id="writing-instruments",
    price=99.99,
    image="https://...",
    rating=5.0,
    reviews=0,
    in_stock=True,
    featured=False
)
session.add(product)
session.commit()
session.close()
```

## 🎓 Next Steps

### Immediate Enhancements:
- [ ] Create admin panel for product management
- [ ] Add product search functionality
- [ ] Implement product details page
- [ ] Add image upload support
- [ ] Create product API endpoints

### Future Improvements:
- [ ] Add product variants (size, color)
- [ ] Implement shopping cart
- [ ] Add product reviews system
- [ ] Create inventory tracking
- [ ] Add product analytics
- [ ] Implement product recommendations

## 📚 Documentation

- **Database Setup**: `DATABASE_SETUP.md`
- **Quick Start**: `QUICKSTART_DATABASE.md`
- **SQLModel Implementation**: `SQLMODEL_IMPLEMENTATION.md`
- **This Document**: `PRODUCTS_DATABASE.md`

## ✨ Summary

**Products are now fully database-driven!**

- **12 products** across **7 categories** migrated
- **4 featured products** on homepage
- All pages load from database
- YAML files retained for UI text
- Easy to manage with command-line tools
- Ready for admin panel development

**Database location**: `data/burokrat.db`  
**Migration tool**: `python3 migrate_products.py`  
**Database tool**: `python3 db_utils.py products`  
**View stats**: `python3 db_utils.py stats`

---

**Migration Date**: October 15, 2025  
**Status**: ✅ Complete and Tested  
**Products Migrated**: 12  
**Categories Created**: 7
