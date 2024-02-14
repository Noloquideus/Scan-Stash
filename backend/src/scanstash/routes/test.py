from typing import Optional

from fastapi import APIRouter, Depends, Cookie

from scanstash.interfaces.auth_service import AuthService


test_router = APIRouter(prefix="/test")


@test_router.get("/test")
async def get_test(
    auth_service: AuthService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    user_id = auth_service.authenticate(session_id)
    return [{"user_id": user_id}]
