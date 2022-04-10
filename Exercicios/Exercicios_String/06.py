'''
Enunciado
Faça uma função que recebe uma string e retorna ela ao contrário.

Exemplo: Recebe "teste" e retorna "etset".
'''

def contrario(string):
    lista = list(string)
    lista.reverse()
    resultado = ''

    for elemento in lista:
        resultado += elemento

    return resultado

print(contrario('teste'))

