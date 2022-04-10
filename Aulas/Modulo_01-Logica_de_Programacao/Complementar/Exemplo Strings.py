exemplo = 'aUlA dE PyThOn'

maiuscula = exemplo.upper() 
minuscula = exemplo.lower()
titulo = exemplo.title()
primeira_maiuscula = exemplo.capitalize()

print(exemplo)
print(maiuscula)
print(minuscula)
print(titulo)
print(primeira_maiuscula)

'''
sexo = input('Digite o seu sexo:').upper()
if sexo == 'M' or sexo == 'F' or sexo == 'OUTRO':
    print('Ok!')
else:
    print('Inválido!')
'''
# Replace: substitui uma substring por outra substring e retorna a nova string
exemplo2 = 'hoje tem aula de python'
substituido = exemplo2.replace('a', '4')
print(substituido)

exemplo3 = 'hoje tem aula de python, amanhã tem aula de ciência de dados'
substituido2 = exemplo3.replace('aula', 'conversa')
print(substituido2)
tamanho = len(exemplo3)
print(tamanho)

# Split - separa uma string em várias substrings e as armazena em uma lista
separado = exemplo3.split()
print(separado)
separado2 = exemplo3.split('a')
print(separado2)
'''
horario = input('Digite o horário atual: ')
lista_horario = horario.split(':')
hora = int(lista_horario[0])
minuto = int(lista_horario[1])
segundo = int(lista_horario[2])
print(hora, minuto, segundo)
'''
'''
nome = input('Digite o seu nome: ')
data_nasc = input('Digite o seu nascimento: ')
data_lista = data_nasc.split('/')
dia = int(data_lista[0])
mes = int(data_lista[1])
ano = int(data_lista[2])

contrato = 'Eu, {}, nascido em {:02d}/{:02d}/{:04d}, concordo em participar do curso.'

contrato_preenchido = contrato.format(nome, dia, mes, ano)
print(contrato_preenchido)
'''

preco_por_litro = 6.789
litros = 31.524
preco = preco_por_litro * litros

nota_fiscal = 'Preço: R$ {:.2f}'.format(preco)
print(nota_fiscal)


# f-strings: uma versão "resumida" do format
nome = input('Digite o seu nome: ')
data_nasc = input('Digite o seu nascimento: ')
data_lista = data_nasc.split('/')
dia = int(data_lista[0])
mes = int(data_lista[1])
ano = int(data_lista[2])

contrato = f'Eu, {nome}, nascido em {dia:02d}/{mes:02d}/{ano:04d}, concordo em participar do curso.'

print(contrato)

preco_por_litro = 6.789
litros = 31.524
preco = preco_por_litro * litros

nota_fiscal = f'Preço: R$ {preco:.2f}'
print(nota_fiscal)