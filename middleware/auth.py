from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")



class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        public_routes = {
            "/docs",
            "/redoc",
            "/openapi.json",
            "/api/v1/login",
            "/api/v1/create",
        }

        if request.url.path in public_routes:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authorization header missing"}
            )

        try:
            scheme, token = auth_header.split()

            if scheme.lower() != "bearer":
                raise ValueError("Invalid auth scheme")

            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM] #type: ignore
            )

            request.state.user = payload

        except jwt.ExpiredSignatureError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Token has expired"}
            )

        except jwt.InvalidTokenError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid token"}
            )

        except Exception:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authentication failed"}
            )

        return await call_next(request)