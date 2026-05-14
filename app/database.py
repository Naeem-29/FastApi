from sqlalchemy import create_engine #for database connection
from sqlalchemy.ext.declarative import declarative_base #base class for our models
from sqlalchemy.orm import sessionmaker #to run database queries sesion toirir kaj korbe

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@Localhost/firstday'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()