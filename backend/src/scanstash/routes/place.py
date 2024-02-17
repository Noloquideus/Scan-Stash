from typing import Optional

from fastapi import APIRouter, Cookie, Depends
from pydantic import BaseModel

from scanstash.interfaces.auth_service import AuthService
from scanstash.interfaces.place_service import PlaceService


place_router = APIRouter(prefix="/place")


class AddPlaceSchema(BaseModel):
    name: str
    qr_txt: str
    about: Optional[str]


@place_router.post("/add")
async def add(
    data: AddPlaceSchema,
    auth_service: AuthService = Depends(),
    place_service: PlaceService = Depends(),
    session_id: Optional[str] = Cookie(None),
) -> bool:
    user_id = auth_service.authenticate(session_id)
    place_service.add(
        user_id=user_id,
        name=data.name,
        qr_txt=data.qr_txt,
        about=data.about,
    )
    return True


class DeletePlaceSchema(BaseModel):
    name: str


@place_router.delete("/delete")
async def delete(
    data: DeletePlaceSchema,
    auth_service: AuthService = Depends(),
    place_service: PlaceService = Depends(),
    session_id: Optional[str] = Cookie(None),
) -> bool:
    user_id = auth_service.authenticate(session_id)
    place_service.delete(
        user_id=user_id,
        name=data.name,
    )
    return True


class GetInfoPlaceSchema(BaseModel):
    place_name: Optional[str]


@place_router.post("/get_info")
async def get_info(
    data: DeletePlaceSchema,
    auth_service: AuthService = Depends(),
    place_service: PlaceService = Depends(),
    session_id: Optional[str] = Cookie(None),
) -> dict:
    user_id = auth_service.authenticate(session_id)
    return place_service.get_info(
        user_id=user_id,
        name=data.name,
    )


# @place_router.patch("/get")
# async def change_info(
#     data: PatchPlaceSchema,
#     auth_service: AuthService = Depends(),
#     place_service: PlaceService = Depends(),
#     session_id: Optional[str] = Cookie(None),
# ) -> None:
#     data
#     ...
