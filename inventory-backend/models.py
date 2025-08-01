# models.py
from pydantic import BaseModel, Field
from typing import Optional, Annotated, List

Name = Annotated[str, Field(min_length=1, max_length=50, strip_whitespace=True)]
Category = Annotated[Optional[str], Field(min_length=1, max_length=50, strip_whitespace=True)]
Quantity = Annotated[int, Field(ge=0, le=100000, description="Must be ≥ 0")]

class Item(BaseModel):
    name: Name
    category: Category = "General"
    quantity: Quantity

class Message(BaseModel):
    message: str
