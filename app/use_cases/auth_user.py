from datetime import datetime
from datetime import timedelta
import pytz

UTC = pytz.utc

import sys

sys.path.append('../../')

from decouple import config
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from jose import jwt
from jose import JWTError
from app.models.user_model import UserModel
from app.models.credit_card_model import CreditCardModel
from app.database.schemas import User
from app.database.schemas import CreditCard
from passlib.context import CryptContext

crypt_context = CryptContext(schemes=['sha256_crypt'])


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def user_register(self, user: User):
        user_model = UserModel(
            username=user.username,
            password=crypt_context.hash(user.password)
        )

        try:
            self.db_session.add(user_model)
            self.db_session.commit()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists",
            ) from e

    def user_login(self, user: User, expires_in: int = 30):
        found_user = self.db_session.query(UserModel).filter_by(username=user.username).first()

        if found_user is None or not crypt_context.verify(user.password, found_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The credentials provided were not authorized."
            )

        expiration_time = datetime.now(UTC) + timedelta(minutes=expires_in)

        payload = {
            "sub": found_user.username,
            "exp": expiration_time
        }

        access_token = jwt.encode(payload, config('SECRET_KEY'), algorithm=config('ALGORITHM'))

        return {
            "access_token": access_token,
            "expiration": expiration_time.isoformat()
        }

    def verify_token(self, access_token):
        if access_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The access_token is required.",
            )

        try:
            data = jwt.decode(access_token, config('SECRET_KEY'), algorithms=[config('ALGORITHM')])
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The credentials provided were not authorized.",
            ) from e

        found_user = self.db_session.query(UserModel).filter_by(username=data['sub']).first()

        if found_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The credentials provided were not authorized."
            )