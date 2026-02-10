from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from helpers.database import db


class Endereco(db.Model):

    __tablename__ = "tb_endereco"
    id: Mapped[int] = mapped_column(primary_key=True)
    logradouro: Mapped[str] = mapped_column(String(), nullable=True)
    cep: Mapped[str] = mapped_column(String(8))
    numero: Mapped[int] = mapped_column(nullable=True)

    usuario_id: Mapped[int] = mapped_column(ForeignKey("tb_usuario.id"))

    usuario: Mapped["Usuario"] = relationship(back_populates="enderencos")
