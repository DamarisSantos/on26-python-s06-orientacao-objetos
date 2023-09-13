class Veiculo:
    def __init__(self, marca, modelo, ano ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def descricao(self):
        return super().descricao() + f', Números de portas: {self.portas}'
       

class Moto(Veiculo):
    def __init__ (self, marca, modelo, ano, motor):
        super().__init__(marca, modelo, ano) 
        self.motor = motor
      
    def descricao(self):
        return super().descricao() + f', tipo de motor: {self.motor}'
     

carro_damaris = Carro('Renualt', 'Sandero', 2018, 4)
print(carro_damaris.descricao())

moto_mammy = Moto('Suzuk', 'PCX', 2023, '4 tempos')
print(moto_mammy.descricao())

carro_joao = Carro('Fiat', 'Siena', 2021, 4)
print(carro_joao.descricao())