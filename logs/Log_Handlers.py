from sqlalchemy.orm import Session
from models import LogEntry

def create_log(level: str, message: str, db: Session):
    """Create a new log entry."""
    new_log = LogEntry(level=level, message=message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log
