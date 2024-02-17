from typing import Optional


class PlaceService:
    def add(
        self,
        *,
        user_id: int,
        name: str,
        qr_txt: str,
        about: Optional[str],
    ) -> None:
        raise NotImplementedError

    def delete(
        self,
        *,
        user_id: int,
        name: str,
    ) -> None:
        raise NotImplementedError

    def get_info(
        self,
        *,
        user_id: int,
        name: str,
    ) -> None:
        raise NotImplementedError
