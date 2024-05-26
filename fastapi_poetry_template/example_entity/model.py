from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_poetry_template.database import Base


class Example(Base):
    """Db schema."""

    __tablename__ = "examples"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status: Mapped[str] = Column(String(10), nullable=False)
