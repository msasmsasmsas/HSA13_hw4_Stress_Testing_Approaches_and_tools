from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class RequestData(Base):
    __tablename__ = "request_data"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True)
    value = Column(String, index=True)


Base.metadata.create_all(bind=engine)


class Data(BaseModel):
    key: str
    value: str


@app.post("/data/")
async def store_data(data: Data):
    db = SessionLocal()
    db_data = RequestData(key=data.key, value=data.value)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    db.close()
    return {"message": "Data stored successfully"}


@app.get("/data/")
async def get_data():
    db = SessionLocal()
    result = db.query(RequestData).all()
    db.close()
    return result
