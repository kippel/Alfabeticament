from fastapi import APIRouter, HTTPException
# db
from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.seed.seed import Seeds

from backend.security import get_db

import yaml

router = APIRouter(
    prefix="/seed",
    tags=["seed"]
)

@router.get("/test/silaba")
def getSilaba(db: Session = Depends(get_db)):
    
    Seeds.seed_silaba(db)
    Seeds.seed_silaba_uns(db)
    Seeds.seed_silaba_user(db)
    Seeds.seed_flag(db)

    with open("seed/config.yaml", 'r') as file:
        config = yaml.safe_load(file)

    Seeds.seed_silaba_bar(config, db)
    
    
    
    return {"monosillabs": "monosillabs"}