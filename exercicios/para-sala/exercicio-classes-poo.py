# Exercício 1

class cachorro: 
  def __init__(self, nome, raca):#init é o método construtor 
    self.nome = nome
    self.raca = raca

  def andar(self):
    print('Estou andando', self.nome)

  def info(self):
    print(self.nome, self.raca)

# pode ser criado diversos objetos com a base acima

cachorro_lulu = cachorro('Lulu', 'Harrier')

cachorro_rex = cachorro('Rex', 'Pinsher')

cachorro_lulu.info()

cachorro_rex.info()

cachorro_lulu.andar()

print(f'Nome do meu cachorro: {cachorro_lulu.nome}')

cachorro_rex.andar() 