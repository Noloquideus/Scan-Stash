import asyncio

from fastapi import FastAPI
from uvicorn import Server, Config
from psycopg2 import connect

from scanstash.routes.auth import auth_router
from scanstash.routes.items import items_router
from scanstash.services.auth import AuthServiceImpl
from scanstash.interfaces.auth_service import AuthService

async def main() -> None:
    app = FastAPI()

    auth_service = AuthServiceImpl(
        connect(dbname="scanstashdb", host="0.0.0.0", password="1234", user="postgres")
    )
    app.dependency_overrides[AuthService] = lambda: auth_service
    
    app.include_router(auth_router)
    app.include_router(items_router)

    config = Config(app, host="0.0.0.0")
    server = Server(config)

    await server.serve()


asyncio.run(main())
