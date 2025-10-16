#!/usr/bin/env python3
"""Database utility script for common database operations"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.db import get_db_session, create_db_and_tables, DATABASE_DIR
from src.models import ContactSubmission, Product, Category
from sqlmodel import select


def list_submissions():
    """List all contact submissions"""
    print("\n📊 Contact Submissions")
    print("=" * 80)
    
    session = get_db_session()
    try:
        statement = select(ContactSubmission).order_by(ContactSubmission.created_at.desc())
        submissions = session.exec(statement).all()
        
        if not submissions:
            print("📭 No submissions found")
            return
        
        for sub in submissions:
            status = "✅" if sub.email_sent else "❌"
            print(f"\n{status} ID: {sub.id} | {sub.created_at.strftime('%Y-%m-%d %H:%M')}")
            print(f"   Name: {sub.name}")
            print(f"   Email: {sub.email}")
            print(f"   Phone: {sub.phone or '-'}")
            print(f"   Subject: {sub.subject or '-'}")
            print(f"   Message: {sub.message[:50]}..." if len(sub.message) > 50 else f"   Message: {sub.message}")
            if not sub.email_sent and sub.email_error:
                print(f"   Error: {sub.email_error}")
        
        print(f"\n{'=' * 80}")
        print(f"Total: {len(submissions)} submissions")
        
    finally:
        session.close()


def show_stats():
    """Show database statistics"""
    print("\n📈 Database Statistics")
    print("=" * 80)
    
    session = get_db_session()
    try:
        # Contact submissions
        total = len(session.exec(select(ContactSubmission)).all())
        successful = len(session.exec(
            select(ContactSubmission).where(ContactSubmission.email_sent == True)
        ).all())
        failed = total - successful
        
        print(f"\n📧 Contact Submissions:")
        print(f"   Total: {total}")
        print(f"   Email Sent: {successful}")
        print(f"   Email Failed: {failed}")
        if total > 0:
            success_rate = (successful / total) * 100
            print(f"   Success Rate: {success_rate:.1f}%")
        
        # Products
        total_products = len(session.exec(select(Product)).all())
        featured_products = len(session.exec(
            select(Product).where(Product.featured == True)
        ).all())
        active_products = len(session.exec(
            select(Product).where(Product.active == True)
        ).all())
        
        print(f"\n📦 Products:")
        print(f"   Total: {total_products}")
        print(f"   Active: {active_products}")
        print(f"   Featured: {featured_products}")
        
        # Categories
        total_categories = len(session.exec(select(Category)).all())
        active_categories = len(session.exec(
            select(Category).where(Category.active == True)
        ).all())
        
        print(f"\n📂 Categories:")
        print(f"   Total: {total_categories}")
        print(f"   Active: {active_categories}")
        
        print("=" * 80)
        
    finally:
        session.close()


def create_test_submission():
    """Create a test submission"""
    print("\n🧪 Creating test submission...")
    
    session = get_db_session()
    try:
        test_sub = ContactSubmission(
            name="Test User",
            email="test@example.com",
            phone="+7 (999) 123-45-67",
            subject="Test Subject",
            message="This is a test message for database testing purposes.",
            company="Test Company LLC",
            email_sent=True,
            email_error=None
        )
        
        session.add(test_sub)
        session.commit()
        session.refresh(test_sub)
        
        print(f"✅ Test submission created with ID: {test_sub.id}")
        
    except Exception as e:
        print(f"❌ Error creating test submission: {e}")
        session.rollback()
    finally:
        session.close()


def reset_database():
    """Reset the database (WARNING: deletes all data)"""
    print("\n⚠️  WARNING: This will delete all data!")
    confirm = input("Type 'YES' to confirm: ")
    
    if confirm == "YES":
        db_file = Path(DATABASE_DIR) / "burokrat.db"
        if db_file.exists():
            db_file.unlink()
            print("🗑️  Database deleted")
        
        create_db_and_tables()
        print("✅ Database recreated")
    else:
        print("❌ Operation cancelled")


def list_products():
    """List all products"""
    print("\n📦 Products")
    print("=" * 80)
    
    session = get_db_session()
    try:
        statement = select(Product).order_by(Product.category_id, Product.id)
        products = session.exec(statement).all()
        
        if not products:
            print("📭 No products found")
            return
        
        current_category = None
        for prod in products:
            if prod.category_id != current_category:
                current_category = prod.category_id
                print(f"\n📁 {current_category.upper()}")
            
            featured = "⭐" if prod.featured else "  "
            active = "✓" if prod.active else "✗"
            print(f"{featured} [{active}] {prod.name} - ${prod.price} (⭐{prod.rating})")
        
        print(f"\n{'=' * 80}")
        print(f"Total: {len(products)} products")
        
    finally:
        session.close()


def list_categories():
    """List all categories"""
    print("\n📂 Categories")
    print("=" * 80)
    
    session = get_db_session()
    try:
        statement = select(Category).order_by(Category.sort_order)
        categories = session.exec(statement).all()
        
        if not categories:
            print("📭 No categories found")
            return
        
        for cat in categories:
            active = "✓" if cat.active else "✗"
            product_count = len(session.exec(
                select(Product).where(Product.category_id == cat.id)
            ).all())
            print(f"[{active}] {cat.name} ({cat.id}) - {product_count} products")
            print(f"    {cat.description}")
            print(f"    URL: {cat.url}")
        
        print(f"\n{'=' * 80}")
        print(f"Total: {len(categories)} categories")
        
    finally:
        session.close()


def show_help():
    """Show available commands"""
    print("\n🛠️  Database Utility Tool")
    print("=" * 80)
    print("Available commands:")
    print("  list       - List all contact submissions")
    print("  products   - List all products")
    print("  categories - List all categories")
    print("  stats      - Show database statistics")
    print("  test       - Create a test submission")
    print("  reset      - Reset database (deletes all data)")
    print("  help       - Show this help message")
    print("=" * 80)


def main():
    """Main entry point"""
    # Ensure database tables exist
    create_db_and_tables()
    
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        list_submissions()
    elif command == "products":
        list_products()
    elif command == "categories":
        list_categories()
    elif command == "stats":
        show_stats()
    elif command == "test":
        create_test_submission()
    elif command == "reset":
        reset_database()
    elif command == "help":
        show_help()
    else:
        print(f"❌ Unknown command: {command}")
        show_help()


if __name__ == "__main__":
    main()
