import sys

sys.path.append('..')


from app.database.connection import Session
from app.use_cases.auth_user import UserUseCases
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/v1/login')

print('------------------------------------------------')
print('oauth_scheme: ')
print(oauth_scheme)
print('------------------------------------------------')


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
    print("----------------------------------------------------------------------")
    print(f"Access token: {token}")
    print("----------------------------------------------------------------------")

    use_case = UserUseCases(db_session=db_session)
    use_case.verify_token(access_token=token)
