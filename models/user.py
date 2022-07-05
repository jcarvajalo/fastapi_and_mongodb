from lib2to3.pgen2.token import OP
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str