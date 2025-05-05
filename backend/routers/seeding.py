from fastapi import APIRouter, HTTPException
# db
from sqlalchemy.orm import Session
from fastapi.params import Depends

#from backend.seed.seed import Seeds
from backend.seed.seed_red import red_language, red_abc



from backend.security import get_db

import yaml
import json

router = APIRouter(
    prefix="/seed",
    tags=["seed"]
)

@router.get("/test/language")
def get_language(db: Session = Depends(get_db)):

    red_language(db)

    
    return {"language": "language"}

@router.get("/test/abc")
def get_abc(db: Session = Depends(get_db)):

    red_abc(db)

    return {"abc": "abc"}

'''
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
'''