# Exemplo 1: dicionário dentro de lista
usuarios = [
    {'nome':'Rafael', 'email':'rafael@letscode.com.br', 'cpf':'12345678912'},
    {'nome':'Matheus', 'email':'matheus@letscode.com.br', 'cpf':'98765432198'}
]

print(usuarios[1]['email'])

# Exemplo 2: dicionário dentro de dicionário
usuarios = {
    '12345678912':{'nome':'Rafael', 'email':'rafael@letscode.com.br'},
    '98765432198':{'nome':'Matheus', 'email':'matheus@letscode.com.br'}
}
print(usuarios['12345678912']['email'])
'''
cpf = input('Digite o cpf: ')
if cpf in usuarios:
    print('Usuário encontrado:', usuarios[cpf])
else:
    print('Usuário não encontrado!')
'''

email = input('Digite o seu e-mail: ')
encontrou = False
for cpf in usuarios:
    if usuarios[cpf]['email'] == email:
        encontrou = True
        print('E-mail duplicado!')

if encontrou == False:
    print('E-mail ok!')