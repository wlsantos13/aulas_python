'''
Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

'''


numero = int(input('Digite um número: '))
soma = 0

print('A tabuada de',numero,'é:')

for contador in range(1,11):
    valor = numero * contador
    print(numero, 'x',contador,'=', valor)
