from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import userSchema, userService

from fastapi.security import OAuth2PasswordRequestForm

from domain.token import aboutToken

router = APIRouter(
    prefix= '/user'
)

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def user_create(newUser: userSchema.userCreate, 
                db: Session =  Depends(get_db)):
    userService.createUser(db=db, userCreate= newUser)
    
@router.post('/login', response_model=aboutToken.accessToken, status_code=status.HTTP_200_OK)
def user_login(formData : OAuth2PasswordRequestForm = Depends(),
               db : Session = Depends(get_db)):
    return userService.login_process(formData,db)