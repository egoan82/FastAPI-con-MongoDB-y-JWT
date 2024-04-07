from pydantic import BaseModel


class CommonUser(BaseModel):
    user: str
    password: str
    email: str
    name: str


class UserRead(CommonUser):
    id: str


class UserCreate(CommonUser):
    ...


class UserUpdate(CommonUser):
    ...
