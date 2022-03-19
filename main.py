from typing import Optional

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    id: int | None
    name: str
    size: str


class Products(BaseModel):
    count: int
    produtos: list[Product]


@app.get('/', status_code=200, response_model=Products)
def first_route():
    """Retorna produtos"""
    return Products(count=1, produtos=[Product(id=1, name='eu', size='m')])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Api de produtos',
        version='0.1.0',
        description='Essa api de produtos é daora d+',
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
