import sys

sys.path.append('../../../')

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.use_cases.auth_user import UserUseCases
from app.database.schemas import User

router = APIRouter(prefix='/v1')


@router.post('/users')
def user_register(user: User, db_session: Session = Depends(get_db_session)):
    use_case = UserUseCases(db_session=db_session)
    use_case.user_register(user=user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": True, "message": "User registered successfully!"}
    )


@router.post('/login')
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
