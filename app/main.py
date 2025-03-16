from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/obat/", response_model=schemas.ObatResponse)
def create_obat(obat: schemas.ObatCreate, db: Session = Depends(get_db)):
    return crud.create_obat(db=db, obat=obat)

@app.get("/obat/{obat_id}", response_model=schemas.ObatResponse)
def get_obat(obat_id: int, db: Session = Depends(get_db)):
    obat = crud.get_obat(db=db, obat_id=obat_id)
    if not obat:
        return {"error": "Obat tidak ditemukan"}
    return obat

@app.get("/obat/", response_model=list[schemas.ObatResponse])
def get_all_obat(db: Session = Depends(get_db)):
    return crud.get_all_obat(db=db)
