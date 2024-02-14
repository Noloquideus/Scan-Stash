from typing import Optional

from pydantic import BaseModel
from fastapi import APIRouter, Cookie, Depends

from scanstash.interfaces.auth_service import AuthService
from scanstash.interfaces.produtc_service import ProductService


product_router = APIRouter(prefix="/product")


class ProductSchema(BaseModel):
    name: str
    qr_txt: str
    about: Optional[str]


@product_router.post("/add")
async def add(
    data: ProductSchema,
    auth_service: AuthService = Depends(),
    product_service: ProductService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    """
    TODO
    """
    ...
    # user_id = auth_service.authenticate(session_id)
    # product_service.add()
    # return True
