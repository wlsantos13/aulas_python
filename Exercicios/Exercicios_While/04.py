'''
Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

'''


numero = int(input('Digite um número: '))
soma = 0
contador = 1

print('A tabuada de',numero,'é:')

while contador <= 10:
    valor = numero * contador
    print(numero, 'x',contador,'=', valor)
    contador += 1
