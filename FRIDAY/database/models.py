from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class FileLog(Base):
    __tablename__ = "file_logs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    path = Column(String)
    action = Column(String) # Created, Read, Deleted
    timestamp = Column(DateTime, default=datetime.utcnow)
    description = Column(String, nullable=True)
