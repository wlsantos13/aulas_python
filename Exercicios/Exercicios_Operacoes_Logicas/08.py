'''
Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.

Obs.: O aluno irá passar de ano se sua média for maior que 6.
'''



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1+n2+n3)/3

if media > 6:
    print('media',media , 'O aluno passou de ano')
else:
    print('media',media,': O aluno nao passou de ano')
