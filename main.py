from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

tarefas=[]

@app.get("/tarefas")
def listar_tarefas():
    global tarefas
    return tarefas

@app.post("/registrar/tarefa")
def registrar_tarefa(tarefa : Tarefa):
    
    nova_tarefa = {
        "titulo": tarefa.titulo,
        "concluida": tarefa.concluida,
    }
    
    tarefas.append(nova_tarefa)
    
    return {
        "menssagem": "Tarefa cadastra com sucesso!",
        "titulo": tarefa.titulo,
        "concluida": tarefa.concluida,
    }
    


    