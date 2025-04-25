from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.security import get_db
from backend.db.models import Silaba, SilabaUn, SilabaUser

class Seeds:
    @staticmethod
    def seed_silaba(db: Session = Depends(get_db)):
        """
        Seed silaba
        """
        silaba = db.query(Silaba).all()
        
        for r in silaba:
            db.delete(r)
            db.commit()

    @staticmethod
    def seed_silaba_uns(db: Session = Depends(get_db)):
        
        silaba_un = db.query(SilabaUn).all()
        
        for r in silaba_un:
            
            db.delete(r)
            db.commit()
    
    @staticmethod
    def seed_silaba_user(db: Session = Depends(get_db)):
        
        silaba_user = db.query(SilabaUser).all()
        
        for r in silaba_user:
            
            db.delete(r)
            db.commit()
    
    @staticmethod
    def seed_silaba_bar(silaba, db: Session = Depends(get_db)):
        """
        Seed silaba
        """
        for r in silaba['silaba']:
            sil = Silaba(
                silaba=r['silaba']
            )
            db.add(sil)
            db.commit()

        for i in silaba['silaba_un']:
            
            mon = SilabaUn(
                nom=i['name'],
                order=i['order'],
                silaba_id=i['silaba_id']
            )
            db.add(mon)
            db.commit()

        for y in silaba['silabs_user']:
            
            mon = SilabaUser(
                nom=y['nom'],
                icon=y['icon'],
                owner_id=y['owner_id']
            )
            db.add(mon)
            db.commit()