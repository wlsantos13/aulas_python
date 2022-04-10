'''
Faça uma função que recebe um número x e uma lista numérica e retorna uma lista cujos elementos são os itens da lista de entrada multiplicado por x.

Exemplo:

Se a função receber o número 5 e a lista [3,5,1], então a função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5].

'''

def produtoLista(x, lista1):

    resultado = []

    for i in range(len(lista1)):
        resultado.append(x * lista1[i])

    return resultado