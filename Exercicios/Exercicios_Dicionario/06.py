'''
Enunciado
Como você armazenaria a seguinte tabela usando apenas dicionários? Tente imprimir o valor correspondente da linha Pedro x Coluna B.
        Coluna A	Coluna B
Maria	    1	    5
Pedro	    0.5	    3
João	    3.2 	1
'''

lista = [{
    'nome':'Maria',
    'colunaA': 1,
    'colunaB': 5
}, {
    'nome':'Pedro',
    'colunaA': 0.5,
    'colunaB': 3
}, {
    'nome':'Joao',
    'colunaA': 3.2,
    'colunaB': 1
}
]

for d in lista:
    if d['nome'] == 'Pedro':
        print(d['colunaB'])

