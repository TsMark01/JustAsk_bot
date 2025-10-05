from sqlalchemy import create_engine
from Backend.config import SQLALCHEMY_MAIN_DATABASE_URL
from Backend.alchemy_models.main.global_base import Base

import Backend.alchemy_models.main.d_user
import Backend.alchemy_models.main.model_settings
import Backend.alchemy_models.main.api_keys

def create_all():
    engine = create_engine(SQLALCHEMY_MAIN_DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    print("Tables created in the main db")

create_all()
