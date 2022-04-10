'''
Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.

OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.
'''


lista = []

print('Digite 5 números:')

for n in range(1,6):
    numero = float(input('digite o %d° número:' % (n)))
    lista.append(numero)

print('Os números digitados foram:')
print(lista)