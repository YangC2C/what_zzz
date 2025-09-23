from pydantic import BaseModel, field_validator
import jwt
from datetime import datetime, timedelta, timezone
import key

class accessToken(BaseModel):
    accessToken : str
    tokentype : str
    id : str

def make_token(id):
    data = {
        "sub" : id,
        "exp" : datetime.now(timezone.utc) + timedelta(minutes=key.time)
    }
    token = jwt.encode(data,key.sc_key,algorithm=key.algo)
    
    return {
        'accessToken' : token,
        'tokentype' : 'bearer',
        'id' : id
    }
    