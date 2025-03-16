from sqlalchemy import Column, Integer, String
from .database import Base

class Obat(Base):
    __tablename__ = "obat"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(255), unique=True, index=True)
    komposisi = Column(String(255))
    khasiat = Column(String(255))
    efek_samping = Column(String(255))
    kontra_indikasi = Column(String(255))
    indikasi = Column(String(255))
    harga = Column(Integer)
    golongan = Column(String(255))
