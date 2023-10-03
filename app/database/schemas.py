import sys

sys.path.append('../../')

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import ValidationError
from app.helpers.custom_helpers import get_last_day
from app.helpers.custom_helpers import fix_card_date
from app.helpers.custom_helpers import is_valid_creditcard_date



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
        if value is None:
            raise ValidationError("The exp_date is required.")

        if len(value) != 7:
            raise ValidationError("The exp_date format is invalid. The correct is dd/YYYY")

        card_date = fix_card_date(value)

        if not is_valid_creditcard_date(card_date):
            raise ValidationError("The exp_date provided is expired.")

        return card_date.strftime('%Y-%m-%d')

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
        return value
        # business logic here...
        # if value is None:
        #     return value

        # if len(value) >= 3:
        #     return value
        # else:
        #     raise ValidationError("The cvv field needs 3 or 4 digits.")
