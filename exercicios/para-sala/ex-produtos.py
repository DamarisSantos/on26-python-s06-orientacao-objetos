class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
          return f'Nome do produto: {self.nome},\nPreço R$ {self.preco},\n'
    
class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes

    def descricao(self):
        return super().descricao() + f'Peso do produto: {self.peso} kg,\nDimensões: {self.dimensoes} cm'


class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho = tamanho_arquivo

    def descricao(self):
        return super().descricao() + f'Tamanho do arquivo: {self.tamanho} MB. '
  
produto_fisico_damaris = ProdutoFisico('Livro', 30, 0.5, '20x15x3')
print(produto_fisico_damaris.descricao())

produto_digital_damaris = ProdutoDigital('Ebook', 50.00, 10)
print(produto_digital_damaris.descricao())