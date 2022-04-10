'''
Crie uma classe ContaCorrente com os atributos cliente (que deve ser um objeto da classe Cliente) e saldo. 
Crie métodos para depósito, saque e transferência. Os métodos de saque e transferência devem verificar se 
é possível realizar a transação.

'''

class Cliente:

    def __init__(self, cpf, nome, dtnascimento):
        self.cpf = cpf
        self.nome = nome
        self.dtnascimento = dtnascimento


class Conta:

    def __init__(self, Cliente):
        self.Cliente = Cliente
        self.saldo = 0.0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo - valor < 0:
            print(f'Saldo Insuficiente, seu saldo é de R$ {self.saldo}')
        else:
            self.saldo -= valor

    def transferencia(self, valor, Conta):
        if self.saldo - valor < 0:
            print(f'Saldo Insuficiente, seu saldo é de R$ {self.saldo}')
        else:
            self.saque(valor)
            Conta.deposito(valor)

    def mostrarSaldo(self):
        return self.saldo


clie1 = Cliente('04787606638', 'wangles', '13/11/1980')
clie2 = Cliente('22244455532', 'Luan', '08/04/2004')

conta1 = Conta(clie1)
conta2 = Conta(clie2)

conta1.deposito(500.00)

print(conta1.mostrarSaldo())

conta1.saque(100)

print(conta1.mostrarSaldo())

conta1.transferencia(100.00, conta2)

print(conta1.mostrarSaldo())
print(conta2.mostrarSaldo())
