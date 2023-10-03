from datetime import datetime
from datetime import timedelta
import pytz

UTC = pytz.utc

import sys

sys.path.append('../../')

from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.credit_card_model import CreditCardModel
from app.database.schemas import CreditCard
from passlib.context import CryptContext

crypt_context = CryptContext(schemes=['sha256_crypt'])


class CreditCardUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_credit_card(self, credit_card: CreditCard):
        credit_card_model = CreditCardModel(
            exp_date=credit_card.exp_date,
            holder=credit_card.holder,
            number=credit_card.number,
            cvv=credit_card.cvv
        )

        try:
            self.db_session.add(credit_card_model)
            self.db_session.commit()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error when trying to store new credit_card.",
            ) from e

    def get_credit_cards(self):
        credit_card = CreditCard
        result = self.db_session.query(credit_card).all()
        # result = self.db_session.execute("select * from credit_cards")

        print('-----------------------------------------------------')
        print('result query:')
        print(result)
        print('-----------------------------------------------------')

        return [{"msg": "ok"}]

        # if result is None:
        #     raise HTTPException(
        #         status_code=status.HTTP_200_OK,
        #         detail="No credit card found"
        #     )
        #
        # return result
