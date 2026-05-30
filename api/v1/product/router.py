from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from api.v1.product import service
from api.v1.product.schema import (
    ProductCreateRequest,
    ProductCreateResponse,
)

router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"],
)


@router.post(
    "/",
    response_model=ProductCreateResponse,
    status_code=201,
)
def create_product(
    payload: ProductCreateRequest,
    db: Session = Depends(get_db),
):
    try:
        product = service.create_product(
            payload=payload,
            db=db,
        )

        return product

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )