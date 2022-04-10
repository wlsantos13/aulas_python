'''
Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.

Exemplo:

digite: 5

imprime: 1 2 3 4 5
'''


numero = int(input('Digite um número: '))
contador = 1


while contador <= numero:
    print(contador)
    contador += 1