from typing import List, Optional

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Insight(BaseModel):
    descricao: str
    categoria: str
    tags: list = []

insights = {
    "1": {"descricao": "teste1", "categoria": "testeC1"},
    "2": {"descricao": "teste2", "categoria": "testeC2"},
    "3": {"descricao": "teste3", "categoria": "testeC3"},
}

# Criar insight

@app.post("/insight/create", status_code=status.HTTP_201_CREATED)
def create_insight(insight: Insight):
    return {"insight_descricao": insight.descricao, "insight_categoria": insight.categoria}


# Listar insight

@app.get("/insight/list", response_model=List[Insight])
def list_insights(insight: Insight):
    return {"insight_descricao": insight.descricao, "insight_categoria": insight.categoria}

# Pesquisar insight

@app.get("/insight/search/{termo}", response_model=Insight, response_model_exclude={"tags"})
def search_insight(termo: str):
    if termo not in insights:
        raise HTTPException(status_code=404, detail="Não foram encontrados insights com o termo digitado!")
    return insights[termo]