# Database Setup with SQLModel

## Overview

This project uses **SQLModel** with **SQLite** for database management. SQLModel is created by the same author as FastAPI and provides a seamless integration between SQLAlchemy and Pydantic.

## Architecture

### Database Location
- **File**: `data/burokrat.db`
- **Type**: SQLite (file-based, no server required)

### Structure

```
src/
├── db.py                    # Database configuration and connection
├── models/                  # Database models
│   ├── __init__.py
│   └── contact.py          # ContactSubmission model
└── routes/
    ├── contact.py          # Contact form with DB integration
    └── admin.py            # Admin panel to view submissions
```

## Features

### 1. Contact Submissions Storage
Every contact form submission is automatically saved to the database with:
- Contact information (name, email, phone, company)
- Message details (subject, message content)
- Email delivery status (success/error)
- Timestamp

### 2. Admin Panel
Access the admin panel to view all submissions:
- **URL**: `http://localhost:8080/admin/submissions`
- View all contact submissions in a table
- See email delivery status
- Click "Подробнее" (Details) to view full submission

## Database Models

### ContactSubmission Model

```python
class ContactSubmission(SQLModel, table=True):
    id: Optional[int]           # Auto-increment primary key
    name: str                   # Contact name
    email: str                  # Contact email
    phone: Optional[str]        # Phone number
    subject: Optional[str]      # Message subject
    message: str                # Message content
    company: Optional[str]      # Company name
    created_at: datetime        # Submission timestamp
    email_sent: bool            # Email delivery status
    email_error: Optional[str]  # Error message if email failed
```

## Usage Examples

### Querying the Database

```python
from src.db import get_db_session
from src.models import ContactSubmission
from sqlmodel import select

# Get a session
session = get_db_session()

# Get all submissions
statement = select(ContactSubmission).order_by(ContactSubmission.created_at.desc())
submissions = session.exec(statement).all()

# Get a specific submission by ID
submission = session.get(ContactSubmission, id)

# Filter submissions
statement = select(ContactSubmission).where(ContactSubmission.email_sent == True)
successful_submissions = session.exec(statement).all()

# Close the session
session.close()
```

### Creating a New Submission

```python
from src.db import get_db_session
from src.models import ContactSubmission

session = get_db_session()

# Create new submission
submission = ContactSubmission(
    name="Иван Иванов",
    email="ivan@example.com",
    phone="+7 (999) 123-45-67",
    subject="Вопрос о печатях",
    message="Хочу заказать печать",
    company="ООО Ромашка",
    email_sent=True
)

# Save to database
session.add(submission)
session.commit()
session.refresh(submission)  # Get the auto-generated ID

print(f"Created submission with ID: {submission.id}")
session.close()
```

## Database Management

### Automatic Initialization
The database is automatically created when the application starts:
```python
# In app.py
from src.db import create_db_and_tables
create_db_and_tables()
```

### Manual Database Operations

**View database in terminal:**
```bash
sqlite3 data/burokrat.db
sqlite> .tables
sqlite> SELECT * FROM contact_submissions;
sqlite> .exit
```

**Reset database:**
```bash
# Delete the database file
rm data/burokrat.db
# Restart the application - it will recreate the database
python app.py
```

## Benefits of SQLModel

1. **Type Safety**: Full type hints and IDE autocomplete
2. **Data Validation**: Automatic validation with Pydantic
3. **FastAPI Integration**: Perfect compatibility with FastAPI
4. **SQLAlchemy Power**: Full SQL capabilities when needed
5. **Simple Syntax**: Easy to learn and use
6. **Migration Ready**: Can easily switch to PostgreSQL/MySQL later

## Adding New Models

To add a new database model:

1. Create the model in `src/models/`:
```python
# src/models/product.py
from sqlmodel import Field, SQLModel
from typing import Optional

class Product(SQLModel, table=True):
    __tablename__ = "products"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    price: float
    description: str
```

2. Import it in `src/models/__init__.py`:
```python
from .contact import ContactSubmission
from .product import Product

__all__ = ['ContactSubmission', 'Product']
```

3. Import it in `app.py` to register it:
```python
from src.models import ContactSubmission, Product
```

4. Restart the application - the table will be created automatically

## Security Notes

- The admin panel at `/admin/submissions` is **not password-protected**
- In production, add authentication middleware
- Consider adding environment-based access control
- The database file contains customer data - ensure proper backups

## Next Steps

Consider implementing:
- [ ] Admin authentication
- [ ] Export submissions to CSV
- [ ] Search and filter functionality
- [ ] Pagination for large datasets
- [ ] Database migrations with Alembic
- [ ] Backup automation
- [ ] Analytics dashboard

## Resources

- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
