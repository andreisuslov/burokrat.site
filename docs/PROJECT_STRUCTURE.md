# Project Structure

This document explains the modular organization of the Burokrat.site application.

## Directory Layout

```
burokrat.site/
├── app.py                      # Main application entry point (27 lines)
├── src/                        # Source code package
│   ├── config/                 # Configuration & data accessors
│   │   ├── __init__.py
│   │   └── data_loader.py      # YAML data loading & cached getters
│   ├── components/             # Reusable UI components
│   │   ├── __init__.py
│   │   ├── layout.py           # Base HTML layout
│   │   ├── header.py           # Header with logo and navigation
│   │   ├── footer.py           # Footer with contact info
│   │   └── contact_info.py     # Contact sections and cards
│   ├── pages/                  # Per-page view modules (render())
│   │   ├── __init__.py
│   │   ├── home/               # Home page content
│   │   ├── about/              # About page content
│   │   ├── clients/            # Clients page content
│   │   └── privacy/            # Privacy page content
│   ├── routes/                 # Route handlers (one file per page)
│   │   ├── __init__.py
│   │   ├── home.py
│   │   ├── about.py
│   │   ├── clients.py
│   │   ├── privacy.py
│   │   ├── seals_stamps.py
│   │   ├── self_inking_stamps.py
│   │   ├── engraving.py
│   │   ├── stationery.py
│   │   ├── contact.py
│   │   └── static_files.py
│   └── utils/                  # Shared utilities
│       └── phone_formatter.py
├── data/                       # YAML content per page
│   ├── main_page.yaml
│   ├── about.yaml
│   ├── clients.yaml
│   ├── contact.yaml
│   ├── privacy.yaml
│   ├── seals_stamps.yaml
│   ├── self_inking_stamps.yaml
│   └── stationery.yaml
├── assets/                     # Static assets
│   ├── images/                 # Images (logo.png, icon.png, etc.)
│   ├── styles/                 # CSS files (e.g. main.css)
│   ├── scripts/                # JavaScript files (e.g. contact-form.js)
│   └── fonts/                  # Custom fonts
├── requirements.txt
├── run.sh                      # Startup script
├── README.md
├── README_EN.md
├── README_RU.md
├── PROJECT_STRUCTURE.md
└── .gitignore

```

## Package Overview

### `app.py` (Main Entry Point)
- Initializes the FastHTML application
- Loads configuration data
- Registers all routes
- Now only **27 lines** instead of 353!

### `src/config/`
**Purpose**: Configuration and data management

- `data_loader.py`: Loads and caches YAML configuration data

### `src/components/`
**Purpose**: Reusable UI components

- `layout.py`: Main HTML layout with head tags, meta data
- `header.py`: Header with logo and navigation menu
- `footer.py`: Footer with company info, phones, emails, addresses
- `contact_info.py`: Contact information sections and service cards

### `src/pages/`
**Purpose**: Page-level view modules responsible for main content of a page.

- Each page has a `view.py` exposing a `render()` function that returns content nodes.
- Example: `src/pages/clients/view.py` defines `render()` to build sections "Доставка", "Оплата", "Гарантия" using `data/clients.yaml` via `get_clients_data()`.

### `src/routes/`
**Purpose**: Route handlers (one file per page/feature)

- `home.py`: Home page route
- `about.py`: About page route
- `clients.py`: Clients info page (Доставка, Оплата, Гарантия)
- `privacy.py`: Privacy policy page
- `seals_stamps.py`: Seals and stamps product page
- `self_inking_stamps.py`: Self-inking stamps catalog
- `engraving.py`: Engraving services page
- `stationery.py`: Stationery products page
- `contact.py`: Contact form and submission handlers
- `static_files.py`: Serves static assets (CSS, images, etc.)

### `src/utils/`
**Purpose**: Small helpers shared across modules

- `phone_formatter.py`: Formats phone numbers for display and tel: links

## Benefits of This Structure

1. **Easy Navigation**: Each file has a single, clear responsibility
2. **Maintainability**: Changes to one page don't affect others
3. **Scalability**: Easy to add new pages or components
4. **Reusability**: Components can be reused across pages
5. **Testing**: Each module can be tested independently
6. **Team Collaboration**: Multiple developers can work on different files

## Adding New Pages

To add a new page:

1. Create a view module in `src/pages/<name>/view.py` that exposes `render()`.
2. Create a route in `src/routes/<name>.py` that wraps the view in `Layout` and defines the URL.
3. Import and register the new route in `src/routes/__init__.py`.

Examples:
```python
# src/pages/new_page/view.py
from fasthtml.common import *

def render():
    return (
        Section(H1('New Page'), P('Content here')),
    )
```

```python
# src/routes/new_page.py
from fasthtml.common import *
from src.components import Layout
from src.pages.new_page.view import render as render_new_page

def register_new_page_route(rt):
    @rt('/new-page')
    def get():
        return Layout('New Page Title', *render_new_page())
```

```python
# src/routes/__init__.py
from .new_page import register_new_page_route

def register_all_routes(rt):
    # ... existing routes
    register_new_page_route(rt)
```

## Adding New Components

Create new component files in `src/components/` and export them via `__init__.py`.

## Data Management

All site data YAML files live under the `data/` directory.

- At startup, `load_page_data()` loads `data/main_page.yaml` and caches it.
- Page-specific data is loaded lazily via getters from `src.config`, for example:
  - `get_about_data()`
  - `get_privacy_data()`
  - `get_contact_data()`
  - `get_seals_stamps_data()`
  - `get_self_inking_stamps_data()`
  - `get_stationery_data()`
  - `get_clients_data()`

Example (Clients page):
```python
from src.config import get_clients_data

data = get_clients_data()
title = data['title']
```
