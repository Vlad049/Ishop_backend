from typing import List, Optional

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import db


class Review(db.Model):
    __tablename__ = "reviews"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    text: Mapped[str] = mapped_column(String())
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))


class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    price: Mapped[float] = mapped_column()
    img_url: Mapped[str] = mapped_column(String())
    reviews: Mapped[List[Review]] = relationship()
    