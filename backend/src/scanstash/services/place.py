from typing import Optional

from fastapi import HTTPException


def place_name_is_taken(cursor, place_name, user_id) -> bool:
    cursor.execute(
        """
        SELECT 1 FROM places
        WHERE name = %s and user_id = %s
        """,
        (place_name, user_id),
    )
    return cursor.fetchone() is not None


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
            name_is_taken = place_name_is_taken()
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
            correct_name = place_name_is_taken(cursor, name, user_id)
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

    def get_info(
        self,
        *,
        user_id: int,
        name: str,
    ) -> None:
        with self._connection.cursor() as cursor:
            correct_name = place_name_is_taken(cursor, name, user_id)
            if not correct_name:
                raise HTTPException(400, "There is no place with this name")

            cursor.execute(
                """
                SELECT (name, qr_txt, about) FROM places
                WHERE name = %s and user_id = %s
                """,
                (name, user_id),
            )
            data = cursor.fetchall()[0][0].split(",")
            return {
                "place_name": data[0][1:],
                "qr_txt": data[1],
                "about": data[2][1:-2],
            }
