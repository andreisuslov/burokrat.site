"""
Burokrat.site - Main Application Entry Point
A modular FastHTML application for a Russian seals and stamps company.
"""

import logging

# Configure logging with a clear format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)

from fasthtml.common import *
from fastapi import FastAPI
from src.config import load_page_data
from src.routes import register_all_routes
from src.db import create_db_and_tables
from src.models import ContactSubmission, Product, Category  # Import models to register them

# Initialize FastHTML app (ASGI app)
fh_app, rt = fast_app(
    hdrs=(
        Link(rel='stylesheet', href='/assets/styles/main.css'),
        Script(src='https://unpkg.com/htmx.org@1.9.10'),
        Script(src='/assets/scripts/css-hot-reload.js'),
    ),
    live=True
)

# Load configuration data
load_page_data()

# Initialize database
create_db_and_tables()

# Register all routes into FastHTML router
register_all_routes(rt)

# Add default 404 handler for FastHTML (must be after all routes)
from src.components.ui import create_404_page
from src.components import Layout

async def custom_404_handler(scope, receive, send):
    """Custom 404 error handler."""
    from starlette.requests import Request
    from starlette.responses import HTMLResponse
    
    request = Request(scope, receive=receive)
    logging.info(f"🚫 404 Error: {request.url.path} not found")
    
    html_content = Layout(
        '404 - Page Not Found',
        Main(
            create_404_page(),
            cls='error-404-page'
        )
    )
    
    response = HTMLResponse(content=to_xml(html_content), status_code=404)
    await response(scope, receive, send)

# Set the default exception handler for 404 errors
fh_app.router.default = custom_404_handler

# Create FastAPI app and mount the FastHTML app at root
app = FastAPI(title="burokrat.site")
app.mount("/", fh_app)

@app.get("/api/health")
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    import uvicorn
    logging.info("🚀 Starting burokrat.site server on http://0.0.0.0:8080")
    uvicorn.run("app:app", host="0.0.0.0", port=8080, log_level="info", reload=True)
