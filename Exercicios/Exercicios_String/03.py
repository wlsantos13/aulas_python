'''
Enunciado
Altere o exercício anterior para que a string copiada alterne entre letras maiúsculas e minúsculas.

Exemplo: se o usuário digitar "latex" o programa deve imprimir "LaTeX".
'''


lista = list(input('Digite uma Palavra: '))
novapalavra = ''

for i in range(len(lista)):
    if i == 0 or i%2 == 0:
        novapalavra += lista[i].upper()
    else:
        novapalavra += lista[i]
        
print(novapalavra)