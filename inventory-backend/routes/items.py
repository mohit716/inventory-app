from fastapi import APIRouter, Security, Depends, Query
from typing import List, Optional
from models import Item, Message
from security import api_key_auth
from services.items_service import ItemService, get_item_service

router = APIRouter(prefix="/items", tags=["items"])

@router.get("", response_model=List[Item])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=1000),
    q: Optional[str] = None,
    svc: ItemService = Depends(get_item_service)
):
    items = svc.list_items(skip, limit)
    if q:
        ql = q.lower()
        items = [i for i in items if ql in i["name"].lower() or ql in (i.get("category","").lower())]
    return items

@router.post("", response_model=Message)
def create_item(item: Item, api_key: str = Security(api_key_auth), svc: ItemService = Depends(get_item_service)):
    svc.create_item(item)
    return {"message": "Item added!"}
