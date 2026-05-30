from importlib import reload

from fastapi import FastAPI
from api.v1.user.route import router as create_router
from api.v1.auth.router import router as auth_router
from api.v1.product.router import router as product_router
from database.db import Base, engine
from middleware.auth import AuthMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(AuthMiddleware)
app.include_router(create_router)
app.include_router(auth_router)
app.include_router(product_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)