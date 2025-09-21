from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.userSchema import userCreate
from models import user

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