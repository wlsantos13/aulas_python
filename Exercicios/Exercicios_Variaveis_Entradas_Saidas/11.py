'''
Faça um programa que peça o peso e altura de 
uma pessoa e calcule seu IMC (Índice de Massa Corporal).

Obs: IMC = Peso/Altura**2
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = (peso/altura) ** 2

print(IMC)
