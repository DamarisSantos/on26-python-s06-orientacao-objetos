# Exercício 1

class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.conta = numero_conta
        self.titular = titular_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor 
            print(f'Valor depositado de R${valor}, realzado com sucesso:')
        else:
            print('O valor deve ser maior que 0')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -+ valor
                print(f'Saque de R${valor} realizado com sucesso.')
            else:
                print('O seu saldo não é suficiente.')
        else:
            print('O valor do saque deve ser maior que 0')


    def titular(self):
        print('Nome do títular:')

    def saldo(self):
        print('Saldo:')

contaDamaris = ContaBancaria(202301, 'Damaris')

contaDamaris.depositar(10000)

contaDamaris.sacar(120)

print(contaDamaris.saldo)

contaDaviny = ContaBancaria(202302, 'Lais')

contaDaviny.depositar(80)

contaDaviny.sacar(1000)

print(contaDaviny.saldo)


