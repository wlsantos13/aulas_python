
'''Enunciado
Implemente um sistema de busca para o programa do exercício anterior. Isto é, se o usuário digitar 4, procure um determinado usuário pelo seu CPF.
'''


opcao = ''
lista = {}

while opcao != '3':
    print('#########  MENU DA APLICAÇÃO ##########')
    print('Digite 1 para cadastrar um novo usuário.')
    print('Digite 2 para listar os usuários cadastrados.')
    print('Digite 3 para fechar o programa.')
    print('Digite 4 para buscar usuario pelo cpf.')
    opcao = input('Digite uma opção valida: ')
    if opcao != '3':
        if opcao == '1':
            cpf = input('Digite o cpf do usuario: ')
            nome = input('Digite o nome do usuario: ')
            idade = input('Digite a idade do usuario: ')
            email = input('Digite o email do usuario: ')
            lista.update({cpf:{'nome':nome, 'idade':idade, 'email':email}})
        elif opcao == '2':
            print(lista)
        elif opcao == '4':
            cpf = input('Digite o cpf do usuario: ')
            for chaves in lista:
                if chaves == cpf:
                    print(lista[chaves])
        else:
            print('Digite uma opção valida')
    else:
        print('fim')
