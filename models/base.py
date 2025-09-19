from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# MySQL engine
engine = create_engine("mysql+mysqlconnector://root@localhost/hrms")

