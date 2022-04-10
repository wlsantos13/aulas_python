'''
Desafio 2 - Faça uma função que recebe duas entradas: um input dado pelo usuário e 
um string que informa o tipo de dado ("idade", "salário" ou "sexo"),
 e verifica se os dados digitados foram válidos, usando os seguintes critérios:

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro.
'''

def teste():
    dicio = {}
    sexo = ['M', 'F', 'Outro']
    tiposdados = ['idade', 'sexo', 'salario']
    cpf = input('Digite seu cpf: ')
    tipodado = input('Digite o tipo de dados (idade, sexo, salario): ')
    while tipodado not in tiposdados:
        print('Digite um tipo de dados válido (idade, sexo, salario: ')
        tipodado = input('Digite o tipo de dado: ')
    valordado = input('Digite o valor do dado: ')

    dict = {tipodado: valordado}
    if 'idade' in dict:
        while int(dict['idade']) < 0 or int(dict['idade']) > 150:
            print('valor Invalido, digite um valor maior que 0 e menor que 150')
            dict['idade'] = int(input('digite novamente o valor: '))
        dicio[cpf] = dict    
    elif 'sexo' in dict:
        while (dict['sexo']) not in sexo:
            print('valor Invalido, digite um sexo valido (M, F, Outros): ')
            dict['sexo'] = input('digite novamente o sexo: ')
        dicio[cpf] = dict
    elif 'salario' in dict:
        while float(dict['salario']) <= 0.0:
            print('valor Invalido, digite um salario valido (maior que 0): ')
            dict['salario'] = input('digite novamente o salario: ')
        dicio[cpf] = dict  

    return dicio


print(teste())
