# coding=utf-8
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from ultros_site.database.common import DeclarativeBase

__author__ = "Gareth Coles"


class EmailCode(DeclarativeBase):
    __tablename__ = "email_code"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    user = relationship("User", back_populates="parent")

    code = Column(String)

    def __repr__(self):
        return "<Session(id={}, user={}, expires={})>".format(
            self.id, self.user.username, self.expires
        )
