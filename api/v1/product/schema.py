from pydantic import BaseModel, Field
from typing import Optional


class ProductCreateRequest(BaseModel):
    name: str = Field(... )
    isbn: str = Field(..., min_length=10, max_length=13)
    description: Optional[str] = Field(None)
    price: float = Field(...)
    in_stock: int = Field(...)
    
class ProductCreateResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True