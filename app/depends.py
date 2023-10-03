import sys

sys.path.append('..')


from app.database.connection import Session
from app.repositories.user_repository import UserRepository
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/v1/login')


def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


def token_verifier(
        db_session=Depends(get_db_session),
        token=Depends(oauth_scheme)
):
    repository = UserRepository(db_session=db_session)
    repository.verify_token(access_token=token)
