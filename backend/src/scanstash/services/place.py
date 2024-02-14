from typing import Optional

from fastapi import HTTPException


class PlaceServiceImpl:
    def __init__(self, connection) -> None:
        self._connection = connection

    def add(
        self,
        *,
        user_id: int,
        name: str,
        qr_txt: str,
        about: Optional[str],
    ) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1 FROM places p WHERE p.name = %s and p.user_id = %s
                """,
                (name, user_id),
            )
            name_is_taken = cursor.fetchone()
            if name_is_taken:
                raise HTTPException(400, "Place name is taken")

            cursor.execute(
                """
                INSERT INTO places
                (name, qr_txt, about, user_id) VALUES (%s, %s, %s, %s)
                """,
                (name, qr_txt, about, user_id),
            )
            self._connection.commit()

    def delete(
        self,
        *,
        user_id: int,
        name: str,
    ) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1 FROM places
                WHERE name = %s and user_id = %s
                """,
                (name, user_id),
            )
            correct_name = cursor.fetchone()
            if not correct_name:
                raise HTTPException(400, "There is no place with this name")

            cursor.execute(
                """
                DELETE FROM places
                WHERE name = %s and user_id = %s
                """,
                (name, user_id),
            )
            self._connection.commit()
