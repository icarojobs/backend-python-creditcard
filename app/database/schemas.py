import re
from pydantic import BaseModel
from pydantic import field_validator
from pydantic import ValidationError


class User(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, value):
        if '@' in value:
            raise ValidationError("The username format is invalid. Dont use email to register.")
        return value
