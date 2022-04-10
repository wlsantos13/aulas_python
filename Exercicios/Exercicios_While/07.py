'''
Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro.

'''


idade = int(input('Digite sua idade: '))

while idade < 0 or idade > 150:
    print('Vc digitou uma idade invalida!')
    idade = int(input('Digite sua idade: '))

salario = int(input('Digite sua salario: '))

while salario < 0:
    print('Vc digitou um salario invalido!')
    idade = int(input('Digite seu salario: '))

sexo = input('Digite sua sexo: ')

while sexo != 'M' and sexo != 'F' and sexo != 'Outro':
    print('Vc digitou um sexo invalido!')
    sexo = input('Digite seu salario: ')

print(idade, salario, sexo)