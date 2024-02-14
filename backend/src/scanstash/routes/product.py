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
