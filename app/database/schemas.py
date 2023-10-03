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


class CreditCard(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: int

    @field_validator('exp_date')
    @classmethod
    def validate_exp_date(cls, value):
        # business logic here...
        if value is None:
            raise ValidationError("The exp_date is required.")

        # todo: get 30 (last day of month) dynamically
        return f"{value}/30"

    @field_validator('holder')
    @classmethod
    def validate_holder(cls, value):
        # business logic here...
        if value is None:
            raise ValidationError("The holder is required.")
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
        # business logic here...
        if value is None:
            return value

        if len(value) in {3, 4}:
            return value
        else:
            raise ValidationError("The cvv field needs 3 or 4 digits.")
