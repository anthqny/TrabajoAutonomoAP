from sqlmodel import create_engine

DATABASE_URL = "postgresql://postgres:anthony1234@api-db.cmtg60ucs2lz.us-east-1.rds.amazonaws.com:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)