from datetime import datetime
from sqlalchemy import Column, String, Integer, TIMESTAMP, BigInteger
from Backend.alchemy_models.main.global_base import Base

class User(Base):
    __tablename__ = "d_user"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False, index=True, unique=True)
    first_name = Column(String(length=100), nullable=True)
    last_name = Column(String(length=100), nullable=True)
    username = Column(String(length=100), nullable=True, index=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)
    last_active_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)