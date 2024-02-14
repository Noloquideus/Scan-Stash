from typing import Optional


class ProductService:
    def add(
        self,
        *,
        place_name: Optional[str],
        name: str,
        qr_txt: str,
        about: Optional[str],
        user_id: int,
    ) -> None:
        raise NotImplementedError
