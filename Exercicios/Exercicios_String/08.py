'''
Enunciado
Faça uma função que receba um texto e uma palavra, então verifique se a palavra está no texto, retornando True ou False.
'''

def palavraintext(string, texto):
    listapalavras = texto.split()

    if string in listapalavras:
        return True
    else:
        return False

palavra = 'bonito'
texto = 'o wangles é bonito e inteligente'

print(palavraintext(palavra, texto))