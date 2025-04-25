from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, status

from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.db.models import Silaba
from backend.security import get_db

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"]
)



@router.get("/")
async def get_workouts(db: Session = Depends(get_db)):
    silaba = db.query(Silaba).all()
    print(silaba)
    return {"silaba": silaba}