from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from api.v1.user.model import User
from api.v1.user.schema import CreateRequest
from security.hash import get_password_hash


def create_user_service(
    payload: CreateRequest,
    db: Session,
):
    # Check if user already exists
    existing_user = (
        db.query(User)
        .filter(User.mobile == payload.mobile)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this mobile number already exists.",
        )

    # Hash password
    hashed_password = get_password_hash(payload.password)

    # Create user
    new_user = User(
        name=payload.name,
        mobile=payload.mobile,
        password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user