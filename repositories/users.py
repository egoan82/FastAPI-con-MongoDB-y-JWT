from fastapi import HTTPException, status
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder

from config.db import conn
from documents.users import User
from schemas.user_schemas import UserRead, UserCreate, UserUpdate


class UsersRepository:
    def __init__(self):
        self.db = conn["users"]

    def find_by_email_password(self, email: str, password: str):
        user = self.db["users"].find_one({"email": email, "password": password})
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        user["id"] = str(user["_id"])
        return UserRead(**user)

    def list(self):
        list_users: list[UserRead] = []
        for user in self.db["users"].find({}):
            user["id"] = str(user["_id"])
            list_users.append(UserRead(**user))

        return list_users

    def find_by_id(self, user_id):
        user = self.db["users"].find_one(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        user["id"] = str(user["_id"])
        return UserRead(**user)

    def create_user(self, user: UserCreate):
        user = User(**user.dict())
        user_data = jsonable_encoder(user)
        self.db["users"].insert_one(user_data)
        return self.find_by_id(user_data["_id"])

    def update_user(self, user_id: str, user: UserUpdate):
        user_data = jsonable_encoder(user)
        self.db["users"].update_one({"_id": user_id}, {"$set": user_data})
        return self.find_by_id(user_id)

    def delete_user(self, user_id: str):
        self.db["users"].delete_one({"_id": user_id})
        return {"message": "User deleted successfully"}