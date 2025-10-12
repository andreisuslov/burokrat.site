from fasthtml.common import *
from src.config import get_data
from .header import create_header
from .footer import create_footer

def Layout(title, *content, header=None, footer=None, sidebar=None, head_meta=None):
    """Main page layout with header/footer slots and optional sidebar.

    Args:
        title: Page title for the document head and layout title.
        *content: Main content nodes (Sections, etc.).
        header: Optional header node or callable returning nodes. Defaults to create_header().
        footer: Optional footer node or callable returning nodes. Defaults to create_footer().
        sidebar: Optional node or callable for sidebar. When provided, main area renders in two columns.
        head_meta: Optional dict to override meta tags (description, keywords, og fields, canonical_url, title).
    """
    data = get_data()

    def _resolve(comp, default_factory):
        if comp is None:
            return default_factory()
        if callable(comp):
            return comp()
        return comp
    
    def _as_nodes(x):
        if x is None:
            return []
        if isinstance(x, (list, tuple)):
            return list(x)
        return [x]

    # Resolve meta with overrides
    hm = head_meta or {}
    meta_desc = hm.get('description', data['description'])
    meta_keywords = hm.get('keywords', data['keywords'])
    mt = data.get('meta_tags', {})
    og_title = hm.get('og:title', mt.get('title', title))
    og_desc = hm.get('og:description', mt.get('description', data.get('description', '')))
    og_url = hm.get('og:url', mt.get('url', data.get('site_url', '')))
    og_type = hm.get('og:type', mt.get('type', 'website'))
    canonical_url = hm.get('canonical_url', data['canonical_url'])

    # Resolve header/footer/sidebar nodes
    header_nodes = _as_nodes(_resolve(header, create_header))
    footer_nodes = _as_nodes(_resolve(footer, create_footer))
    sidebar_nodes = _as_nodes(_resolve(sidebar, lambda: None)) if sidebar is not None else None

    # Build main content with optional sidebar layout
    if sidebar_nodes is not None:
        main_node = Main(
            Div(*sidebar_nodes, cls='sidebar'),
            Div(*content, cls='main-with-sidebar'),
            id='main-content',
            cls='content-with-sidebar container'
        )
    else:
        main_node = Main(*content, id='main-content', cls='container')

    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Meta(name='description', content=meta_desc),
            Meta(name='keywords', content=meta_keywords),
            # Open Graph meta tags
            Meta(property='og:title', content=og_title),
            Meta(property='og:description', content=og_desc),
            Meta(property='og:url', content=og_url),
            Meta(property='og:type', content=og_type),
            Link(rel='canonical', href=canonical_url),
            Link(rel='icon', type='image/png', href='/assets/images/icon.png'),
            Title(title or 'Бюрократ'),
            Link(rel='stylesheet', href='/assets/styles/main.css'),
            Script(src='https://unpkg.com/htmx.org@1.9.10'),
        ),
        Body(
            Header(*header_nodes),
            main_node,
            Footer(*footer_nodes),
        ),
        lang=data['language']
    )
