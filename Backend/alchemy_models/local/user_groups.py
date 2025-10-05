from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, BigInteger, VARCHAR

from Backend.alchemy_models.local.global_base import Base

class UserGroups(Base):
    __tablename__ = "user_groups"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, nullable=False, index=True)
    telegram_username = Column(VARCHAR(length=100), nullable=True, index=True)
    group_id = Column(BigInteger, nullable=False, index=True)
    group_name = Column(VARCHAR(length=100), nullable=False, index=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False, index=True)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)