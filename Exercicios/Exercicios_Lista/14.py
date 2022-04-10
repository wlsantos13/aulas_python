'''
Super Desafio - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. 
Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF pelos números de 10 a 2 
e somar todas as respostas. 
O resultado deve ser multiplicado por 10 e dividido por 11.
O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito). 
Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 
e repetir o procedimento anterior para verificar o segundo dígito verificador.

Exemplo:

Se o CPF for 286.255.878-87 o programa deve fazer primeiro:

x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)

Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). 
Se sim, o programa deve calcular:

x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)

e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).
'''

cpf = list(input('Digite o cpf: (somente números): '))
ultimonumero = int(cpf[len(cpf)-1])
penultimonumero = int(cpf[len(cpf) - 2])
# print(cpf)
# print(ultimonumero)
# print(penultimonumero)
cpf.reverse()
soma = 0
i = 2
for n in range(2,11):
    x = n * int(cpf[i])
    # print(n, cpf[i],x)
    soma += x
    i += 1

teste1 = soma*10%11
# print(soma)
# print(teste1)

soma2 = 0
i2 = 1
if teste1 == 10:
    teste1 = 0
if teste1 == penultimonumero:
    for n in range(2,12):
        x2 = n * int(cpf[i2])
        # print(n, cpf[i2],x2)
        soma2 += x2
        i2 += 1
    teste2 = soma2*10%11
    # print(soma2)
    # print(teste2)
    if teste2 == ultimonumero:
        print('CPF VALIDO')
    else:
        print('CPF INVALIDO')
else:
    print('CPF INVALIDO')





