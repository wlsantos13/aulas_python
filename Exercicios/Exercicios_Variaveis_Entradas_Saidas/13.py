'''
Faça um programa que peça um valor monetário e diminua-o em 15%. 
Seu programa deve imprimir a mensagem “O novo valor é [valor]”.
'''

valor = float(input('Digite um valor: '))

newvalor = round((valor * 0.85), 2)

print('O novo valor é', newvalor)