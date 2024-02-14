from typing import Optional

from uuid import uuid4
from fastapi import HTTPException


class AuthServiceImpl:
    def __init__(self, connection) -> None:
        self._connection = connection

    def register(
        self,
        username: str,
        password: str,
    ) -> str:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1 FROM users u WHERE u.username = %s
                """,
                (username,),
            )
            name_is_taken = cursor.fetchone()
            if name_is_taken:
                raise HTTPException(400, "Username is taken")

            cursor.execute(
                """
                INSERT INTO users
                (username, password) VALUES (%s, %s)
                RETURNING id
                """,
                (username, password),
            )
            user_id = cursor.fetchone()

            session_id = uuid4().hex
            cursor.execute(
                """
                INSERT INTO sessions
                (id, user_id) VALUES (%s, %s)
                """,
                (session_id, user_id),
            )
            self._connection.commit()
        return session_id

    def login(self, username: str, password: str) -> str:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, password FROM users u WHERE u.username = %s
                """,
                (username,),
            )
            data = cursor.fetchone()
            if not data:
                raise HTTPException(400, "User not found")
            if data[1] != password:
                raise HTTPException(400, "Inccoret password")

            cursor.execute(
                """
                SELECT id FROM sessions s WHERE s.user_id = %s
                """,
                (data[0],),
            )
            session_id = cursor.fetchone()  # возвращает tuple
            self._connection.commit()
            return session_id[0]

    def authenticate(self, session_id: Optional[str]) -> str:
        if not session_id:
            raise HTTPException(400, "No session_id provided")
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT user_id FROM sessions s WHERE s.id = %s
                """,
                (session_id,),
            )
            user_id = cursor.fetchone()
            if not user_id:
                raise HTTPException(400, "Incorrect session_id provided")
        return user_id
