
#Soma de inteiros de uma lista

# lista = [1,2,3,4,5,[3,2,[5,5]]]


lista = [[0, 3, 5, 1], 2, 3, [2, [5, 6, 7, [1, 4, 6]], 3], 2, [3, 5, 10, [6]]]


print(type(lista) == list)

def somalista(lista):
    soma = 0
    for i in lista:
        if type(i) == int:
            soma += i
        else:
            soma += somalista(i)
    return soma

print(somalista(lista))
