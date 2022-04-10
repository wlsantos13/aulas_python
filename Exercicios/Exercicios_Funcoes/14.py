'''
Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista.

'''

def mediaitenslista(lista):
    soma = 0

    for n in lista:
        soma += n

    media = soma/len(lista)

    return media