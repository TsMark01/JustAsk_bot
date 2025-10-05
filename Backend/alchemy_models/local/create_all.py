from sqlalchemy import create_engine
from Backend.config import SQLALCHEMY_MAIN_DATABASE_URL
from Backend.alchemy_models.local.global_base import Base

import Backend.alchemy_models.local.user_groups
import Backend.alchemy_models.local.group_history
import Backend.alchemy_models.local.logged_messages
import Backend.alchemy_models.local.summaries

def create_all():
    engine = create_engine(SQLALCHEMY_MAIN_DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    print("Tables created in the local db")

create_all()
