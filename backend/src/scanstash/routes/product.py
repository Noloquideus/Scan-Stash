from fastapi import APIRouter


product_router = APIRouter(prefix="/product")


# class ProductSchema(BaseModel):
#     name: str
#     qr_txt: str
#     about: Optional[str]


# @product_router.post("/add")
# async def add(
#     data: ProductSchema,
#     auth_service: AuthService = Depends(),
#     product_service: ProductService = Depends(),
#     session_id: Optional[str] = Cookie(None),
# ):
#     user_id = auth_service.authenticate(session_id)
#     product_service.add()
#     return True
