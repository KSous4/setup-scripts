from sqlalchemy import Column, Integer, String, DateTime
import datetime
from db_setup.database import Base

class LogEntry(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return (f"<LogEntry(id={self.id}, level='{self.level}', "
                f"message='{self.message}', timestamp='{self.timestamp}')>")
