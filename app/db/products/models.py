from uuid import uuid4

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column,declarative_base
from sqlalchemy.ext.asyncio import  create_async_engine, async_sessionmaker
from passlib.context import CryptContext

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    def __init__(self, **kwargs):
        self.id = uuid4().hex
        super().__init__(**kwargs)
