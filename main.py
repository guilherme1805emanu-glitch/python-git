from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rota_inicial():
    return {"message": "Hello, World!"}

@app.get("/teste")
def rota_teste():
    return {"message": "Rota de teste funcionando!"}
