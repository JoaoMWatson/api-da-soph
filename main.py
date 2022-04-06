from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from custom_openapi import custom_openapi

app = FastAPI()
app.openapi = custom_openapi(app)


class Product(BaseModel):
    id: int | None
    name: str
    size: str


class Products(BaseModel):
    count: int
    produtos: list[Product]


@app.get('/', status_code=200, response_model=Products)
def produtos():
    """Retorna produtos"""
    return Products(count=1, produtos=[Product(id=1, name='eu', size='m')])


@app.get('/healthcheck')
def healthcheck():
    """Status da aplicação"""
    return {'status': 'ok'}
