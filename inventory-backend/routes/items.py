# routes/items.py
from fastapi import APIRouter, Security
from typing import List
from models import Item, Message
from db import get_items_collection
from security import api_key_auth

router = APIRouter(prefix="/items", tags=["items"])

@router.get("", response_model=List[Item])
def list_items():
    col = get_items_collection()
    return list(col.find({}, {"_id": 0}))

@router.post("", response_model=Message)
def create_item(item: Item, api_key: str = Security(api_key_auth)):
    col = get_items_collection()
    col.insert_one(item.model_dump())  # pydantic v2
    return {"message": "Item added!"}
