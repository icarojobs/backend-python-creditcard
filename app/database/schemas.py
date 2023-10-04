from app.helpers.custom_helpers import dd
import sys

sys.path.append('../../')

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import ValidationError
from pydantic import Field
from typing import Any
from fastapi.exceptions import HTTPException
from fastapi import status
from creditcard import CreditCard as CardValidator


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
    brand: Any = Field(default="unknown", repr=False)

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
        cc = CardValidator(value)

        if value is None or len(value) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The card number is required.",
            )

        if not cc.is_valid():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The card number is invalid.",
            )

        return value

    @field_validator('cvv')
    @classmethod
    def validate_cvv(cls, value):
        return value

    # @field_validator('brand')
    # @classmethod
    # def validate_brand(cls, value):
    #     cc = CardValidator(value)
    #     if cc.get_brand() is None or len(cc.get_brand()) == 0:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="The card brand is invalid.",
    #         )
    #
    #     return cc.get_brand()
