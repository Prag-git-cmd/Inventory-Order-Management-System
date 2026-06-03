from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database import get_db
from . import crud, schemas

router = APIRouter()

@router.get("/")
def home():
    return {"message": "API Running"}

@router.post("/products")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
