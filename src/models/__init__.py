"""Database models for burokrat.site"""
from .contact import ContactSubmission
from .product import Product, Category

__all__ = ['ContactSubmission', 'Product', 'Category']
