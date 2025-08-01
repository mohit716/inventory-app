from typing import List
from models import Item
from db import get_items_collection

class ItemService:
    def __init__(self):
        self.col = get_items_collection()

    def list_items(self, skip: int = 0, limit: int = 50) -> List[Item]:
        return list(self.col.find({}, {"_id": 0}).skip(skip).limit(limit))

    def create_item(self, item: Item) -> None:
        self.col.insert_one(item.model_dump())
