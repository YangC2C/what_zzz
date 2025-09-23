from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import FieldValidationInfo

class userCreate(BaseModel):
    id : str
    password1: str
    password2: str
    nickname: str
    
    @field_validator('id','password1','password2','nickname')
    def notEmpty(cls,v):
        if not v or not v.strip():
            raise ValueError('필수값입니다.')
        return v
    
    @field_validator('password2')
    def passwordCheck(cls, v, info: FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('비밀번호가 틀립니다.')
        return v
