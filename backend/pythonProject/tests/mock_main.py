from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "unitTest"

fake_db = {
    "insight1": {"id": 1, "descricao": "Arrascaeta fez a diferença e garantiu a vitória para o time rubro-negro.", "categoria": "JOGADOR"},
    "insight2": {"id": 2, "descricao": "O Flamengo não conseguia vencer um time na Argentina há mais de 40 anos", "categoria": "HISTÓRICO"},
}

app = FastAPI()


class Insight(BaseModel):
    id: int
    descricao: str
    categoria: str


@app.get("/insights/")
async def read_insights(x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return fake_db


@app.post("/insights/", response_model=Insight)
async def create_insight(insight: Insight, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return insight
