# services/items_service.py
from typing import List
from models import Item
from db import get_items_collection

class ItemService:
    def __init__(self):
        self.col = get_items_collection()

    def list_items(self) -> List[Item]:
        return list(self.col.find({}, {"_id": 0}))  # keep _id out

    def create_item(self, item: Item) -> None:
        self.col.insert_one(item.model_dump())

# DI provider
def get_item_service() -> ItemService:
    return ItemService()
