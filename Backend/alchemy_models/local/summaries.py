from sqlalchemy import Column, Integer, BigInteger, Text, TIMESTAMP, ForeignKey
from Backend.alchemy_models.local.global_base import Base

class Summaries(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    group_id = Column(BigInteger, ForeignKey("user_groups.group_id"), nullable=False, index=True)
    summary_text = Column(Text, nullable=False)
    generated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", nullable=False, index=True)
    message_count = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", nullable=False, index=True)
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP", index=True)