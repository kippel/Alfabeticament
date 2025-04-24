from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from .database import Base


class Silaba(Base):
    __tablename__ = "silaba"

    id = Column(Integer, primary_key=True)
    silaba = Column(String)

    silaba_id = relationship("SilabaUn", backref="silabas")

class SilabaUn(Base):
    __tablename__ = "silabaun"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    order = Column(Integer)
    silaba_id = Column(Integer, ForeignKey('silaba.id'))
    monousers = relationship("SilabaUser", backref="silabaun")


class SilabaUser(Base):
    __tablename__ = "silabauser"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    icon = Column(String)
    owner_id = Column(Integer, ForeignKey('silabaun.order'))   