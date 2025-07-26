import asyncio

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import uvicorn

from app.routes.users import users_route
# from app.routes.users import products_route
from app.db.users.models import create_db

app = FastAPI()
app.include_router(users_route)
# app.include_router(products_route)
# app.add_middleware(HTTPSRedirectMiddleware)


if __name__ == "__main__":
    # asyncio.run(create_db())
    uvicorn.run("main:app", reload=True)