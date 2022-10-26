from fastapi import APIRouter, Header
from pydantic import BaseModel
from functions.jwt import generate_token, validate_token
from fastapi import status
from fastapi.responses import JSONResponse

auth_routes = APIRouter()


class User (BaseModel):
    user: str
    password: str


@auth_routes.post('/login')
def login(user: User):
    print(user.password)
    if user.user == "edward":
        return generate_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=status.HTTP_404_NOT_FOUND)


@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
