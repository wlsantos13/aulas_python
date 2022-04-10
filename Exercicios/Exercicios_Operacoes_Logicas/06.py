'''
Vamos fazer um programa para verificar quem é o assassino de um crime. 
Para descobrir o assassino, a polícia faz um pequeno questionário com 5 
perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os 
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 
2 pontos são apenas suspeitos, necessitando outras investigações. 
Valores iguais ou abaixo de 1 são liberados.
'''

contador = 0
a = input('Mora perto da vítima? ')
if a == 'sim':
    contador += 1
b = input('Já trabalhou com a vítima? ')
if b == 'sim':
    contador += 1
c = input('Telefonou para a vítima? ')
if c == 'sim':
    contador += 1
d = input('Esteve no local do crime? ')
if d == 'sim':
    contador += 1
e = input('Devia para a vítima? ')
if e == 'sim':
    contador += 1


if contador <= 1:
    print('Liberados')
elif contador > 1 and contador < 3:
    print('Suspeitos')
elif contador >= 3 and contador < 5:
    print('Cumplices')
else:
    print('Assassinos')
