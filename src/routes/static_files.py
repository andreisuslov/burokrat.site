from fasthtml.common import *

def register_static_route(rt):
    """Register static file serving route."""
    
    @rt('/assets/{filepath:path}')
    def get(filepath: str):
        return FileResponse(f'assets/{filepath}')
