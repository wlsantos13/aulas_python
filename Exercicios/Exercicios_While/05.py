'''
Faça um programa, usando loops, que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0. 
Ao final imprima a soma de todos os números digitados.
'''


numero = int(input('Digite um número: '))
soma = 0

while numero != 0:
    soma += numero
    numero = int(input('Digite um número: '))

print('A soma dos numeros digitados é:', soma)
