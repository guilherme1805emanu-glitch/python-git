from pydantic import BaseModel
from fastapi import HTTPException,APIRouter
from connection import conexaoBanco

aluno_router=APIRouter(prefix='/Aluno', tags=['Aluno'])

class Aluno(BaseModel):
    nome:str   
    idade:int
    turma:str
    nota_media:int
    cidade:str


# SELECIONANDO O ALUNO
@aluno_router.get("/")
def get_Aluno():
    cursor=conexaoBanco.cursor()
    comando_sql="SELECT * FROM Aluno"
    cursor.execute(comando_sql)
    resultado_consulta=cursor.fetchall()
    return resultado_consulta
# -------------------------------------------------------------------------------------------
# ADICIONANDO ALUNO SE NÃO TIVER SIDO CRIADO AINDA
@aluno_router.post("/")
def post_Aluno(item:Aluno):
    cursor=conexaoBanco.cursor()
    comando_sql_verificar='SELECT * FROM Aluno WHERE nome=%(nome)s'
    cursor.execute(comando_sql_verificar, {'nome': item.nome})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is not None:
        raise HTTPException(status_code=400, detail="Aluno já cadastrado")
    
    comando_sql_inserir='INSERT INTO Aluno (nome,idade,turma,nota_media,cidade) VALUES (%(nome)s, %(idade)s, %(turma)s, %(nota_media)s, %(cidade)s)'
    cursor.execute(comando_sql_inserir, {'nome': item.nome, 'idade': item.idade, 'turma': item.turma, 'nota_media': item.nota_media, 'cidade': item.cidade})
    conexaoBanco.commit()
    return {"message":"Aluno adicionado com sucesso!"}
# ---------------------------------------------------------------------------------------------
# ATUALIZANDO/ALTERANDO O ALUNO
@aluno_router.patch("/{id}")
def patch_Aluno(item:Aluno,id:int):
    cursor= conexaoBanco.cursor()
    comando_sql='SELECT * FROM Aluno WHERE id=%(id)s'
    cursor.execute(comando_sql, {'id': id})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    comando_sql_atualizar='UPDATE Aluno SET nome=%(nome)s, idade=%(idade)s, turma=%(turma)s, nota_media=%(nota_media)s, cidade=%(cidade)s WHERE id=%(id)s'
    cursor.execute(comando_sql_atualizar, {'nome': item.nome, 'idade': item.idade, 'turma': item.turma, 'nota_media': item.nota_media, 'cidade': item.cidade, 'id': id})
    conexaoBanco.commit()
    return {"message":"Aluno atualizado/alterado com sucesso!"}
# ---------------------------------------------------------------------------------------------
# DELETANDO UM ALUNO
@aluno_router.delete("/{id}")
def delete_Aluno(id:int):
    cursor=conexaoBanco.cursor()
    comando_sql='SELECT * FROM Aluno WHERE id=%(id)s'
    cursor.execute(comando_sql, {'id': id})
    resultado_consulta= cursor.fetchone()

    if resultado_consulta is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    comando_sql_deletar='DELETE FROM Aluno WHERE id=%(id)s'
    cursor.execute(comando_sql_deletar, {'id': id})
    conexaoBanco.commit()
    return {"message":"Aluno deletado com sucesso!"}
# ---------------------------------------------------------------------------------------------