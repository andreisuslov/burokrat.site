# Quick Start: SQLModel Database Integration

## ✅ What Was Implemented

Your FastAPI/FastHTML application now has a fully integrated SQLite database using SQLModel!

### Features Added:
1. **Database Models** - Contact submission model with full data validation
2. **Automatic Storage** - All contact form submissions are saved to database
3. **Admin Panel** - View all submissions at `/admin/submissions`
4. **Database Utilities** - Command-line tool for database management

## 🚀 Quick Start

### 1. Start the Application

```bash
python3 app.py
```

The database will be automatically created at `data/burokrat.db` on first run.

### 2. Test the Contact Form

Visit `http://localhost:8080/contact` and submit a form. The submission will be:
- Saved to the database ✅
- Email sent via SendGrid (if configured) 📧
- Available in the admin panel 👀

### 3. View Submissions in Admin Panel

Open `http://localhost:8080/admin/submissions` to see all contact form submissions.

### 4. Use Database Utilities

```bash
# View all submissions
python3 db_utils.py list

# Show statistics
python3 db_utils.py stats

# Create test data
python3 db_utils.py test

# Show help
python3 db_utils.py help
```

## 📁 Project Structure

```
burokrat.site/
├── data/
│   └── burokrat.db          # SQLite database (auto-created)
├── src/
│   ├── db.py                # Database configuration
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   └── contact.py       # ContactSubmission model
│   └── routes/
│       ├── contact.py       # Contact form (saves to DB)
│       └── admin.py         # Admin panel (views DB)
├── db_utils.py              # Database utility script
└── DATABASE_SETUP.md        # Full documentation
```

## 🔍 Database Schema

**contact_submissions** table:
- `id` - Auto-increment primary key
- `name` - Contact name
- `email` - Contact email
- `phone` - Phone number (optional)
- `subject` - Message subject (optional)
- `message` - Message content
- `company` - Company name (optional)
- `created_at` - Submission timestamp
- `email_sent` - Email delivery status (boolean)
- `email_error` - Error message if email failed

## 🔌 API Usage Examples

### Query Submissions in Your Code

```python
from src.db import get_db_session
from src.models import ContactSubmission
from sqlmodel import select

session = get_db_session()

# Get all submissions
submissions = session.exec(
    select(ContactSubmission).order_by(ContactSubmission.created_at.desc())
).all()

# Get submissions where email failed
failed = session.exec(
    select(ContactSubmission).where(ContactSubmission.email_sent == False)
).all()

session.close()
```

### Create New Submission Programmatically

```python
from src.db import get_db_session
from src.models import ContactSubmission

session = get_db_session()

submission = ContactSubmission(
    name="Иван Иванов",
    email="ivan@example.com",
    message="Тестовое сообщение",
    email_sent=True
)

session.add(submission)
session.commit()
session.close()
```

## 🛡️ Important Notes

1. **Admin Panel Security**: The `/admin/submissions` route is **not password-protected**. Add authentication before deploying to production!

2. **Database Backups**: The database file is at `data/burokrat.db`. Make regular backups in production.

3. **Database Migrations**: Currently using automatic table creation. For production, consider using Alembic for migrations.

## 🎯 Next Steps

Consider implementing:
- [ ] Admin authentication (basic auth or OAuth)
- [ ] Export submissions to CSV/Excel
- [ ] Email notifications for new submissions
- [ ] Search and filter in admin panel
- [ ] Pagination for large datasets
- [ ] Archive old submissions
- [ ] Dashboard with analytics

## 📚 Documentation

- Full documentation: [DATABASE_SETUP.md](./DATABASE_SETUP.md)
- SQLModel docs: https://sqlmodel.tiangolo.com/
- FastAPI docs: https://fastapi.tiangolo.com/

## 🧪 Testing

```bash
# Create test submission
python3 db_utils.py test

# View it in the database
python3 db_utils.py list

# Check statistics
python3 db_utils.py stats
```

## 🐛 Troubleshooting

**Database not found?**
- Start the application once to create the database
- Or run `python3 db_utils.py test` to initialize

**Import errors?**
- Make sure SQLModel is installed: `pip install sqlmodel`
- Check `requirements.txt` is updated

**Can't see submissions?**
- Check the logs when submitting a form
- Verify `data/burokrat.db` exists
- Use `python3 db_utils.py list` to check directly

## ✨ Summary

You now have a production-ready database integration that:
- ✅ Stores all contact submissions permanently
- ✅ Tracks email delivery status
- ✅ Provides admin interface for viewing submissions
- ✅ Includes command-line utilities for management
- ✅ Uses type-safe, validated models
- ✅ Integrates seamlessly with FastAPI/FastHTML

**Database location**: `data/burokrat.db`  
**Admin panel**: `http://localhost:8080/admin/submissions`  
**Database tool**: `python3 db_utils.py`

Enjoy your new database! 🎉
