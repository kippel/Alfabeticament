from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from .database import Base

class Flag(Base):
    __tablename__ = "flag"
    id = Column(Integer, primary_key=True)
    flag = Column(String)
    icon = Column(String)
    language = Column(String)


class Abc(Base):
    __tablename__ = "abc"
    id = Column(Integer, primary_key=True)
    abc = Column(String)
    href = Column(String)
    icon = Column(String)
    width = Column(Integer)
    height = Column(Integer)

class Silaba(Base):
    __tablename__ = "silaba"

    id = Column(Integer, primary_key=True)
    silaba = Column(String)
    #owner_id = Column(Integer, ForeignKey('silabaun.order')) 
    #silaba_id = relationship("SilabaUn", backref="silabas")
    #order = Column(String)
    silaba_id = Column(Integer) #, ForeignKey('silaba_id.silabaun_id'))

class SilabaUn(Base):
    __tablename__ = "silabaun"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    order = Column(Integer)

    silabaun_id = Column(Integer) #, ForeignKey('silaba_id.silabaun_id'))

    #silaba_id = Column(Integer, ForeignKey('silaba.id'))
    #monousers = relationship("SilabaUser", backref="silabaun")


class SilabaUser(Base):
    __tablename__ = "silabauser"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    icon = Column(String)
    owner_id = Column(Integer, ForeignKey('silabaun.order'))   