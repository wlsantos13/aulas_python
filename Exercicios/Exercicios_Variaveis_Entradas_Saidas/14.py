'''
Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), 
uma posição inicial (em m) e um instante de tempo (em s) 
e imprima a posição de um projétil nesse instante de tempo.

Use a fórmula matemática:

y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final
, y(0) é a posição inicial, v(0) é a velocidade inicial e t é 
o instante de tempo.

'''

velInicial = float(input('Digite a velocidade inicial: '))
posInicial = float(input('Digite a posicao inicial: '))
InstInicial = float(input('Digite a Instante inicial: '))

resp = posInicial + velInicial*InstInicial + (-10*(InstInicial**2)/2)

print(resp)