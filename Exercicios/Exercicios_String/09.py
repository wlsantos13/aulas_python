'''
Faça uma função que receba uma string que contém tanto números quanto letras e caracteres especiais,
 e que separe as letras em uma variável e os números em outra (os caracteres especiais podem ser descartados).
  Ao final a função deve imprimir as duas variáveis.
'''

def teste(string):
    texto = list(string)
    listaletras = []
    listanumeros = []

    for elemento in texto:
        if elemento.isalpha():
            listaletras.append(elemento)
        elif elemento.isdigit():
            listanumeros.append(elemento)
    return listaletras, listanumeros

print(teste('1a5b3e4dfg*%&'))