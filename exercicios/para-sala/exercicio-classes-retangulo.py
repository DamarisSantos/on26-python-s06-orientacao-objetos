# exercício 2 

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
 #       print(f'Calcular a área{self.largura * self.altura}')
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
casa_damaris = Retangulo(21.0, 7.0)

print(f'A casa da Damaris tem: {casa_damaris.calcular_area()} m²')

print(f'A casa da Damaris tem: {casa_damaris.calcular_perimetro()} de perímetro')


casa_daviny = Retangulo(9.0, 10.5)

print(casa_daviny.calcular_area())
print(casa_daviny.calcular_perimetro())