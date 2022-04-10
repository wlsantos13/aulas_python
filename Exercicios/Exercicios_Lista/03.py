'''
Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1.

Exemplo: se o usuário digitar 5, o programa deve imprimir [0, 1, 2, 3, 4]
'''

numero = int(input('Digite um número: ')) 

for n in range(numero):
    print(n)

