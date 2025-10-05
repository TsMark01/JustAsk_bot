from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, Text, TIMESTAMP, ForeignKey, Boolean
from Backend.alchemy_models.local.global_base import Base

class UserPrompts(Base):
    __tablename__ = "user_prompts"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("d_user.user_id"), nullable=False, index=True)
    prompt_text = Column(Text, nullable=False)
    is_custom = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False, index=True)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)
