from typing import Optional


class ProductServiceImpl:
    def __init__(self, connection) -> None:
        self._connection = connection

    def add(
        self,
        place_id: Optional[int],
        name: str,
        qr_txt: str,
        about: Optional[str],
        user_id: int,
    ):
        ...
