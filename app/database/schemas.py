from app.helpers.custom_helpers import dd
import sys

sys.path.append('../../')

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import ValidationError
from fastapi.exceptions import HTTPException
from fastapi import status


class User(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, value):
        if '@' in value:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The username format is invalid. Dont use email to register.",
            )

        return value


class CreditCard(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: int

    @field_validator("holder")
    @classmethod
    def validate_holder(cls, value):
        if value is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The holder is required.",
            )

        if len(value) < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The holder field needs to be equals or greater 2 characters.",
            )

        return value

    @field_validator('number')
    @classmethod
    def validate_number(cls, value):
        # business logic here...
        if value is None:
            raise ValidationError("The number is required.")
        return value

    @field_validator('cvv')
    @classmethod
    def validate_cvv(cls, value):
        return value
        # business logic here...
        # if value is None:
        #     return value

        # if len(value) >= 3:
        #     return value
        # else:
        #     raise ValidationError("The cvv field needs 3 or 4 digits.")
