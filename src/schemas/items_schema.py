from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class ItemTypeEnum(Enum):
    ELECTRONICS = "electronics"
    FURNITURE = "furniture"
    CLOTHING = "clothing"
    FOOD = "food"
    BOOKS = "books"


class ItemBase(BaseModel):
    name: str = Field(default="Smartphone")
    description: str = Field(default="A high-end smartphone with 128GB storage")
    price: float = Field(gt=0, default=999.99)
    quantity: int = Field(ge=0, default=50)
    item_type: ItemTypeEnum = Field(default=ItemTypeEnum.FOOD)

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    pass

    class Config:
        from_attributes = True