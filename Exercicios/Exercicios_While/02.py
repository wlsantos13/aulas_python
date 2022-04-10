'''
Peça ao usuário para digitar um número e imprima o fatorial de n.
'''

numero = int(input('Digite um número: '))
contador = 1
soma = 1

while contador <= numero:
    soma *= contador
    contador += 1

print(soma)