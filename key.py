import os
from dotenv import load_dotenv

#환경 가져오가ㅣ
load_dotenv()

# token
sc_key = os.getenv('SECRECT_KEY')
algo = os.getenv('ALGORITHM')
time = int(os.getenv('ACCESS_TOKEN_TIME'))

# db
db =os.getenv('DB_URL')