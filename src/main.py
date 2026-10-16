from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.products.routes import product_router
from src.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

version = "v1"
app = FastAPI(
    lifespan=lifespan,
    version=version
    )

app.include_router(product_router,prefix=f"/api/{version}/products")