import sys

sys.path.append('../../../')

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.depends import token_verifier
from app.use_cases.auth_user import UserUseCases
from app.use_cases.credit_card import CreditCardUseCases
from app.database.schemas import User
from app.database.schemas import CreditCard

user_router = APIRouter(prefix='/v1')
credit_card_router = APIRouter(prefix='/v1', dependencies=[Depends(token_verifier)])


@user_router.post('/users')
def user_register(user: User, db_session: Session = Depends(get_db_session)):
    use_case = UserUseCases(db_session=db_session)
    use_case.user_register(user=user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": True, "message": "User registered successfully!"}
    )


@user_router.post('/login')
def user_login(
        request_form_user: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db_session)
):
    use_case = UserUseCases(db_session=db_session)

    user = User(
        username=request_form_user.username,
        password=request_form_user.password
    )

    auth_data = use_case.user_login(user=user)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": True, "data": auth_data}
    )


@credit_card_router.post('/credit-cards')
def create_credit_card(credit_card: CreditCard, db_session: Session = Depends(get_db_session)):
    use_case = CreditCardUseCases(db_session=db_session)
    use_case.create_credit_card(credit_card=credit_card)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": True, "message": "CreditCard added successfully!"}
    )


@credit_card_router.get('/credit-cards')
def get_credit_cards(db_session: Session = Depends(get_db_session)):
    use_case = CreditCardUseCases(db_session=db_session)
    result = use_case.get_credit_cards()
    print('-----------------------------------------------------------')
    print('credit_cards:')
    print(result)
    print('-----------------------------------------------------------')
    #
    # return JSONResponse(
    #     status_code=status.HTTP_200_OK,
    #     content={"status": True, "data": result}
    # )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": True, "data": [{"id": 1, "card_id": "xpto"}]}
    )

