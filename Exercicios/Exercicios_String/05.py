'''
Faça uma função que receba uma string e retorne uma nova string substituindo:

'a' por '4'

'e' por '3'

'I' por '1'

't' por '7'
'''


def substituicao(string):
    resultado = string.replace('a', '4')
    resultado = resultado.replace('e','3')
    resultado = resultado.replace('I','1')
    resultado = resultado.replace('t','7')

    return resultado



print(substituicao('aeIt'))