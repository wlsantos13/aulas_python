'''
Super Desafio! - faça uma função que criptografa uma mensagem substituindo cada letra pela letra oposta do dicionário:

'a' por 'z'

'b' por 'y'

'c' por 'x'
'''


def teste(string):

    texto = list(string)
    dicionario = list('abcdefghijklmnopqrstuvwxyz')
    texto2 = ''

    for elemento in texto:
        for i in range(len(dicionario)):
            if elemento == dicionario[i]:
                texto2 += dicionario[(len(dicionario) - 1) - i]
    return texto2

print(teste('luan'))


