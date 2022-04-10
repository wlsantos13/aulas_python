'''
Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, copiando letra por letra a palavra digitada, depois imprima a nova string.

'''

lista = list(input('Digite uma Palavra: '))
novapalavra = ''

for elemento in lista:
    novapalavra += elemento

print(novapalavra)