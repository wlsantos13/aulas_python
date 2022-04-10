'''
Desafio - Faça uma função que receba uma string e uma letra x:

a. imprima quantas vezes a letra aparece na string;

b. imprima todas as posições em que a letra aparece na string;

c. retorne a distância entre a primeira e a última aparição dessa letra na string.
'''

def teste(string, letra):

    lista = list(string)
    contador = 0
    positions = []
    pos = 0

    for elemento in lista:
        if elemento == letra:
            positions.append(pos)
            contador += 1
        pos += 1

    distancia = max(positions) - min(positions)

    return contador, positions, distancia

print(teste('luan silva santos', 'i'))




