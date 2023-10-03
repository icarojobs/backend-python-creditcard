import calendar
from datetime import datetime
import pytz

UTC = pytz.utc

import random
import string


def random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def get_last_day() -> str:
    datetime_utc = datetime.now(UTC)

    res = calendar.monthrange(datetime_utc.year, datetime_utc.month)
    return str(res[1])


def fix_card_date(value: str) -> datetime:
    date_string = f"{str}/{get_last_day()}"
    date_object = datetime.strptime(date_string, "%m/%Y/%d")
    formatted_date = date_object.strftime('%Y-%m-%d')
    return datetime.strptime(formatted_date, "%Y-%m-%d")


def is_valid_creditcard_date(date_to_compare: datetime) -> bool:
    datetime_utc = datetime.now(UTC)

    return date_to_compare > datetime_utc
