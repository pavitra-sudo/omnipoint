from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    isbn = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float)
    in_stock = Column(Integer)

