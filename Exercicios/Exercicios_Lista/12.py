'''
Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.

Obs.: Precisa usar a biblioteca random

'''

import random

lista = []
qtd = 0

for n in range(10):
    numero = random.randint(1,100)
    lista.append(numero)
    if numero > 50:
        qtd +=1

print(lista)
print('A quantidade de números maiores que 50 é:', qtd)
