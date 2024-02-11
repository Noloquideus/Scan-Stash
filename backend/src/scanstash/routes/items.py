from typing import Optional

from fastapi import APIRouter, Depends, Cookie

from scanstash.interfaces.auth_service import AuthService


items_router = APIRouter()


@items_router.get("/items")
async def get_items(
    auth_service: AuthService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    auth_service.authenticate(session_id)
    return [{"item": 1}]


#это просто тестовая хуйня