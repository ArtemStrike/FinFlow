from fastapi import FastAPI, HTTPException
from core.entities.account import Account
from schemas import AccountCreate, OperationRequest, AccountResponse

app = FastAPI(title="FinFlow API", description="Финансовый менеджер для управления доходами и расходами", version="1.0.0")

accounts = {}

@app.get("/", summary="Главная страница", description="Возвращает приветственное сообщение")
async def root():
    return {"message": "FinFlow Financial Manager API"}

@app.get("/health")
async def health_check():
    return {"status": "OK", "version": "1.0.0"}

@app.post("/accounts/", response_model=AccountResponse)
async def create_account(account_data: AccountCreate):
    if account_data.name in accounts:
        raise HTTPException(
            status_code=400,
            detail="Account already exists"  # сообщение для пользователя
        )
    name = account_data.name
    balance = account_data.initial_balance
    currency = account_data.currency

    # создаём аккаунт
    account = Account(name, balance, currency)
    accounts[name] = account
    
    # возвращаем через response_model
    return AccountResponse(
        name=account.name,
        balance=account.get_balance(),
        currency=account.currency,
        created_at=account.created_at
    )

@app.get("/accounts/{account_name}/balance")
async def get_balance(account_name: str):
    if account_name not in accounts:
        raise HTTPException(
            status_code=404,
            detail="Account not found"  # сообщение для пользователя
        )
    return {"balance": accounts[account_name].get_balance()}

@app.post("/accounts/{account_name}/deposit")
async def deposit(account_name: str, operation: OperationRequest):
    if account_name not in accounts:
        raise HTTPException(
            status_code=404,
            detail="Account not found"  # сообщение для пользователя
        )
    response = accounts[account_name].deposit(operation.amount, operation.description)

    if response:
        # Верни новый баланс и сообщение
        return {
            "status": "success",
            "message": "Deposit completed",
            "new_balance": accounts[account_name].get_balance(),
            "transaction": accounts[account_name].transactions[-1]  # последняя транзакция
        }
    else:
        # Верни детальную ошибку из транзакции
        last_transaction = accounts[account_name].transactions[-1]
        raise HTTPException(
            status_code=400,
            detail=last_transaction.get("error", "Deposit failed")
        )
    
@app.post("/accounts/{account_name}/withdraw")
async def withdraw(account_name: str, operation: OperationRequest):
    if account_name not in accounts:
        raise HTTPException(
            status_code=404,
            detail="Account not found"  # сообщение для пользователя
        )
    response = accounts[account_name].withdraw(operation.amount, operation.description)

    if response:
        # Верни новый баланс и сообщение
        return {
            "status": "success",
            "message": "Withdraw completed",
            "new_balance": accounts[account_name].get_balance(),
            "transaction": accounts[account_name].transactions[-1]  # последняя транзакция
        }
    else:
        # Верни детальную ошибку из транзакции
        last_transaction = accounts[account_name].transactions[-1]
        raise HTTPException(
            status_code=400,
            detail=last_transaction.get("error", "Deposit failed")
        )
@app.get("/accounts/{account_name}/transactions")
async def get_transaction_history(account_name: str):
    if account_name not in accounts:
        raise HTTPException(
            status_code=404,
            detail="Account not found"  # сообщение для пользователя
        )
    return accounts[account_name].get_transaction_history()
