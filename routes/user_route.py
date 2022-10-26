from re import A
from fastapi import APIRouter, Depends
from middlewares.verify_token_route import VerifyTokenRoute
from config.db import conn
from schemas.user_schemas import userEntity, usersEntity
from functions.jwt import auth_bearer

user_routes = APIRouter(route_class=VerifyTokenRoute)
# user_routes = APIRouter()


@user_routes.post("/users")
def create_user(user: str):
    print(user)
    return 'correcto'


@user_routes.get("/users")
async def find_all_users(v=Depends(auth_bearer)):
    return usersEntity(conn.users.clients.find())


@user_routes.get("/users/{id: str}")
def find_user(v=Depends(auth_bearer)):
    return userEntity(conn.users.clients.find_one({"_id": id}))


@user_routes.put("/users/{id: str}")
def update_user(v=Depends(auth_bearer)):
    print('user')
    return 'correcto'


@user_routes.delete("/users/{id: str}")
def delete_user(v=Depends(auth_bearer)):
    return 'correcto'
