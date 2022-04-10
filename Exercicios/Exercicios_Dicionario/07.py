'''
Faça um programa que conte quantas vezes cada elemento aparece em uma 
lista (pode criar uma lista na mão). Esse programa deverá guardar os dados 
em um dicionário no qual as chaves são os elementos da lista e os valores são a contagem de quantas vezes esse elemento aparece.
'''

lista = ['banana', 'maca', 'pera','banana', 'melancia', 'pera','uva']

listadistinta = []
listafinal = {}

for f in lista:
    if f not in listadistinta:
        listadistinta.append(f)

for i in range(len(listadistinta)):
    listafinal{listadistinta[i]:lista.count(listadistinta[i])}

print(listafinal)