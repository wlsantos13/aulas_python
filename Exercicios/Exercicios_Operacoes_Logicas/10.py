'''
Desafio 2 - Faça o mesmo programa do exercício anterior, porém com 4 números.

'''


n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
n4 = float(input('Digite o Quarto numero: '))



if n2 > n1 and n2 > n3 and n2 > n4:
    maior = n2
elif n3 > n2 and n3 > n4 and n3 > n1: 
    maior = n3
elif n4 > n3 and n4 > n2 and n4 > n1: 
    maior = n4
else:
    maior = n1


print('O maior número é:',maior)