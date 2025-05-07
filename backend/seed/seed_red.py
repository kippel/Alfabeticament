from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.security import get_db
from backend.seed.seed import seed_language, seed_abc, seed_abc_item
import json

def red_language(db: Session = Depends(get_db)):

    seed_language.seed_flag_delete(db)

    with open("seed/work/language.json", 'r') as file:
        dict = json.load(file)
    #print(dict)
    seed_language.seed_flag(dict['language'], db)

'''
def red_silaba(db: Session = Depends(get_db)):

    Seeds.seed_silaba(db)
    Seeds.seed_silaba_uns(db)
    Seeds.seed_silaba_user(db)
    
    ## todo
    with open("seed/config.yaml", 'r') as file:
        config = json.load(file)

    Seeds.seed_silaba_bar(config, db)
'''
def red_abc(db: Session = Depends(get_db)):
    seed_abc.delete(db)

    with open("seed/work/abc.json", 'r') as file:
        config = json.load(file)

    seed_abc.abc(config['abc'], db)

def red_abc_items(db: Session = Depends(get_db)):
    seed_abc_item.delete(db)
    with open("seed/work/abc_item.json", 'r') as file:
        config = json.load(file)
    seed_abc_item.abc(config['abc_item'], db)