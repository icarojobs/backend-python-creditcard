import calendar
from datetime import datetime
from datetime import date
import pytz

UTC = pytz.utc

import random
import string
from cryptography.fernet import Fernet
from fastapi.exceptions import HTTPException
from fastapi import status
from typing import Union


def dd(value):
    print('-----------------------------------------------------------------')
    print(value)
    print(type(value))
    print('-----------------------------------------------------------------')


def random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def get_last_day(month: int = 0, year: int = 0) -> str:
    if month != 0 and year != 0:
        datetime_utc = datetime(year, month, 1)
        res = calendar.monthrange(datetime_utc.year, datetime_utc.month)
        return str(res[1])

    datetime_utc = datetime.now(UTC)
    res = calendar.monthrange(datetime_utc.year, datetime_utc.month)
    return str(res[1])


def fix_card_date(value: str) -> date:
    split_date = value.split('/')
    last_day_of_referenced_date = get_last_day(int(split_date[0]), int(split_date[1]))

    return date(int(split_date[1]), int(split_date[0]), int(last_day_of_referenced_date))


def check_if_creditcard_date_is_valid(date_to_compare: date) -> bool:
    to_date = datetime.strptime(date_to_compare.strftime('%Y-%m-%d'), '%Y-%m-%d')
    datetime_utc = datetime.now(UTC)
    from_date = datetime.strptime(datetime_utc.strftime('%Y-%m-%d'), "%Y-%m-%d")

    return to_date > from_date


def prepare_credit_card_date(value: str) -> Union[date, bool]:
    if value is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The exp_date is required.",
        )

    try:
        card_date = fix_card_date(value)

        return card_date if check_if_creditcard_date_is_valid(card_date) else False
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The exp_date format is invalid. The correct is dd/YYYY",
        ) from e


def encrypt_credit_card(card_number: str) -> dict:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encryption_card_number = fernet.encrypt(card_number.encode())

    return {
        "encryption_key": key,
        "encryption_card_number": encryption_card_number
    }


def decrypt_credit_card(encryption_key, encryption_card_number) -> str:
    key = encryption_key
    fernet = Fernet(key)
    card = encryption_card_number
    return fernet.decrypt(card).decode()
