'''
Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da lista anterior, porém escritas em caixa alta.
'''

def maiuscula(lista):
    maiusculas = []
    for nome in lista:
        m = nome.upper()
        maiusculas.append(m)
    return maiusculas


nomes = ['wangles', 'luan']
print(maiuscula(nomes))