from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.db import get_db
from api.v1.user.schema import (
    CreateRequest as UserCreate,
    CreateResponse,
)
from api.v1.user.service import create_user_service



router = APIRouter(
    prefix="/api/v1/create",
    tags=["create"],
)


@router.post(
    "/",
    response_model=CreateResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user_service(payload, db)


