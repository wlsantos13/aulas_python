'''
Faça um programa que imprima todos os itens de uma lista usando while e compare com o exercício 1.
'''


lista = ['Wangles', 'Lucia', 'Luan']
contador = 0

while contador < len(lista):
    print(lista[contador])
    contador += 1


for elemento in lista:
    print(elemento)