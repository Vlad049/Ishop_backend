from sqlalchemy import Table, Column, ForeignKey

from src.database.base import Base


user_product_assoc = Table(
    "user_product_assoc",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)