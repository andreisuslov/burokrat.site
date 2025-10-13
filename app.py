"""
Burokrat.site - Main Application Entry Point
A modular FastHTML application for a Russian seals and stamps company.
"""

from fasthtml.common import *
from fastapi import FastAPI
from src.config import load_page_data
from src.routes import register_all_routes

# Initialize FastHTML app (ASGI app)
fh_app, rt = fast_app(
    hdrs=(
        Link(rel='stylesheet', href='/assets/styles/main.css'),
        Script(src='https://unpkg.com/htmx.org@1.9.10'),
    ),
    live=True
)

# Load configuration data
load_page_data()

# Register all routes into FastHTML router
register_all_routes(rt)

# Create FastAPI app and mount the FastHTML app at root
app = FastAPI(title="Burokrat.site")
app.mount("/", fh_app)

@app.get("/api/health")
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
