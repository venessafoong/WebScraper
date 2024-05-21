from pydantic import BaseModel
from typing import Optional

class Property(BaseModel):
    id: Optional[int] = None
    address: str
    price: int

    class Config:
        arbitrary_types_allowed = True
