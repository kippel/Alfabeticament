from typing import Annotated 
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


from dotenv import load_dotenv
import os
from .db.database import SessionLocal

load_dotenv()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

