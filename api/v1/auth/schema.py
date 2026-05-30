from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    mobile: str = Field(..., min_length=10, max_length=15)
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"