'''
Enunciado
Crie uma lista de 10 números e imprima:

a. uma lista com os 4 primeiros números;

b. uma lista com os 5 últimos números;

c. uma lista contendo apenas os elementos das posições pares;

d. uma lista contendo apenas os elementos das posições ímpares;

e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);

f. uma lista inversa dos 5 primeiros números;

g. uma lista inversa dos 5 últimos números.

'''

lista = [1,2,3,4,5,6,7,8,9,10] 
lista4pri = []
lista5ult = []
listapares = []
listaimpares = []
listainversa = []
listainversa4pri = []
listainversa5ult = []

for n in range(4):
    lista4pri.append(lista[n])


for n in range(-5,0):
    lista5ult.append(lista[n])

for n in lista:
    if n % 2 == 0:
        listapares.append(n)

for n in lista:
    if n % 2 != 0:
        listaimpares.append(n)

print('Lista Original:',lista)
print('4 primeiros números:',lista4pri)
print('5 últimos números:',lista5ult)
print('Elementos das posições pares:',listapares)
print('Elementos das posições ímpares:',listaimpares)
lista.reverse()
print('Lista original inversa:', lista)
lista4pri.reverse()
print('Lista Inversa dos 4 primeiros números:',lista4pri)
lista5ult.reverse()
print('Lista Inversa 5 ultimos números:',lista5ult)

