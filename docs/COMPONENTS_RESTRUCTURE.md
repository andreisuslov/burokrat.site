# Components Folder Restructure

## Overview
Reorganized the `src/components/` folder into logical subfolders for better maintainability and code organization.

## New Structure

```
src/components/
├── __init__.py                 # Main exports
├── layout/                     # Core layout components
│   ├── __init__.py
│   ├── layout.py              # Main layout wrapper
│   ├── header.py              # Site header
│   ├── footer.py              # Site footer
│   └── burger_menu.py         # Mobile navigation menu
├── ui/                        # Reusable UI components
│   ├── __init__.py
│   ├── dropdown.py            # Dropdown component
│   └── error_404.py           # 404 error page
├── contact/                   # Contact-related components
│   ├── __init__.py
│   ├── contact_form.py        # Contact form
│   ├── contact_header.py      # Contact page header
│   ├── contact_info.py        # Contact information display
│   ├── contact_info_grid.py   # Contact info grid layout
│   └── map_card.py            # Interactive map card
├── sections/                  # Page section components
│   ├── __init__.py
│   ├── hero.py                # Hero section
│   ├── services.py            # Services section
│   ├── expertise.py           # Expertise section
│   ├── values.py              # Values section
│   ├── cta.py                 # Call-to-action section
│   ├── our_history.py         # History section
│   ├── locations.py           # Locations section
│   └── faq_section.py         # FAQ section
└── products/                  # Product-related components
    ├── __init__.py
    ├── products_page.py       # Products page layout
    ├── featured_products.py   # Featured products display
    └── shop_categories.py     # Shop categories display
```

## Changes Made

### 1. Created Subfolders
- **`layout/`** - Core layout components (header, footer, layout, burger_menu)
- **`ui/`** - Reusable UI components (dropdown, error_404)
- **`contact/`** - Contact-related components (5 files)
- **`sections/`** - Page section components (8 files)
- **`products/`** - Product-related components (3 files)

### 2. Updated Imports
All internal imports were updated to reflect the new structure:

#### Files with updated imports:
- `src/components/layout/header.py` - Updated burger_menu import
- `src/components/layout/footer.py` - Updated contact_info import
- `src/components/contact/contact_info.py` - Updated contact_form import
- `src/components/contact/map_card.py` - Updated dropdown import
- `src/components/sections/services.py` - Updated create_service_card import
- `src/components/products/products_page.py` - Updated dropdown import
- `src/routes/error_404.py` - Updated error_404 import

### 3. Created __init__.py Files
Each subfolder has its own `__init__.py` that exports its components:
- `layout/__init__.py` - Exports Layout, create_header, create_footer, burger menu functions
- `ui/__init__.py` - Exports create_dropdown, create_404_page
- `contact/__init__.py` - Exports all contact-related functions
- `sections/__init__.py` - Exports all section creation functions
- `products/__init__.py` - Exports all product-related functions

### 4. Updated Main __init__.py
The main `src/components/__init__.py` now imports from submodules and maintains backward compatibility with existing code.

## Benefits

1. **Better Organization** - Related components are grouped together
2. **Easier Navigation** - Clear separation of concerns
3. **Maintainability** - Easier to find and update specific component types
4. **Scalability** - Easy to add new components to appropriate folders
5. **Backward Compatibility** - All existing imports still work through main __init__.py

## Usage

All existing code continues to work without changes:

```python
from src.components import Layout, create_header, create_footer
from src.components import create_hero, create_services
from src.components import create_contact_form, create_dropdown
```

You can also import directly from submodules if needed:

```python
from src.components.layout import Layout, create_header
from src.components.ui import create_dropdown
from src.components.contact import create_contact_form
```

## Testing

✅ All imports tested and verified
✅ Application starts successfully
✅ No breaking changes to existing code
