'''
Faça um programa que leia a validade das informações:

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação inválida.
'''

idade = float(input('Digite a sua idade: '))
if idade < 0 or idade > 150:
    print('erro')
else:
    salario = float(input('Digite a seu Salário: '))
    if salario < 0:
        print('erro')
    else:
        sexo = input('Digite seu sexo: ')
        if sexo != 'M' and sexo != 'F' and sexo != 'Outro':
            print('erro')
        else:
            print(idade, salario, sexo)