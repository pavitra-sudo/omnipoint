from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from api.v1.auth.schema import LoginRequest, LoginResponse
from api.v1.auth.service import login_user

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
):
    result = login_user(
        mobile=payload.mobile,
        password=payload.password,
        db=db,
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid mobile number or password",
        )

    return result