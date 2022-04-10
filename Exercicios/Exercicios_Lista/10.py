'''
Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas.
'''


lista = []
soma = 0

print('Digite 5 números:')

for n in range(1,5):
    numero = float(input('digite o %d° nota:' % (n)))
    soma += numero
    lista.append(numero)

media = soma/len(lista)

print(media)