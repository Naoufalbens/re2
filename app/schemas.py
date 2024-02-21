from pydantic import BaseModel
from datetime import datetime

class QuoteBase(BaseModel):
    description: str

class QuoteCreate(QuoteBase):
    price: float

class Quote(QuoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
