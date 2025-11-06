from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from connection import conexaoBanco

user_router = APIRouter(prefix='/users', tags=['users'])

class Produto(BaseModel):
    name: str


@user_router.get("/")
def get_sala():
    cursor= conexaoBanco.cursor(dictionary=True)
    comando_sql="SELECT * FROM produtos"
    cursor.execute(comando_sql)
    resultado_consulta= cursor.fetchall()
    return resultado_consulta