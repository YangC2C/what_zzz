from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import userFunction, userSchema

router = APIRouter(
    prefix= '/user'
)

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def user_create(newUser: userSchema.userCreate, db: Session =  Depends(get_db)):
    userFunction.createUser(db=db, userCreate= newUser)
    
