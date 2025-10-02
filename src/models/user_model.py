from ..config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from .items_model import Item
from sqlalchemy.orm import relationship
from ..schemas.auth_schema import USERROLE as RoleEnum
from sqlalchemy import Enum



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(Text, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")

    def __repr__(self):
      return f"<User(username={self.username}, email={self.email}, role={self.role})>"