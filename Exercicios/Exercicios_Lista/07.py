'''
Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual 
a soma dos elementos da lista 1 com os da lista 2, na mesma posição.

Exemplo:

Dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]

'''

lista1 = [1, 4, 5] 
lista2 = [2, 2, 3]
listafinal = []

for item in range(len(lista1)):
    valor = lista1[item] + lista2[item]
    listafinal.append(valor)

print(lista1)
print(lista2)
print(listafinal)

