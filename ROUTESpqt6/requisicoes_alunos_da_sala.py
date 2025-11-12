from pydantic import BaseModel
from fastapi import HTTPException,APIRouter
from connection import conexaoBanco

alunos_da_sala_router=APIRouter(prefix='/alunos_da_sala', tags=['alunos_da_sala'])

class alunos_da_sala(BaseModel):
    id_aluno:int
    id_sala:int


# SELECIONANDO Os ALUNOs
@alunos_da_sala_router.get("/")
def get_Aluno_da_sala():
    cursor=conexaoBanco.cursor()
    comando_sql="SELECT * FROM alunos_salas_de_aula"
    cursor.execute(comando_sql)
    resultado_consulta=cursor.fetchall()
    return resultado_consulta
# -------------------------------------------------------------------------------------------
# ADICIONANDO ALUNOS NA TABELA alunos_salas_de_aula SE NÃO TIVER SIDO ADICIONADO AINDA.
@alunos_da_sala_router.post("/")
def post_Aluno_na_sala(aluno_sala:alunos_da_sala):
    cursor=conexaoBanco.cursor()
    comando_sql_verificacao="SELECT * FROM alunos_salas_de_aula WHERE id_aluno=%s AND id_sala=%s"
    valores_verificacao=(aluno_sala.id_aluno,aluno_sala.id_sala)
    cursor.execute(comando_sql_verificacao,valores_verificacao)
    resultado_verificacao=cursor.fetchone()

    if resultado_verificacao:
        raise HTTPException(status_code=400, detail="Aluno já está adicionado nesta sala.")
    
    comando_sql_insercao="INSERT INTO alunos_salas_de_aula (id_aluno, id_sala) VALUES (%s, %s)"
    valores_insercao=(aluno_sala.id_aluno,aluno_sala.id_sala)
    cursor.execute(comando_sql_insercao,valores_insercao)
    conexaoBanco.commit()
    return {"mensagem":"Aluno adicionado à sala com sucesso."}

# -------------------------------------------------------------------------------------------------------------------------------------------
# ATUALIZANDO/MODIFICANDO O ID DA SALA DE UM ALUNO
@alunos_da_sala_router.patch("/{id_aluno}")
def patch_Aluno_na_sala(id_aluno:int, aluno_sala:alunos_da_sala):
    cursor=conexaoBanco.cursor()
    comando_sql_verificacao="SELECT * FROM alunos_salas_de_aula WHERE id_aluno=%s"
    valores_verificacao=(id_aluno,)
    cursor.execute(comando_sql_verificacao,valores_verificacao)
    resultado_verificacao=cursor.fetchone()

    if not resultado_verificacao:
        raise HTTPException(status_code=404, detail="Aluno não encontrado nesta sala.")
    
    comando_sql_atualizacao="UPDATE alunos_salas_de_aula SET id_sala=%s WHERE id_aluno=%s"
    valores_atualizacao=(aluno_sala.id_sala,id_aluno)
    cursor.execute(comando_sql_atualizacao,valores_atualizacao)
    conexaoBanco.commit()
    return {"mensagem":"Sala do aluno atualizada com sucesso."}

# -------------------------------------------------------------------------------------------------------------------------------------------
# DELETANDO UM ALUNO DA SALA
@alunos_da_sala_router.delete("/{id_aluno}")
def delete_Aluno_da_sala(id_aluno:int):
    cursor=conexaoBanco.cursor()
    comando_sql_verificacao="SELECT * FROM alunos_salas_de_aula WHERE id_aluno=%s"
    valores_verificacao=(id_aluno,)
    cursor.execute(comando_sql_verificacao,valores_verificacao)
    resultado_verificacao=cursor.fetchone()

    if not resultado_verificacao:
        raise HTTPException(status_code=404, detail="Aluno não encontrado nesta sala.")
    
    comando_sql_delecao="DELETE FROM alunos_salas_de_aula WHERE id_aluno=%s"
    valores_delecao=(id_aluno,)
    cursor.execute(comando_sql_delecao,valores_delecao)
    conexaoBanco.commit()
    return {"mensagem":"Aluno removido da sala com sucesso."}


