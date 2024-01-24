from .db import SessionLocal


def get_db():
    """Accesses a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
