'''
Enunciado
Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números digitados pelo usuário 
(sem converter os números para int ou float).

Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir a lista ['1','5','2','3','6']
'''

lista = []

print('Digite 5 números:')

for n in range(1,6):
    numero = input('digite o %d° número:' % (n))
    lista.append(numero)

print('Os números digitados foram:')
print(lista)