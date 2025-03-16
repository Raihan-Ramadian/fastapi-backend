from pydantic import BaseModel

class ObatBase(BaseModel):
    nama: str
    komposisi: str
    khasiat: str
    efek_samping: str
    kontra_indikasi: str
    indikasi: str
    harga: int
    golongan: str

class ObatCreate(ObatBase):
    pass

class ObatResponse(ObatBase):
    id: int

    class Config:
        orm_mode = True
