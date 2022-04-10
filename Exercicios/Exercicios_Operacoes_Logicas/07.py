'''
Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:
a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:
A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças
'''


a = input('Sente dor no corpo? ')
b = input('Você tem febre? ')
c = input('Você tem tosse? ')
d = input('Está com congestão nasal? ')
e = input('Tem manchas pelo corpo? ')

if a == 'Sim' and b == 'Sim' and c == 'Nao' and d == 'Nao' and e == 'Sim':
    print('Dengue')
elif a == 'Sim'  and b == 'Sim' and c == 'Sim' and d == 'Sim' and e == 'Nao':
    print('Gripe')
elif a == 'Nao'  and b == 'Sim' and c == 'Sim' and d == 'Sim' and e == 'Nao':
    print('Gripe')
elif a == 'Sim' and b == 'Nao' and c == 'Nao' and d == 'Nao' and e == 'Nao':
    print('Sem doenças')
elif a == 'Nao' and b == 'Nao' and c == 'Nao' and d == 'Nao' and e == 'Nao':
    print('Sem doenças')
else:
    print('Doenca Desconhecida')