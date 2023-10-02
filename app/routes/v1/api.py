import sys

sys.path.append('../../../')

from fastapi import APIRouter

router = APIRouter(prefix='v1')

@router.post('/users')
def user_register():
    pass