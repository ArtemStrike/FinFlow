from fastapi import FastAPI

app = FastAPI(title="FinFlow API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "FinFlow Financial Manager API"}