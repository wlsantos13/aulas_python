'''
Imprima as chaves seguidas dos seus valores para dicionário criado no exercício anterior.

'''

meses = {'janeiro': 30
, 'fevereiro': 28
, 'março': 30
, 'abril': 31
, 'maio': 30
, 'junho': 31
, 'julho': 31
, 'agosto': 30
, 'setembro': 31
, 'outubro': 31
, 'novembro': 30
, 'dezembro': 31}

for chaves in meses:
    print(chaves,'-',meses[chaves] )