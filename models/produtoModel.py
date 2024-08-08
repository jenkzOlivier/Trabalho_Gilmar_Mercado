from categoria import Categoria

class Produto(object):
    def __init__(self, codigo_de_barras: str, nome: str, 
                 categoria: Categoria, preCompra: float, precoVenda: float, QuantidadeEstoque: int):
        
        self._codigo_de_barras = codigo_de_barras
        self.nome = nome
        self.categoria = categoria
        self.preCompra = preCompra
        self.precoVenda = precoVenda
        self._QuantidadeEstoque = QuantidadeEstoque

    def atualizarEstoque(self,QuantidadeEstoque: int) -> int:
        self.QuantidadeEstoque = QuantidadeEstoque
        print(f"estou foi alterado para {QuantidadeEstoque}")
    
    def registrarVendas(self, precoVendas: float, quantidadeVendida: int) -> int:
        self.precoVenda = precoVendas
        self.quantidadeVendida = quantidadeVendida - QuantidadeEstoque()
    
