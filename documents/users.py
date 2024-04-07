from uuid import uuid4

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id")
    user: str = Field()
    password: str = Field()
    email: str = Field()
    name: str = Field()
