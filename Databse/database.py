from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./user.db"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})
Sessionlocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()



def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()