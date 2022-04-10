'''
Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.

Dica: Use o método próprio de listas .remove().
'''
lista = [14,20,37,42,2,0,22]

for item in range(1,4):
   maior = max(lista) 
   print('O %d° numero maior é: %d' % (item, maior))
   lista.remove(maior)