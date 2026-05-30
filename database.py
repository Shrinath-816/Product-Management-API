from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


#db_url = "postgresql//postgres:your_password@localhost:5432/fastapi_db"
db_url = "postgresql+psycopg2://postgres:your_password@localhost:5432/fastapi_db"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Shrinathtop1 - 6 line p
