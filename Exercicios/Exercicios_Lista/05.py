'''
Faça um programa que imprima o maior número de uma lista, sem usar a função max().
'''

lista = [14,20,37,42,2,0,22]

maior = lista[0]

for n in lista:
    if n > maior:
        maior = n

print('o maior da primeira lista é:', maior)
