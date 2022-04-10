'''
Enunciado
Agora faça uma função que recebe uma palavra e diz se ela é um palíndromo, ou seja, se ela é igual a ela mesma ao contrário.

Dica: Use a função do exercício 6.

'''


def contrario(string):
    lista = list(string)
    lista.reverse()
    novastring = ''

    for elemento in lista:
        novastring += elemento

    if string == novastring:
        print('A String é um palindromo')
    else:
        print('A String não é um palidromo')

contrario('wangles')

