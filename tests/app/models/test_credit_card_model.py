import sys

sys.path.append('../../../')

from datetime import date
from app.models.credit_card_model import CreditCardModel
import unittest
from app.helpers.custom_helpers import encrypt_credit_card


class TestCreditCardModel(unittest.TestCase):
    def test_credit_card_model_attributes(self):
        encrypted_credit_card = encrypt_credit_card("4539578763621486")

        credit_card_model = CreditCardModel(
            exp_date=date.today(),
            holder="testholder",
            number=encrypted_credit_card['encryption_card_number'],
            cvv=123,
            brand='visa',
            encryption_key=encrypted_credit_card['encryption_key']
        )

        self.assertTrue(type(credit_card_model.exp_date) is date)
        self.assertTrue(type(credit_card_model.holder) is str)
        self.assertTrue(type(credit_card_model.number) is bytes)
        self.assertTrue(type(credit_card_model.cvv) is int)
        self.assertTrue(type(credit_card_model.brand) is str)
        self.assertTrue(type(credit_card_model.encryption_key) is bytes)
        self.assertTrue(str(credit_card_model.cvv).isnumeric())
        self.assertTrue(len(credit_card_model.holder) == 10)
