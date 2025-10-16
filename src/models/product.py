"""Product database models"""
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Category(SQLModel, table=True):
    """Product category model"""
    
    __tablename__ = "categories"
    
    id: str = Field(primary_key=True, max_length=100)  # e.g., "writing-instruments"
    name: str = Field(max_length=255)
    description: Optional[str] = Field(default="", max_length=500)
    icon: Optional[str] = Field(default="", max_length=255)
    color: Optional[str] = Field(default="bg-blue-500", max_length=100)
    url: Optional[str] = Field(default="", max_length=255)
    sort_order: int = Field(default=0)
    active: bool = Field(default=True)
    
    # Relationship
    # products: list["Product"] = Relationship(back_populates="category_rel")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "writing-instruments",
                "name": "Письменные принадлежности",
                "description": "Ручки, карандаши и маркеры",
                "icon": "/assets/images/pen.svg",
                "color": "bg-blue-500",
                "url": "/products/writing-instruments"
            }
        }


class Product(SQLModel, table=True):
    """Product model"""
    
    __tablename__ = "products"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, index=True)
    category_id: str = Field(foreign_key="categories.id", max_length=100)
    price: float = Field(gt=0)
    image: str = Field(max_length=1000)
    rating: float = Field(default=0.0, ge=0, le=5)
    reviews: int = Field(default=0, ge=0)
    badge: Optional[str] = Field(default="", max_length=100)
    in_stock: bool = Field(default=True)
    description: Optional[str] = Field(default="", max_length=2000)
    
    # Metadata
    featured: bool = Field(default=False)
    active: bool = Field(default=True)
    sort_order: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship
    # category_rel: Optional[Category] = Relationship(back_populates="products")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Набор премиальных перьевых ручек",
                "category_id": "writing-instruments",
                "price": 89.99,
                "image": "https://images.unsplash.com/photo-123...",
                "rating": 4.9,
                "reviews": 124,
                "badge": "Бестселлер",
                "in_stock": True,
                "featured": True
            }
        }
