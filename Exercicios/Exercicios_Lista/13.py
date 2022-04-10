'''
Enunciado
Faça um programa que sorteie 10 números entre 0 e 100 e imprima:

a. o maior número sorteado;

b. o menor número sorteado;

c. a média dos números sorteados;

d. a soma dos números sorteados.

Obs.: Precisa usar a biblioteca random
'''

import random

lista = []
soma = 0

for n in range(10):
    numero = random.randint(1,100)
    lista.append(numero)
    soma += numero

media = soma / len(lista)
print(lista)
print(max(lista))
print(min(lista))
print(media)
print(soma)