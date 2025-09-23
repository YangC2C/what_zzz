from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import key


#엔진 준비 (MYSQL + PYMYSQL)
engine = create_engine(key.db)

#세션
SessionLocal = sessionmaker(autoflush= False, autocommit = False, bind=engine)

#DB 모델 베이스
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
