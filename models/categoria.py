from produtoModel import Produto

class Categoria(Produto):
    def __init__(self, id:int, nome:str):
        self.id = id
        self.nome = nome
        self.lista = []

    def adicionarProduto(produto) -> list:
        
        