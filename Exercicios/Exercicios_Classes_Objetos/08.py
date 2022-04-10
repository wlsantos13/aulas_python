'''
Crie uma classe Cliente cujos atributos são nome, idade e e-mail. 
Construa um método que imprima as informações tal como abaixo:

Nome: Fulano de Tal

Idade: 40

E-mail: fulano@mail.com
'''


class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __repr__(self):
        return f'None: {self.nome}\n\nIdade: {self.idade}\n\nE-mail: {self.email}\n'

clie1 = Cliente('Fulano de Tal', 40, 'fulano@mail.com')

print(clie1)