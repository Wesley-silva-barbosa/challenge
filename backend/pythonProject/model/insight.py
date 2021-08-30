
class Insight:
    def __init__(self, id, descricao, categoria):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria

    def setId(self, id):
        self.id = id

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setCategoria(self, categoria):
        self.categoria = categoria

    def getId(self):
        return self.id

    def getDescricao(self):
        return self.descricao

    def getCategoria(self):
        return self.categoria