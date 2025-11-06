from pydantic import BaseModel
#field - фильтр для валидации значений типо больше меньше
#EmailStr - фильтр для валидации поля почты
#ConfigDict - фильтр для валидации словаря пример запретить дополнительные значение которые отсутствуют в схеме

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

class UserLogin(BaseModel):
    username: str
    password: str