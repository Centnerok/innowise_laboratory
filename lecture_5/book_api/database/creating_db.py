from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base, Book

DB_URL = 'sqlite:///lecture_5/book_api/database/database.db'
engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)