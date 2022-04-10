'''
Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.

'''


from random import randint


def sorteio():

    lista = []
    for i in range(10):
        list.append(randint(0, 100))

    return max(lista)

