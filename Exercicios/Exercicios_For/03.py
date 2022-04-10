'''
Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de repetição while.

'''


numero = int(input('Digite um número: '))
soma = 0

for contador in range(numero+1):
    soma +=contador

print(soma)
