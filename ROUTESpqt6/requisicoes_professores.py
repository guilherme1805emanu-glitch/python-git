from pydantic import BaseModel
from fastapi import HTTPException,APIRouter
from connection import conexaoBanco

professores_router=APIRouter(prefix='/professores', tags=['professores'])

class professor(BaseModel):
    nome:str


# SELECIONANDO  professor
@professores_router.get("/")
def get_professor():
    cursor=conexaoBanco.cursor()
    comando_sql="SELECT * FROM professor"
    cursor.execute(comando_sql)
    resultado_consulta=cursor.fetchall()
    return resultado_consulta
# -------------------------------------------------------------------------------------------
# ADICIONANDO A SALA DE AULA SE NÃO TIVER SIDO CRIADA AINDA
@professores_router.post("/")
def post_professor(item:professor):
    cursor=conexaoBanco.cursor()
    comando_sql_verificar='SELECT * FROM professor WHERE nome=%(nome)s'
    cursor.execute(comando_sql_verificar, {'nome': item.nome})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is not None:
        raise HTTPException(status_code=400, detail="professor já cadastrado")
    
    comando_sql_inserir='INSERT INTO professor (nome) VALUES (%(nome)s)'
    cursor.execute(comando_sql_inserir, {'nome': item.nome})
    conexaoBanco.commit()
    return {"message":"professor adicionado com sucesso!"}
# ---------------------------------------------------------------------------------------------
# ATUALIZANDO/ALTERANDO O PROFESSOR
@professores_router.patch("/{id}")
def patch_professor(item:professor,id:int):
    cursor= conexaoBanco.cursor()
    comando_sql='SELECT * FROM professor WHERE id=%(id)s'
    cursor.execute(comando_sql, {'id': id})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is None:
        raise HTTPException(status_code=404, detail="professor não encontrado")
    
    comando_sql_atualizar='UPDATE professor SET nome=%(nome)s WHERE id=%(id)s'
    cursor.execute(comando_sql_atualizar, {'nome': item.nome, 'id': id})
    conexaoBanco.commit()
    return {"message":"professor atualizado/alterado com sucesso!"}
# ---------------------------------------------------------------------------------------------
# DELETANDO UM professor
@professores_router.delete("/{id}")
def delete_professor(id:int):
    cursor=conexaoBanco.cursor()
    comando_sql='SELECT * FROM professor WHERE id=%(id)s'
    cursor.execute(comando_sql, {'id': id})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is None:
        raise HTTPException(status_code=404, detail="professor não encontrado")
    
    comando_sql_deletar='DELETE FROM professor WHERE id=%(id)s'
    cursor.execute(comando_sql_deletar, {'id': id})
    conexaoBanco.commit()
    return {"message":"professor deletado com sucesso!"}
# ---------------------------------------------------------------------------------------------