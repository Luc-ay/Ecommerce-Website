from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import enum
from sqlalchemy import Enum

class RoleEnum(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    VENDOR = "vendor"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")

    def __repr__(self):
      return f"<User(username={self.username}, email={self.email}, role={self.role})>"