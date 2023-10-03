import sys

sys.path.append('../../../')

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.depends import token_verifier
from app.database.schemas import User
from app.database.schemas import CreditCard
from app.repositories.credit_card_repository import CreditCardRepository
from app.repositories.user_repository import UserRepository

user_router = APIRouter(prefix='/v1')
credit_card_router = APIRouter(prefix='/v1', dependencies=[Depends(token_verifier)])


@user_router.post('/users')
def user_register(user: User, db_session: Session = Depends(get_db_session)):
    repository = UserRepository(db_session=db_session)
    repository.create_user(user=user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": True, "message": "User created successfully!"}
    )


@user_router.post('/login')
def user_login(
        request_form_user: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db_session)
):
    repository = UserRepository(db_session=db_session)

    user = User(
        username=request_form_user.username,
        password=request_form_user.password
    )

    auth_data = repository.user_login(user=user)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": True, "data": auth_data}
    )


@credit_card_router.post('/credit-cards')
def create_credit_card(credit_card: CreditCard, db_session: Session = Depends(get_db_session)):
    try:
        repository = CreditCardRepository(db_session=db_session)
        repository.create_credit_card(credit_card=credit_card)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"status": True, "message": "CreditCard created successfully!"}
        )
    except Exception as error:
        raise HTTPException(
            400, detail="Error when trying create new credit card."
        ) from error


@credit_card_router.get('/credit-cards')
def create_credit_card(db_session: Session = Depends(get_db_session)):
    try:
        repository = CreditCardRepository(db_session=db_session)
        response = repository.get_credit_cards()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": True, "data": response}
        )
    except Exception as error:
        raise HTTPException(
            400,
            detail="Error when trying to get all credit cards"
        ) from error


@credit_card_router.get('/credit-cards/{card_id}')
def get_credit_card(card_id: int, db_session: Session = Depends(get_db_session)):
    try:
        repository = CreditCardRepository(db_session=db_session)
        response = repository.get_credit_card(card_id=card_id)

        if response is None:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"status": False, "message": f"card_id {card_id} not found."}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": True, "data": response}
        )
    except Exception as error:
        raise HTTPException(
            400,
            detail=f"Error when trying to get card_id {card_id}"
        ) from error
