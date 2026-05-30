from sqlalchemy.orm import Session

from api.v1.product.model import Product
from api.v1.product.schema import ProductCreateRequest


def create_product(
    payload: ProductCreateRequest,
    db: Session,
):
    if payload.price <= 0:
        raise ValueError("Price must be greater than 0")

    if payload.in_stock < 0:
        raise ValueError("Stock cannot be negative")

    existing_product = (
        db.query(Product)
        .filter(Product.isbn == payload.isbn)
        .first()
    )

    if existing_product:
        raise ValueError("Product with this ISBN already exists")

    product = Product(
        name=payload.name,
        isbn=payload.isbn,
        description=payload.description,
        price=payload.price,
        in_stock=payload.in_stock,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product