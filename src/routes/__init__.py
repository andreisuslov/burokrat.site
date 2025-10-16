from .home import register_home_route
from .about import register_about_route
from .seals_stamps import register_seals_stamps_route
from .self_inking_stamps import register_self_inking_stamps_route
from .engraving import register_engraving_route
from .stationery import register_stationery_route
from .contact import register_contact_routes
from .admin import register_admin_routes
from .static_files import register_static_route
from .privacy import register_privacy_route
from .clients import register_clients_route
from .agreement import register_agreement_route
from .products_services import register_products_services_route
from .featured_products import register_featured_products_route
from .error_404 import register_404_handler

def register_all_routes(rt):
    """Register all application routes."""
    register_home_route(rt)
    register_about_route(rt)
    register_seals_stamps_route(rt)
    register_self_inking_stamps_route(rt)
    register_engraving_route(rt)
    register_stationery_route(rt)
    register_contact_routes(rt)
    register_admin_routes(rt)
    register_static_route(rt)
    register_privacy_route(rt)
    register_clients_route(rt)
    register_agreement_route(rt)
    register_products_services_route(rt)
    register_featured_products_route(rt)
    register_404_handler(rt)
