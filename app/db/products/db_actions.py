from typing import Annotated, Optional

from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select

from app.db.products.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.users.models import get_db

async def get_product(product_id: str, db: AsyncSession):
    query = select(Product).filter_by(id=product_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()
