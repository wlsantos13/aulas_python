'''
Faça uma função que receba duas listas e retorne o produto item a item dessas listas.

Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].
'''


def produtoListas(lista1, lista2):

    resultado = []

    for i in range(len(lista1)):
        resultado.append(lista1[i] * lista2[i])

    return resultado