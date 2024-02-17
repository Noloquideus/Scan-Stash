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

    def delete(
        self,
        *,
        user_id: int,
        place_name: str,
        product_name: str,
    ) -> None:
        raise NotImplementedError

    def get_info(
        self,
        *,
        user_id: int,
        place_name: str,
        product_name: str,
    ) -> None:
        raise NotImplementedError
