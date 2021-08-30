from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#cria
@app.post("/insights/", response_model=schemas.Insight)
def create_insight(insight: schemas.Insight, db: Session = Depends(get_db)):
    return crud.create_insight(db=db, insight=insight)

#lista todos
@app.get("/insights/{skip}/{limit}", response_model=List[schemas.Insight])
def get_insights(skip: int, limit: int, db: Session = Depends(get_db)):
    insights = crud.get_insights(db, skip=skip, limit=limit)
    return insights

#pesquisa por palavra
@app.get("/insights/{word}", response_model=List[schemas.Insight])
def get_insight_by_word(word: str, db: Session = Depends(get_db)):
    db_insight = crud.get_insight_by_word(db, word=word)
    if word is None:
        raise HTTPException(status_code=404, detail="Nenhum insight encontrado")
    return db_insight