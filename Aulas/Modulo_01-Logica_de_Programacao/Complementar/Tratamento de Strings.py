# Tratamento de strings
exemplo = 'olá mundo'

print(exemplo[0])
print(exemplo[1])
print(exemplo[2])
print(exemplo[3])
print(exemplo[4])

print('--------------')

for letra in exemplo:
    print(letra)

#exemplo[0] = 'O' # isso dá erro: string é imutável
#print(exemplo)

#exemplo.append('!') # também não funciona: string é imutável!
#print(exemplo)

exemplo_lista = list(exemplo)
print(exemplo_lista)

exemplo_lista[0] = 'O'
exemplo_lista.append('!')
print(exemplo_lista)

# isso não funciona como esperamos...
exemplo_modificado = str(exemplo_lista)
print(exemplo_modificado)
# ele converte a representação da lista (com colchetes e tudo) para str!
for letra in exemplo_modificado:
    print(letra)

exemplo_modificado = ''.join(exemplo_lista)
print(exemplo_modificado)

'''
string = 'ABC'
lista = ['x', 'y', 'z']
resultado = string.join(lista)
print(resultado)
'''

# operações "aritméticas" com strings
# + soma => concatenação de strings
string1 = 'Olá'
string2 = 'Mundo'
soma = string1 + string2
print(soma)

# * multiplicação (entre int e str): repete a string "int" vezes
multiplicacao = soma * 3
print(multiplicacao)

# revisitando a nossa lista modificada...
print(exemplo_lista)
exemplo_modificado_soma = ''
for elemento in exemplo_lista:
    exemplo_modificado_soma = exemplo_modificado_soma + elemento

print(exemplo_modificado_soma)


exemplo_quebra = 'Olá\nmundo'
print(exemplo_quebra)

exemplo_tabulacao = 'Aluno1:\t10.0\t9.0\t9.5\t9.5'
print(exemplo_tabulacao)

exemplo_final = 'O símbolo \\n quebra linhas.' # o símbolo \\ indica que '\' deve ser escrito literalmente!
print(exemplo_final)
