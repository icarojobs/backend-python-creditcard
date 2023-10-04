import sys

sys.path.append('../../')

from sqlalchemy import Column, Integer, String, Date
from app.database.base import Base


class CreditCardModel(Base):
    __tablename__ = 'credit_cards'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    exp_date = Column('exp_date', Date, nullable=False)
    holder = Column('holder', String, nullable=False)
    number = Column('number', String, nullable=False)
    cvv = Column('cvv', Integer, nullable=True)
    brand = Column('brand', String, nullable=False)
