from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, status

from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.db.models import Silaba, Flag, SilabaUn
from backend.security import get_db

router = APIRouter( )



@router.get("/silaba", tags=["silaba"])
async def get_workouts(db: Session = Depends(get_db)):
    silaba = db.query(Silaba).all()
    print(silaba)
    return {"silaba": silaba}

@router.get("/silabaun", tags=["silaba"])
async def get_silabaun(db: Session = Depends(get_db)):
    silaba_un = db.query(SilabaUn).all()
    print(silaba_un)
    return {"silabaun": silaba_un}



@router.get("/flag", tags=["flag"])
async def get_flag(db: Session = Depends(get_db)):
    flag_app = db.query(Flag).all()
    
    return {"flag": flag_app}