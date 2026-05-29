from pydantic import BaseModel
from pydantic import Field




class CreateRequest(BaseModel):
    name: str
    mobile: int
    password: str = Field(..., min_length=8)
    
class CreateResponse(BaseModel):
    id: int
    name: str
    mobile: int
    
    class Config:
        from_attributes = True