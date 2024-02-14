from typing import Optional

from fastapi import APIRouter, Cookie, Depends
from pydantic import BaseModel

from scanstash.interfaces.auth_service import AuthService
from scanstash.interfaces.place_service import PlaceService


place_router = APIRouter(prefix="/place")


class PlaceSchema(BaseModel):
    name: str
    qr_txt: str
    about: Optional[str]


@place_router.post("/add")
async def add(
    data: PlaceSchema,
    auth_service: AuthService = Depends(),
    place_service: PlaceService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    user_id = auth_service.authenticate(session_id)
    place_service.add(
        user_id=user_id,
        name=data.name,
        qr_txt=data.qr_txt,
        about=data.about,
    )
    return True
