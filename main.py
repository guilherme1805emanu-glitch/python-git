from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rota_inicial():
    return {"message": "Hello, World!"}
