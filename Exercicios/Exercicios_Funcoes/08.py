'''
Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna a média deles.

'''

from random import randint


def medianumeros(qtd):
    lista = []
    soma = 0
    for i in range(qtd):
       lista.append(randint(0,100))

    for n in lista:
        soma += n
    media = soma/len(lista)

    return media


print(medianumeros(4))