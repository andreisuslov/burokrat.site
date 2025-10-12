# Burokrat.site - "Burokrat" Company

Official website of "Burokrat" company - seals and stamps manufacturing in Barnaul, Russia.

[🇷🇺 Русская версия](README_RU.md)

## 📋 Table of Contents

- [Tech Stack](#tech-stack)
- [About](#about)
- [Project Structure](#project-structure)
- [Installation & Running](#installation--running)
- [Features](#features)
- [Development](#development)
- [Deployment](#deployment)
- [Contact Information](#contact-information)

## 🛠 Tech Stack

- **Backend**: [FastHTML](https://github.com/AnswerDotAI/fasthtml) - modern Python framework for web development
- **Frontend**: HTMX for dynamic interactions without JavaScript
- **Data**: YAML for structured data storage
- **Styling**: Vanilla CSS with CSS variables
- **Server**: Uvicorn (ASGI server)

## 📖 About

Website for "Burokrat" company specializing in:
- 🖨️ **Seals and Stamps** - production of any complexity
- 🔧 **Self-Inking Stamps** - wide range of automatic stamp holders
- ✨ **Engraving** - on metal, plastic, wood
- 📝 **Stationery** - complete office supplies assortment

## 📁 Project Structure

```
burokrat.site/
├── app.py                  # Main FastHTML application
├── main_page.yaml          # Main page data source
├── requirements.txt        # Python dependencies
├── run.sh                  # Quick start script
├── README.md               # Main README
├── README_RU.md            # Russian documentation
├── README_EN.md            # English documentation
├── .gitignore              # Git ignore file
└── assets/                 # Static resources
    ├── images/            # Images
    ├── styles/
    │   └── main.css       # Main stylesheet
    └── fonts/             # Fonts
```

## 🚀 Installation & Running

### Requirements
- Python 3.10 or higher
- pip (Python package manager)

### Quick Start

#### Option 1: Using the script (recommended)
```bash
./run.sh
```

#### Option 2: Manual start
```bash
# 1. Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run application
python3 app.py
```

### Open in Browser
```
http://localhost:5001
```

## ✨ Features

### Main Pages
- **`/`** - Home page with services overview
- **`/seals-and-stamps`** - Seals and stamps
- **`/self-inking-stamps`** - Self-inking stamp holders
- **`/engraving`** - Engraving services
- **`/stationery`** - Stationery products

### FastHTML + HTMX Benefits
- ⚡ **Rapid development** - write in Python instead of JavaScript
- 🔄 **Dynamic updates** - without page reloads
- 📱 **Responsive design** - adaptive layout
- 🎨 **Modern UI** - gradients, animations, hover effects
- 📧 **Modal forms** - for customer contact
- 🔥 **Live reload** - automatic refresh on changes

### HTMX Endpoints
- **`/contact-form`** - Load contact modal form
- **`/submit-contact`** - Handle form submission

## 💻 Development

### Live Reload
FastHTML includes automatic reload on file changes. Simply:
1. Modify files (`app.py`, CSS)
2. Save changes
3. Browser automatically refreshes

### Editing Data
All company data is stored in `main_page.yaml`:
- Company name
- Contact information (phones, emails, addresses)
- Navigation menu
- Office hours
- SEO meta tags

After changing `main_page.yaml`, restart the application.

### Adding New Pages

1. **Add route in `app.py`:**
```python
@rt('/new-page')
def get():
    return Layout(
        'Page Title',
        Section(
            H1('Heading'),
            P('Page content'),
            cls='page-content'
        )
    )
```

2. **Add link in `main_page.yaml`:**
```yaml
navigation:
  main_menu:
    - label: New Page
      url: /new-page
```

### Customizing Styles

Edit `assets/styles/main.css`. Use CSS variables for consistency:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    /* modify as needed */
}
```

### Component Structure

**Layout** - main layout:
```python
def Layout(title, *content):
    # Generates HTML with header, main, footer
```

**create_header()** - site header with navigation  
**create_footer()** - footer with contacts  
**create_service_card()** - service card component

## 🌐 Deployment

### Local Testing
```bash
python3 app.py
```

### Production with Gunicorn
```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:8000 --workers 4
```

### Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 5001

# Run application
CMD ["python3", "app.py"]
```

Build and run:
```bash
docker build -t burokrat-site .
docker run -p 5001:5001 burokrat-site
```

### Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5001:5001"
    volumes:
      - ./main_page.yaml:/app/main_page.yaml
    restart: unless-stopped
```

Run:
```bash
docker-compose up -d
```

## 📞 Contact Information

### Phones:
- **8(3852) 62-82-82** - main office
- **25-14-91** - additional number
- **8(3852) 53-20-46** - office
- **8-964-603-20-46** - seals and stamps department

### Email:
- L628282@yandex.ru
- s628282@gmail.com

### Addresses:

**Office 1:** Sotsialisticheskiy Prospekt, 109, Barnaul, Altai Krai  
**Hours:** Mon-Sun 09:30 - 18:30 (no lunch break)

**Office 2:** Stroiteley Prospekt, 4, Barnaul, Altai Krai  
**Hours:** Mon-Sun 09:30 - 18:30 (no lunch break)

## 🌍 Domain

**Current address:** https://burokrat.site  
**Previous address (Wix):** https://l628282.wixsite.com/seals

## 📝 License

© 2025 "Burokrat" Company. All rights reserved.

## 🤝 Support

If you have questions or issues:
1. Check the documentation
2. Contact us by phone or email
3. Create an issue in the repository (if applicable)

---

Made with ❤️ for "Burokrat" Company
