from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class user(Base):
    #__tablename__은 형식임 테이블의 이름을 담당함
    __tablename__ = 'users'
    #칼럼
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(16), unique= True, nullable=False)
    user_password = Column(String(255), nullable=False)
    nickname = Column(String(16), unique=True, nullable= False)
    
    # 1:n
    people = relationship("person", back_populates= 'owner')
    
    
class person(Base):
    __tablename__ = 'people'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(16), unique=True, nullable=True)
    money = Column(Integer, default=0)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship('user', back_populates='people')
    