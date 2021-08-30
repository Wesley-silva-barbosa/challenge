from sqlalchemy.orm import Session
from sqlalchemy import or_

from . import models, schemas

def get_insight_by_word(db: Session, word: str):
    search = "%{}%".format(word)
    return db.query(models.Insight).filter(or_(models.Insight.descricao.like(search), models.Insight.categoria.like(search))).all()

def get_insights(db: Session, skip: int, limit: int):
    return db.query(models.Insight).offset(skip).limit(limit).all()

def create_insight(db: Session, insight: schemas.Insight):
    db_insight = models.Insight(descricao=insight.descricao, categoria=insight.categoria)
    db.add(db_insight)
    db.commit()
    db.refresh(db_insight)
    return db_insight
