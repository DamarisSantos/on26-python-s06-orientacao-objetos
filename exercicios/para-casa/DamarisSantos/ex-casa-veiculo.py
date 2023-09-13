'''
## 👩🏻‍💻 Crie uma classe base chamada Veiculo com os seguintes atributos:

- modelo: o modelo do veículo (uma string).
- ano: o ano de fabricação do veículo (um número inteiro).
preco: o preço do veículo (um número decimal).
Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. O imposto é calculado como 10% do preço do veículo.

Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:

- marca: a marca do carro (uma string).
Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

- cilindrada: a cilindrada da moto (um número inteiro).
Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. O imposto para motos é de 5% do preço do veículo.

Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.'''
# Exercício para casa 
# Damaris Santos

class Veiculo:
    def __init__(self, valor, modelo, ano): 
        self.valor = valor
        self.modelo = modelo
        self.ano = ano

    def calcular_imposto (self):      
        return self.valor * 0.1

class Carro(Veiculo):
    def __init__(self, valor, modelo, ano, marca):
        super().__init__(valor, modelo, ano)
        self.marca = marca

    def calcular_desconto(self):
        imposto = self.calcular_imposto()
        desconto = (self.valor) * 0.05
        return desconto
    
    def calcular_imposto(self):
        imposto = super().calcular_imposto()
        return imposto 
    
    def valor_total(self):
        valor_total = super().calcular_imposto()
        valor_imposto = self.valor + valor_total
        return valor_imposto - self.calcular_desconto()
    
class Moto(Veiculo):    
    def __init__(self, calcular_imposto, modelo, ano, cilindrada):
        super().__init__(calcular_imposto, modelo, ano) 
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        imposto = super().calcular_imposto()
        imposto_moto = imposto * 0.5
        return imposto - imposto_moto
            
    def valor_total(self):
        valor_total = super().calcular_imposto()
        valor_imposto = valor_total + self.valor
        return valor_imposto  - self.calcular_imposto()
     
carro_damaris = Carro(10000, 'Sandero', 2018, 'Renualt')
imposto_carro = carro_damaris.calcular_imposto()
valor_total_carro = carro_damaris.valor_total()
desconto = carro_damaris.calcular_desconto()
print(f'O carro {carro_damaris.modelo} {carro_damaris.ano} {carro_damaris.marca} custa R$ {carro_damaris.valor:}.')
print(f'O valor do desconto é R${desconto}.')      
print(f'O imposto é de R${imposto_carro}.')  
print(f'O valor final do carro é R${valor_total_carro}.\n')

moto = Moto(1000, 'PCX', 2023, 250)
imposto_moto = moto.calcular_imposto()
valor_total_moto = moto.valor_total()
print(f'A moto {moto.modelo} {moto.ano} de {moto.cilindrada} cilindradas custa R${moto.valor}')
print(f'O imposto é de R${imposto_moto}')
print(f'O valor final da moto é R${valor_total_moto}')
