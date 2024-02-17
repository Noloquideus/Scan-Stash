class SearchServiceImpl:
    def __init__(self, connection) -> None:
        self._connection = connection

    def search(self, user_id: int):
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT name FROM places
                WHERE user_id = %s
                """,
                (user_id,),
            )
            places = [data[0] for data in cursor.fetchall()]
            cursor.execute(
                """
                SELECT name FROM products
                WHERE user_id = %s
                """,
                (user_id,),
            )
            products = [data[0] for data in cursor.fetchall()]
            return {"places": places, "products": products}
