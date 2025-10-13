#!/usr/bin/env python3
"""
Static site generator for Burokrat.site FastHTML application
Generates static HTML files for deployment to Netlify
"""

import os
import shutil
from pathlib import Path
from fasthtml.common import *
from src.config import load_page_data
from src.routes import register_all_routes

def create_static_site():
    """Generate static HTML files from FastHTML application"""
    
    # Create dist directory
    dist_dir = Path("dist")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # Copy assets
    assets_src = Path("assets")
    assets_dst = dist_dir / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, assets_dst)
        print(f"✅ Copied assets to {assets_dst}")
    
    # Initialize FastHTML app
    app, rt = fast_app(
        hdrs=(
            Link(rel='stylesheet', href='/assets/styles/main.css'),
            Script(src='https://unpkg.com/htmx.org@1.9.10'),
        ),
        live=False
    )
    
    # Load configuration data
    load_page_data()
    
    # Register all routes
    register_all_routes(rt)
    
    # Define pages to generate
    pages = [
        ('/', 'index.html'),
        ('/seals-and-stamps', 'seals-and-stamps.html'),
        ('/self-inking-stamps', 'self-inking-stamps.html'),
        ('/engraving', 'engraving.html'),
        ('/stationery', 'stationery.html'),
        ('/products-and-services', 'products-and-services.html'),
        ('/about', 'about.html'),
        ('/contact', 'contact.html'),
    ]
    
    print("🏗️  Generating static pages...")
    
    # Generate each page
    for route, filename in pages:
        try:
            # Use Starlette's TestClient directly
            from starlette.testclient import TestClient
            client = TestClient(app)
            
            # Get the page content
            response = client.get(route)
            
            if response.status_code == 200:
                # Write HTML file
                html_file = dist_dir / filename
                html_file.write_text(response.text, encoding='utf-8')
                print(f"✅ Generated {filename}")
            else:
                print(f"❌ Failed to generate {filename} (status: {response.status_code})")
                
        except Exception as e:
            print(f"❌ Error generating {filename}: {str(e)}")
    
    print(f"\n🎉 Static site generated successfully in {dist_dir}/")
    print(f"📁 Total files: {len(list(dist_dir.rglob('*')))}")

if __name__ == "__main__":
    create_static_site()
