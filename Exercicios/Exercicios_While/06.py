'''
Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. 
A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está errada e pedir novamente uma resposta ao usuário.

Para a realização desse exercício, utilize alguma função da biblioteca random (e.g. randint()).
'''

import random
from typing import NoReturn

numero = int(input('Adivinhe o numero soteado de 1 a 10: '))

nrsoteado = random.randint(1,10)

while numero != nrsoteado:
    print('número errado')
    numero = int(input('Digite um novo número:'))


print('Voce acertou, o número sorteado foi', nrsoteado)

