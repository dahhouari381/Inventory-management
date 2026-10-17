from fastapi import APIRouter,status,Depends
from fastapi.exceptions import HTTPException
from .models import Product,UpdateProduct
from ..database import get_session 
from sqlmodel import Session ,select

product_router = APIRouter()

@product_router.get("/")
def get_products(session:Session=Depends(get_session)):
    products = session.exec(select(Product))
    return products.all()


@product_router.get("/{product_id}")
def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return product



@product_router.post("/",status_code=status.HTTP_201_CREATED)
def create_product(product: Product,
                 session:Session=Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)

    return product

@product_router.patch("/{product_id}")
def update_product(
    product_id: int,
    product_data: UpdateProduct,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if product_data.name is not None:
        product.name = product_data.name

    if product_data.desription is not None:
        product.desription = product_data.desription

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


@product_router.delete("/{product_id}")
def delete_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    session.delete(product)
    session.commit()

    return {"message": "Product deleted"}