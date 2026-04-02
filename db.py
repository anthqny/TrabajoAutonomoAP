from sqlmodel import create_engine

DATABASE_URL = "database-1.cpimmamw0aq9.us-east-2.rds.amazonaws.com"

engine = create_engine(DATABASE_URL, echo=True)