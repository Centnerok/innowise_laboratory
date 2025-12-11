from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from typing import Optional

class Base(DeclarativeBase):
	pass

class Book(Base):
	__tablename__ = "book"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(String(30))
	author: Mapped[str] = mapped_column(String(30))
	year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)