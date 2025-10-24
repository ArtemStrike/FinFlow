from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    name: str
    initial_balance: float = 0
    currency: str = "RUB"

class OperationRequest(BaseModel):
    amount: float
    description: Optional[str] = ""

class AccountResponse(BaseModel):
    name: str
    balance: float
    currency: str
    created_at: datetime