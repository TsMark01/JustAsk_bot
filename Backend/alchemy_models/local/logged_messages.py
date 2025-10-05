from sqlalchemy import Column, String, Integer, BigInteger, VARCHAR, DateTime
from datetime import datetime
from Backend.alchemy_models.local.global_base import Base

class MessageLog(Base):
    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    username = Column(String(255), nullable=True)
    message_id = Column(BigInteger, nullable=False)
    text = Column(VARCHAR(length=4000), nullable=True)
    topic_name = Column(String(255), nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)