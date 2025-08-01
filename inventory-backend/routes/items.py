# routes/items.py
from fastapi import APIRouter, Security, Depends
from typing import List
from models import Item, Message
from security import api_key_auth
from services.items_service import ItemService, get_item_service

router = APIRouter(prefix="/items", tags=["items"])

@router.get("", response_model=List[Item])
def list_items(svc: ItemService = Depends(get_item_service)):
    return svc.list_items()

@router.post("", response_model=Message)
def create_item(item: Item, api_key: str = Security(api_key_auth),
                svc: ItemService = Depends(get_item_service)):
    svc.create_item(item)
    return {"message": "Item added!"}
