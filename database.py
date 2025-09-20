from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#환경 가져오가ㅣ
load_dotenv()

#엔진 준비 (MYSQL + PYMYSQL)
engine = create_engine(os.getenv('DB_URL'))

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