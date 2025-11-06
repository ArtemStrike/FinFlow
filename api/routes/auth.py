from fastapi import APIRouter, HTTPException, Response, Depends
from schemas import UserLogin
from authx import AuthX, AuthXConfig

router = APIRouter(prefix="/auth", tags=["auth"])

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_token_for_access"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

@router.post("/login")
async def login(credentials: UserLogin, response: Response):
    # тут нужно будет доделать проверку юзернейма и пороля вместо иф
    if credentials.username == "admin" and credentials.password == "admin":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@router.get("/protected", dependencies=[Depends(security.access_token_required)])
async def protected():
    return {"data": "чупеп"}
