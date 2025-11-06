from fastapi import FastAPI
import uvicorn
from api.routes import accounts, auth

app = FastAPI(
    title="FinFlow API", 
    description="Финансовый менеджер для управления доходами и расходами", 
    version="1.0.0"
)

app.include_router(accounts.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "FinFlow Financial Manager API"}

@app.get("/health")
async def health_check():
    return {"status": "OK", "version": "1.0.0"} 

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)