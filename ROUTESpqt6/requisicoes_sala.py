from pydantic import BaseModel
from fastapi import HTTPException,APIRouter
from connection import conexaoBanco

salaDeAula_router=APIRouter(prefix='/sala_de_aula', tags=['sala_de_aula'])

class sala(BaseModel):
    professor:int


# SELECIONANDO A SALA DE AULA
@salaDeAula_router.get("/")
def get_sala():
    cursor=conexaoBanco.cursor()
    comando_sql="SELECT * FROM Sala_de_aula"
    cursor.execute(comando_sql)
    resultado_consulta=cursor.fetchall()
    return resultado_consulta
# -------------------------------------------------------------------------------------------
# ADICIONANDO A SALA DE AULA SE NÃO TIVER SIDO CRIADA AINDA
@salaDeAula_router.post("/")
def post_sala(item:sala):
    cursor=conexaoBanco.cursor()    
    comando_sql_inserir='INSERT INTO Sala_de_aula (professor) VALUES (%(professor)s)'
    cursor.execute(comando_sql_inserir, {'professor': item.professor})
    conexaoBanco.commit()
    return {"message":"Sala de aula adicionada com sucesso!"}

# ---------------------------------------------------------------------------------------------
# ATUALIZANDO A SALA DE AULA
@salaDeAula_router.patch("/{id}")
def patch_sala(item:sala,id:int):
    cursor= conexaoBanco.cursor()
    comando_sql='SELECT * FROM Sala_de_aula WHERE id=%(id)s'
    cursor.execute(comando_sql, {'id': id})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is None:
        raise HTTPException(status_code=404, detail="Sala de Aula não encontrado")
    
    comando_sql_atualizar='UPDATE Sala_de_aula SET professor=%(professor)s WHERE id=%(id)s'
    cursor.execute(comando_sql_atualizar, {'professor': item.professor, 'id': id})
    conexaoBanco.commit()
    return {"message":"Sala de aula atualizado/alterado com sucesso!"}
# ---------------------------------------------------------------------------------------------
# DELETANDO UMA SALA DE AULA
@salaDeAula_router.delete("/{id}")
def delete_sala(id:int):
    cursor=conexaoBanco.cursor()
    comando_sql='SELECT * FROM Sala_de_aula WHERE id=%(id)s'
    cursor.execute(comando_sql, {'id': id})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is None:
        raise HTTPException(status_code=404, detail="Sala de aula não encontrada")
    
    comando_sql_deletar='DELETE FROM Sala_de_aula WHERE id=%(id)s'
    cursor.execute(comando_sql_deletar, {'id': id})
    conexaoBanco.commit()
    return {"message":"Sala de aula deletada com sucesso!"}
# ---------------------------------------------------------------------------------------------








