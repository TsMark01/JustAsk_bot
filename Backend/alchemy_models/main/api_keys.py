from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, Text, TIMESTAMP, ForeignKey, Boolean
from Backend.alchemy_models.main.global_base import Base

class ApiKeys(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("d_user.user_id"), nullable=True, index=True)
    model_id = Column(Integer, ForeignKey("model_settings.id"), nullable=False, index=True)
    api_key = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", nullable=False, index=True)
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP", index=True)