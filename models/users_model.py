from typing import Optional
from pydantic import BaseModel


class User (BaseModel):
    id: Optional[str]
    user: str
    password: str
    email: str
    name: str
