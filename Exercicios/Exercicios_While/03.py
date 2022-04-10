'''
Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de repetição while.

'''


numero = int(input('Digite um número: '))
soma = 0
contador = 1

while contador <= numero:
    soma +=contador
    contador += 1

print(soma)
