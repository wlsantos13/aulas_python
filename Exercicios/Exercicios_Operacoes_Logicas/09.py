'''
Desafio 1 - Faça um programa que leia 3 números e informe o maior deles.

'''


n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))


if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
else:
    maior = n1

print('O maior número é:',maior)

