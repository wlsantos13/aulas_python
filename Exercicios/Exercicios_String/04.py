'''
Enunciado
Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string:

Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "
'''

lista = list(input('Digite uma Palavra: '))
novapalavra = ''

for elemento in lista:
       novapalavra += (' ' + elemento)

        
print(novapalavra)


