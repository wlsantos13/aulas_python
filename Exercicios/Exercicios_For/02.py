'''
Peça ao usuário para digitar um número e imprima o fatorial de n.
'''

numero = int(input('Digite um número: '))
soma = 1

for contador in range(1, numero + 1):
    soma *= contador

print(soma)