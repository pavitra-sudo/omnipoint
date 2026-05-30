from sqlalchemy.orm import Session
from api.v1.auth.schema import LoginRequest
from api.v1.user.model import User
from api.v1.auth.jwt_handler import create_access_token
from security.hash import verify_password


def login_user(
    payload: LoginRequest,
    db: Session,
):
    user = (
        db.query(User)
        .filter(User.mobile == payload.mobile)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        payload.password,
        user.password,
    ):
        return None

    return {
        "access_token": create_access_token(user.id), #type: ignore
        "token_type": "bearer",
    }