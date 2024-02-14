from fastapi import APIRouter, Response, Depends
from pydantic import BaseModel

from scanstash.interfaces.auth_service import AuthService


auth_router = APIRouter(prefix="/auth")


class RegisterSchema(BaseModel):
    username: str
    password: str


@auth_router.post("/register")
async def register(
    data: RegisterSchema,
    response: Response,
    auth_service: AuthService = Depends(),
):
    session_id = auth_service.register(
        username=data.username,
        password=data.password,
    )
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return True


class LoginSchema(BaseModel):
    username: str
    password: str


@auth_router.post("/login")
async def login(
    data: LoginSchema,
    response: Response,
    auth_service: AuthService = Depends(),
):
    session_id = auth_service.login(
        username=data.username,
        password=data.password,
    )
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return True
