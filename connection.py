from pymysql import connect
from pymysql.cursors import DictCursor
import os
import dotenv

dotenv.load_dotenv()

conexaoBanco= connect(
    host= os.getenv("DATABASE_HOST"),
    port=int(os.getenv("DATABASE_PORT")),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_DB"),
    cursorclass=DictCursor
)