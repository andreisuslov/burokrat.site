"""Database configuration and utilities"""
import logging
from pathlib import Path
from typing import Generator
from sqlmodel import SQLModel, Session, create_engine

# Database configuration
DATABASE_DIR = Path(__file__).parent.parent / "data"
DATABASE_DIR.mkdir(exist_ok=True)
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/burokrat.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Set to True to see SQL queries in logs
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

def create_db_and_tables():
    """Create all database tables"""
    logging.info(f"📊 Creating database tables at {DATABASE_DIR}/burokrat.db")
    SQLModel.metadata.create_all(engine)
    logging.info("✅ Database tables created successfully")

def get_session() -> Generator[Session, None, None]:
    """Get a database session
    
    Usage in routes:
        with get_session() as session:
            # do database operations
    """
    with Session(engine) as session:
        yield session

def get_db_session() -> Session:
    """Get a database session (simpler version)
    
    Usage in routes:
        session = get_db_session()
        # do database operations
        session.commit()
        session.close()
    """
    return Session(engine)
