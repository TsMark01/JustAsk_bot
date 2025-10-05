from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, TIMESTAMP, VARCHAR
from Backend.alchemy_models.main.global_base import Base

class ModelSettings(Base):
    __tablename__ = "model_settings"
    id = Column(Integer, primary_key=True)
    model_name = Column(VARCHAR(100), nullable=False, unique=True)
    api_endpoint = Column(VARCHAR(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False, index=True)
