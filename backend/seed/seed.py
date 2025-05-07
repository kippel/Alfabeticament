from sqlalchemy.orm import Session
from fastapi.params import Depends

from backend.security import get_db
#from backend.db.models import Silaba, SilabaUn, SilabaUser, Flag, Abc
from backend.db.models import Flag, Abc, AbcItem
from gtts import gTTS
import hashlib
import secrets
import os

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



class seed_abc_item:

    @staticmethod
    def delete(db: Session = Depends(get_db)):
        abc = db.query(AbcItem).all()

        for i in abc:
            db.delete(i)
            db.commit()


        
        dir_path = r"../frontend/public/vocals"
        # List all files in the directory
        for filename in os.listdir(dir_path):
            
            file_path = os.path.join(dir_path, filename)
        
            # Check if it is a file (not a subdirectory)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Remove the file



    @staticmethod
    def abc(abc_item, db: Session = Depends(get_db)):
        for r in abc_item:

            # todo: 
            voice_app = seed_abc_item.mp3(r['vocals'])

            abc_app = AbcItem(
                lletra=r["lletra"],
                numbro=r["numbro"],
                vocals=r["vocals"],
                voice=voice_app
            )



            db.add(abc_app)
            db.commit()

    @staticmethod
    def mp3(vocals): 

        salt = secrets.token_hex(16)
        hash_object = hashlib.sha256(salt.encode())
        hash_hex = hash_object.hexdigest()

        tts = gTTS(text=vocals,lang='ca',slow=False)
        tts.save(f"../frontend/public/vocals/{hash_hex}.mp3")
        

        return f"/vocals/{hash_hex}.mp3"
        

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