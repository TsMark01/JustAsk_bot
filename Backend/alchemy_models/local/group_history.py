from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, BigInteger, ForeignKey, Text, VARCHAR
from Backend.alchemy_models.local.global_base import Base

class GroupHistory(Base):
    __tablename__ = "group_history"
    id = Column(Integer, primary_key=True)
    group_id = Column(BigInteger, ForeignKey("user_groups.group_id"), nullable=False, index=True)  # Связь с UserGroups
    user_id = Column(BigInteger, nullable=False, index=True)
    username = Column(VARCHAR(100), nullable=True)
    request_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False, index=True)

