from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.security import get_db
#from backend.db.models import Silaba, SilabaUn, SilabaUser, Flag, Abc
from backend.db.models import Flag, Abc

class seed_language:

    @staticmethod
    def seed_flag_delete(db: Session = Depends(get_db)):
        flag_app = db.query(Flag).all()

        for r in flag_app:
            db.delete(r)
            db.commit()

    @staticmethod
    def seed_flag(language, db: Session = Depends(get_db)):
        for r in language:

            flag_app = Flag(
                flag=r['flag'],
                icon=r['icon'],
                language=r['language']
            )
            db.add(flag_app)
            db.commit()

class seed_abc:
    
    @staticmethod
    def delete(db: Session = Depends(get_db)):
        abc = db.query(Abc).all()

        for i in abc:
            db.delete(i)
            db.commit()

    @staticmethod
    def abc(abc, db: Session = Depends(get_db)):
        for r in abc:
            abc_app = Abc(
                abc=r["abc"],
                href=r["href"],
                icon=r["icon"],
                width=r['width'],
                height=r['height']
            )
            db.add(abc_app)
            db.commit()

'''
class seeds_silaba:
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

        for r in silaba['silaba']:
            sil = Silaba(
                silaba=r['silaba'],
                silaba_id=r['silaba_id']
            )
            db.add(sil)
            db.commit()

        for i in silaba['silaba_un']:
            
            mon = SilabaUn(
                nom=i['name'],
                order=i['order'],
                silabaun_id=i['silabaun_id']
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
'''