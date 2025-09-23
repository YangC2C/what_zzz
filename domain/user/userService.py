from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.userSchema import userCreate
from models import user
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import HTTPException
from starlette import status
from domain.token.aboutToken import make_token

#유저 찾아오기
def get_id(db : Session, id : str):
    return db.query(user).filter(user.user_id == id).first()

#비밀번호 암호화
pw_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

def createUser(db : Session, userCreate: userCreate):
    newUser = user(
        user_id = userCreate.id,
        user_password = pw_context.hash(userCreate.password1),
        nickname = userCreate.nickname
    )
    
    db.add(newUser)
    db.commit()
    
def login_process(formData : OAuth2PasswordRequestForm,
                  db : Session):
    ch_id = get_id(db, formData.username)
    print(ch_id)
    if not ch_id or not pw_context.verify(formData.password, ch_id.user_password):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                            detail="아이디나 비빌번호를 확인하세요",
                            headers={"WWW-Authenticate": "Bearer"})
    
    return make_token(ch_id.user_id)
