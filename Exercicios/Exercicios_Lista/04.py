'''
Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.

'''


lista = [2, 3, 4, 5, 6, 7, 8.5, 10.0]
soma = 0

for item in lista:
    if item % 2 == 0:
        soma += 1


print('A quantidade de números pares da lista é:',soma)
    