import asyncio

from fastapi import FastAPI
from uvicorn import Server, Config
from psycopg2 import connect

from scanstash.routes.auth import auth_router
from scanstash.routes.test import test_router
from scanstash.routes.place import place_router
from scanstash.routes.product import product_router
from scanstash.services.auth import AuthServiceImpl
from scanstash.services.place import PlaceServiceImpl
from scanstash.services.product import ProductServiceImpl
from scanstash.interfaces.auth_service import AuthService
from scanstash.interfaces.place_service import PlaceService
from scanstash.interfaces.produtc_service import ProductService


async def main() -> None:
    app = FastAPI(title="Scan&Stash")

    auth_service = AuthServiceImpl(
        connect(
            dbname="scanstashdb",
            host="0.0.0.0",
            password="1234",
            user="postgres",
        ),
    )
    place_service = PlaceServiceImpl(
        connect(
            dbname="scanstashdb",
            host="0.0.0.0",
            password="1234",
            user="postgres",
        ),
    )
    product_service = ProductServiceImpl(
        connect(
            dbname="scanstashdb",
            host="0.0.0.0",
            password="1234",
            user="postgres",
        ),
    )

    app.dependency_overrides[AuthService] = lambda: auth_service
    app.dependency_overrides[PlaceService] = lambda: place_service
    app.dependency_overrides[ProductService] = lambda: product_service

    app.include_router(auth_router)
    app.include_router(test_router)
    app.include_router(place_router)
    app.include_router(product_router)

    config = Config(app, host="0.0.0.0")
    server = Server(config)

    await server.serve()


asyncio.run(main())
