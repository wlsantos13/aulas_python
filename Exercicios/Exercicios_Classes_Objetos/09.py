'''
Enunciado
Com base no exercício anterior, crie um sistema de cadastro e a classe Cliente. Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.

Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros. Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente, alterar um cadastro ou sair.
'''

from re import I


class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    # def __repr__(self):
    #     return f'Nome: {self.nome}, Idade: {self.idade}, E-mail: {self.email}\n'

class Sistema:

    def __init__(self):

        self.Clientes = []

    def cadastroCliente(self, Cliente):
        if Cliente not in self.Clientes:
            self.Clientes.append({'Nome':Cliente.nome, 'Idade':Cliente.idade, 'c':Cliente.email})

    def ListarClientes(self):
        print(self.Clientes)

    def alterarCadastro(self, name, op, valor):
          
        for i in range(len(self.Clientes)):
            if self.Clientes[i]['Nome'] == name and op == '1':
                self.Clientes[i]['Idade'] = valor
            elif self.Clientes[i]['Nome'] == name and op == '2':
                self.Clientes[i]['Email'] = valor


menu = Sistema()

opcao = ''

while opcao != '0':

    print('MENU DO SISTEMA')
    print('1 - Cadastro novo Usuário')
    print('2 - Alterar Cadastro')
    print('3 - Listar Usuaŕios Cadastrados') 
    print('0 - Sair')    
    opcao = input('Escolha uma opção válida: ')
    if opcao == '1':
        nome = input('Digite o nome do Cliente: ')
        idade = input('Digite a idade do Cliente: ')
        email = input('Digite o email do cliente: ')  

        cliente1 = Cliente(nome, idade, email)
        
        menu.cadastroCliente(cliente1)
    elif opcao == '2':
        name = input('Digite o nome do Cliente que deseja alterar: ')
        op = input('Digite 1 para alterar a idade e 2 para alterar email: ')
        valor = input('Digite o novo valor: ')
        menu.alterarCadastro(name, op, valor)
        print('Atualização Efetuada')
        
    elif opcao == '3':
        menu.ListarClientes()
print('fim')
