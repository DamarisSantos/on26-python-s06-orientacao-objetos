'''
Implemente o método calcular_aluguel() em cada uma das subclasses para calcular o valor do aluguel com base em regras específicas:
Para Casa, o aluguel deve ser calculado como preco_base + (area_terreno * 5).
Para Apartamento, o aluguel deve ser calculado como preco_base + (numero_quartos * 300).
Exercício 4: Testando as Classes
Crie instâncias de Casa e Apartamento, atribuindo valores aos seus atributos. Em seguida, calcule e imprima o aluguel para cada uma das propriedades usando o método calcular_aluguel().
Exercício 5: Método de Exibição
Adicione um método chamado descricao() em cada uma das classes (Imovel, Casa, Apartamento) que retorna uma descrição completa da propriedade, incluindo todos os atributos relevantes. Por exemplo, para uma Casa, a descrição pode ser "Casa localizada em [endereco], área do terreno [area_terreno]m², aluguel R$ [calcular_aluguel()]".
Crie instâncias de Casa e Apartamento novamente e use o método descricao() para exibir informações detalhadas sobre cada propriedade.
mplemente o método calcular_aluguel() em cada uma das subclasses para calcular o valor do aluguel com base em regras específicas:
Para Casa, o aluguel deve ser calculado como preco_base + (area_terreno * 5).
Para Apartamento, o aluguel deve ser calculado como preco_base + (numero_quartos * 300).
e superclass tem o atributo endereco e nome_do_proprietario
'''

class Imovel:
    def __init__(self, endereco, nome_proprietario, preco_base):
        self.endereco = endereco
        self.nome_proprietario = nome_proprietario
        self.preco_base = preco_base

    def calcular_aluguel(self):
        return self.preco_base
    

class Casa(Imovel):
    def __init__(self, endereco, nome_proprietario, preco_base, area_terreno):
        super().__init__(endereco, nome_proprietario, preco_base)
        self.area_terreno = area_terreno

    def calcular_aluguel(self):
        resp = self.preco_base + (self.area_terreno * 5)
        return resp

class Apartamento(Imovel):
    def __init__(self, endereco, nome_proprietario, preco_base, numero_quartos):
        super().__init__(endereco, nome_proprietario, preco_base)
        self.numero_quartos = numero_quartos

    def calcular_aluguel(self):
        resp = self.preco_base + (self.numero_quartos * 300)
        return resp
    
casa_maria = Casa('122 Rua das Flores', 'Maria', 1500, 300)
print(casa_maria.calcular_aluguel())


apartamento_carlos = Apartamento('333, Av. Joao Mendes', 'Carlos', 1200, 2)
print(apartamento_carlos.calcular_aluguel())