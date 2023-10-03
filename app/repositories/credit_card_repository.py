import sys

sys.path.append('../../')

from app.models.credit_card_model import CreditCardModel
from app.database.schemas import CreditCard
from app.database.connection import Session
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException
from fastapi import status


class CreditCardRepository:
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
            self.db_session = Session()
            self.db_session.add(credit_card_model)
            self.db_session.commit()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error when trying store new credit card: {e.detail}",
            ) from e

    def get_credit_cards(self):
        query = self.db_session.query(CreditCardModel).all()

        return [
            {
                "id": row.id,
                "holder": row.holder,
                "number": row.number,
                "exp_date": row.exp_date.strftime('%m/%Y'),
                "cvv": row.cvv,
            }
            for row in query
        ]
