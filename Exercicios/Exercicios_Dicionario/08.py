'''
nunciado
Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. 
Se o usuário digitar 1, o programa deve cadastrar um novo usuário e guardar esse cadastro num dicionário cuja chave será o CPF da pessoa. 
Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados; 
e se o usuário digitar 3, o programa deve fechar.

Exemplo do dicionário:

‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’ : maria@mail.com}


'''

opcao = ''
lista = {}

while opcao != '3':
    print('#########  MENU DA APLICAÇÃO ##########')
    print('Digite 1 para cadastrar um novo usuário.')
    print('Digite 2 para listar os usuários cadastrados.')
    print('Digite 3 para fechar o programa.')
    opcao = input('Digite uma opção valida: ')

    if opcao == '1':
        cpf = input('Digite o cpf do usuario: ')
        nome = input('Digite o nome do usuario: ')
        idade = input('Digite a idade do usuario: ')
        email = input('Digite o email do usuario: ')
        lista.update({cpf:{'nome':nome, 'idade':idade, 'email':email}})
    elif opcao == '2':
        print(lista)
    else:
        print('Digite uma opção valida')

