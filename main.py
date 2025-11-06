from fastapi import FastAPI
from Routes.products import products_router
from Routes.users import user_router
from ROUTESpqt6.requisicoes_sala import salaDeAula_router
from ROUTESpqt6.requisicoes_professores import professores_router
from ROUTESpqt6.requisicoes_aluno import aluno_router
from ROUTESpqt6.requisicoes_alunos_da_sala import alunos_da_sala_router

app = FastAPI()

app.include_router(products_router)
app.include_router(user_router)
app.include_router(salaDeAula_router)
app.include_router(professores_router)
app.include_router(aluno_router)
app.include_router(alunos_da_sala_router)

@app.get("/")
def rota_inicial():
    return { 
        "message": "Olá mundo" 
    }
    
@app.get("/teste")
def rota_teste():
    return {
        "message": "Tá funcionando"
    }
    