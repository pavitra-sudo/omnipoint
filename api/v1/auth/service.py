from sqlalchemy.orm import Session

from api.v1.user.model import User
from api.v1.auth.jwt_handler import create_access_token
from security.hash import verify_password


def login_user(
    mobile: str,
    password: str,
    db: Session,
):
    user = (
        db.query(User)
        .filter(User.mobile == mobile)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password,
    ):
        return None

    return {
        "access_token": create_access_token(user.id), #type: ignore
        "token_type": "bearer",
    }