from typing import Optional


class AuthService():
    def register(self, username: str, password: str) -> str:
        raise NotImplementedError
    
    def login(self, username: str, password: str) -> str:
        raise NotImplementedError

    def authenticate(self, session_id: Optional[str]) -> None:
        raise NotImplementedError 
    