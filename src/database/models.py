from typing import List, Optional
from dataclasses import dataclass

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import db
from src.database.asociative import user_product_assoc


@dataclass
class Review(db.Model):
    __tablename__ = "reviews"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    text: Mapped[str] = mapped_column(String())
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=True, server_default=None)
    user: Mapped["User"] = relationship()


@dataclass
class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    price: Mapped[float] = mapped_column()
    img_url: Mapped[str] = mapped_column(String())
    reviews: Mapped[List[Review]] = relationship()


@dataclass
class User(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    reviews: Mapped[List[Review]] = relationship()
    products: Mapped[List[Product]] = relationship(secondary=user_product_assoc)
    