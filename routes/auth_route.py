from fastapi import APIRouter, Header, Depends
from fastapi.params import Body
from pydantic import BaseModel
from functions.jwt import generate_token, validate_token
from fastapi import status
from fastapi.responses import JSONResponse

from repositories.users import UsersRepository

auth_routes = APIRouter()


class Token(BaseModel):
    token: str


class Message(BaseModel):
    message: str


@auth_routes.post(
    '/login',
    status_code=status.HTTP_200_OK,
    response_model=Token,
)
async def login(
        email: str = Body(...),
        password: str = Body(...),
        user_repository: UsersRepository = Depends(UsersRepository)
):
    user = user_repository.find_by_email_password(email, password)
    token = generate_token({"email": email, "user": user.user})
    return JSONResponse(
        content={
            "token": token
        }
    )


@auth_routes.post(
    "/verify_token",
    status_code=status.HTTP_200_OK,
    # response_model=Message,
)
async def verify_token(
        token: str,
):
    return validate_token(token)
