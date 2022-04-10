'''
Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.

Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].

'''

def somaListas(lista1, lista2):

    resultado = []

    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])

    return resultado