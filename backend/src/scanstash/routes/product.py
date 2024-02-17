from typing import Optional

from pydantic import BaseModel
from fastapi import APIRouter, Cookie, Depends

from scanstash.interfaces.auth_service import AuthService
from scanstash.interfaces.produtc_service import ProductService


product_router = APIRouter(prefix="/product")


class AddProductSchema(BaseModel):
    product_name: str
    qr_txt: str
    about: Optional[str]
    place_name: Optional[str]


@product_router.post("/add")
async def add(
    data: AddProductSchema,
    auth_service: AuthService = Depends(),
    product_service: ProductService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    user_id = auth_service.authenticate(session_id)
    product_service.add(
        place_name=data.place_name,
        name=data.product_name,
        qr_txt=data.qr_txt,
        about=data.about,
        user_id=user_id,
    )
    return True


class DeleteProductSchema(BaseModel):
    product_name: str
    place_name: str


@product_router.delete("/delete")
async def delete(
    data: DeleteProductSchema,
    auth_service: AuthService = Depends(),
    product_service: ProductService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    user_id = auth_service.authenticate(session_id)
    product_service.delete(
        user_id=user_id[0],
        place_name=data.place_name,
        product_name=data.product_name,
    )
    return True


class GetInfoProductSchema(BaseModel):
    product_name: str
    place_name: str


@product_router.post("/get_info")
async def get_info(
    data: GetInfoProductSchema,
    auth_service: AuthService = Depends(),
    product_service: ProductService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    user_id = auth_service.authenticate(session_id)
    return product_service.get_info(
        user_id=user_id[0],
        place_name=data.place_name,
        product_name=data.product_name,
    )
