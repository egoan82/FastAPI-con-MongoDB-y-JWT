from fastapi import APIRouter, Depends, status

from repositories.users import UsersRepository
from functions.jwt import auth_bearer
from schemas.user_schemas import UserRead, UserCreate, UserUpdate

user_routes = APIRouter()


@user_routes.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=list[UserRead],
    dependencies=[Depends(auth_bearer)]
)
async def find_all_users(
        user_repository: UsersRepository = Depends(UsersRepository)
):
    return user_repository.list()


@user_routes.get(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserRead,
    dependencies=[Depends(auth_bearer)]
)
async def get_user_by_id(
        user_id: str,
        user_repository: UsersRepository = Depends(UsersRepository)
):
    return user_repository.find_by_id(user_id=user_id)


@user_routes.post(
    "/users",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth_bearer)]
)
def create_user(
        data: UserCreate,
        user_repository: UsersRepository = Depends(UsersRepository)
):
    return user_repository.create_user(data)


@user_routes.put(
    "/users/{user_id}",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth_bearer)]
)
def create_user(
        user_id: str,
        data: UserUpdate,
        user_repository: UsersRepository = Depends(UsersRepository)
):
    return user_repository.update_user(user_id=user_id, user=data)


@user_routes.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth_bearer)]
)
def delete_user(
        user_id: str,
        user_repository: UsersRepository = Depends(UsersRepository)
):
    return user_repository.delete_user(user_id=user_id)
