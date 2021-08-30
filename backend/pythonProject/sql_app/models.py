from sqlalchemy import Column, Integer, String

from .database import Base

class Insight(Base):

    __tablename__ = "insights"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), index=True)
    categoria = Column(String(255), index=True)
