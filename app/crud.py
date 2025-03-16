from sqlalchemy.orm import Session
from . import models, schemas

def create_obat(db: Session, obat: schemas.ObatCreate):
    db_obat = models.Obat(**obat.dict())
    db.add(db_obat)
    db.commit()
    db.refresh(db_obat)
    return db_obat

def get_obat(db: Session, obat_id: int):
    return db.query(models.Obat).filter(models.Obat.id == obat_id).first()

def get_all_obat(db: Session):
    return db.query(models.Obat).all()
