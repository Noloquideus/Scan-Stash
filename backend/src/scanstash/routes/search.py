from typing import Optional

from fastapi import APIRouter, Cookie, Depends

from scanstash.interfaces.auth_service import AuthService
from scanstash.interfaces.search_service import SearchService


search_router = APIRouter(prefix="/search")

@search_router.post("")
async def search(
    auth_service: AuthService = Depends(),
    search_sevice: SearchService = Depends(),
    session_id: Optional[str] = Cookie(None),
):
    user_id = auth_service.authenticate(session_id)
    return search_sevice.search(user_id)

