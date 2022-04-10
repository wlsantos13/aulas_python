'''
Desafio 1 - Faça uma função que receba um número e calcule seu fatorial.
'''


def fatorial(x):

    resultado = x

    for i in range(1, x):
        resultado *= i

    return resultado