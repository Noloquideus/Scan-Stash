from typing import Optional

from fastapi import HTTPException


def get_place_id(cursor, place_name: str, user_id: int) -> int:
    cursor.execute(
        """
            SELECT id FROM places p WHERE p.name = %s and p.user_id = %s
            """,
        (place_name, user_id),
    )
    return cursor.fetchone()[0]


def check_product_name(
    cursor,
    product_name: str,
    place_id: int,
    user_id: int,
) -> bool:
    cursor.execute(
        """
            SELECT 1 FROM products
            WHERE name = %s and place_id = %s and user_id = %s
            """,
        (product_name, place_id, user_id),
    )
    return cursor.fetchone() is not None


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
            place_id = get_place_id(cursor, place_name, user_id)
            if not place_id:
                raise HTTPException(400, "Thete is no place with this name")

            if check_product_name(cursor, name, place_id, user_id):
                raise HTTPException(
                    400,
                    "You already have product with similar name in this place",
                )

            cursor.execute(
                """
                INSERT INTO products
                (name, qr_txt, about, place_id, user_id) VALUES (%s, %s, %s, %s, %s)
                """,
                (name, qr_txt, about, place_id, user_id),
            )
            self._connection.commit()

    def delete(
        self,
        *,
        user_id: int,
        place_name: str,
        product_name: str,
    ) -> None:
        with self._connection.cursor() as cursor:
            place_id = get_place_id(cursor, place_name, user_id)
            if not place_id:
                raise HTTPException(400, "There is no place with such name")

            if not check_product_name(cursor, product_name, place_id, user_id):
                raise HTTPException(
                    400,
                    "There is no product with such name in the place",
                )

            cursor.execute(
                """
                DELETE FROM products
                WHERE name = %s and place_id = %s and user_id = %s
                """,
                (product_name, place_id, user_id),
            )
            self._connection.commit()

    def get_info(
        self,
        *,
        user_id: int,
        place_name: str,
        product_name: str,
    ) -> dict:
        with self._connection.cursor() as cursor:
            place_id = get_place_id(cursor, place_name, user_id)
            if not place_id:
                raise HTTPException(400, "There is no place with such name")

            if not check_product_name(cursor, product_name, place_id, user_id):
                raise HTTPException(
                    400,
                    "There is no product with such name in the place",
                )

            cursor.execute(
                """
                SELECT (name, qr_txt, about) FROM products
                WHERE name = %s and place_id = %s and user_id = %s
                """,
                (product_name, place_id, user_id),
            )
            data = cursor.fetchall()[0][0].split(",")
            return [
                {
                    "product_name": data[0][1:],
                    "qr_txt": data[1],
                    "about": data[2][:-1],
                },
            ]
