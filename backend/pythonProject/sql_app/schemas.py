from pydantic import BaseModel

class Insight(BaseModel):
    id: int
    descricao: str
    categoria: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True





