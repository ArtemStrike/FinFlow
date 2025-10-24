from pydantic import BaseModel
from typing import Optional

class AccountCreate(BaseModel):
    name: str
    initial_balance: float = 0
    currency: str = "RUB"

class TransactionRequest(BaseModel):
    amount: float
    description: Optional[str] = ""