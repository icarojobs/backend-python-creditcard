import sys

sys.path.append('../../../')

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi import status
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.controllers.auth_user import UserUseCases
from app.database.schemas import User

router = APIRouter(prefix='/v1')


@router.post('/users')
def user_register(user: User, db_session: Session = Depends(get_db_session)):
    use_case = UserUseCases(db_session=db_session)
    use_case.user_register(user=user)

    return JSONResponse(
        content={"status": True, "message": "User registered successfully!"},
        status_code=status.HTTP_201_CREATED
    )
