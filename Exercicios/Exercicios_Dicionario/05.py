'''
Crie uma função que receba os valores do nome, 
idade e e-mail de uma pessoa e guarde-os em um dicionário com as 
chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. Sua função deve retornar esse dicionário.
'''

def retornadic(nome, idade, email):
    lista = {
        'nome':'',
        'idade':'',
        'email':''
        }

    lista['nome'] = nome
    lista['idade'] = idade
    lista['email'] = email

    return lista


listafinal = retornadic('wangles', '41', 'wangles.santos@gmail.com')

print(listafinal)



