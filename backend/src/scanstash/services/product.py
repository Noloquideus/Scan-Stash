from typing import Optional

from fastapi import HTTPException


class ProductServiceImpl:
    def __init__(self, connection) -> None:
        self._connection = connection

    def add(
        self,
        *,
        place_name: Optional[str],
        name: str,
        qr_txt: str,
        about: Optional[str],
        user_id: int,
    ) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id FROM places p WHERE p.name = %s and p.user_id = %s
                """,
                (name, user_id),
            )
            place_id = cursor.fetchone()[0]
            if not place_id:
                raise HTTPException(400, "Thete is no place with this name")
            cursor.execute(
                """
                INSERT INTO products
                (name, qr_txt, about, place_id, user_id) VALUES (%s, %s, %s, %s, %s)
                """,
                (name, qr_txt, about, place_id, user_id),
            )
            self._connection.commit()
