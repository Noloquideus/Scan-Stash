from typing import Optional


class AuthService:  # нужно ли сюда передавать connection
    def register(self, username: str, password: str) -> str:
        raise NotImplementedError

    def login(self, username: str, password: str) -> str:
        raise NotImplementedError

    def authenticate(self, session_id: Optional[str]) -> str:
        raise NotImplementedError
