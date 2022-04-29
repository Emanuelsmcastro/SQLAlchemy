from pydantic import BaseModel
from typing import Optional


class SchemaProduct(BaseModel):
    id: Optional[int]
    uid: Optional[str]
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
