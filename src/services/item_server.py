from sqlalchemy.orm import Session
from ..models.items_model import Item
from ..schemas.items_schema import ItemCreate
from ..models.user_model import User


def create_item(db: Session, item: ItemCreate):
    db_item = db.query(Item)
    