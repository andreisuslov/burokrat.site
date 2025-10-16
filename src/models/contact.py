"""Contact submission database model"""
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class ContactSubmission(SQLModel, table=True):
    """Model for storing contact form submissions"""
    
    __tablename__ = "contact_submissions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    email: str = Field(max_length=255)
    phone: Optional[str] = Field(default="", max_length=50)
    subject: Optional[str] = Field(default="", max_length=255)
    message: str = Field(default="")
    company: Optional[str] = Field(default="", max_length=255)
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.utcnow)
    email_sent: bool = Field(default=False)
    email_error: Optional[str] = Field(default=None, max_length=500)
    
    class Config:
        """Pydantic config"""
        json_schema_extra = {
            "example": {
                "name": "Иван Иванов",
                "email": "ivan@example.com",
                "phone": "+7 (999) 123-45-67",
                "subject": "Заказ печати",
                "message": "Хочу заказать печать для ООО",
                "company": "ООО Ромашка"
            }
        }
