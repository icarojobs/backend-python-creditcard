import re
from pydantic import BaseModel
from pydantic import field_validator


class User(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z][0-9]|@)+$', value):
            raise ValueError("The username format is invalid.")
        return value
