'''
Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...

Dica: Assim como no exercício anterior use três variáveis: um contador; uma variável para a soma;
e uma variável para os termos. Lembre-se de que 4! = 4*3*2*1 que também é igual a 4*3!.

'''


soma = 0
contador = 1
while contador <= 50:
    contador2 = 1
    fator = 1
    while contador2 <= contador:
        fator *= contador2
        contador2 += 1
    # print(1,'/',fator)
    soma += 1/fator
    contador += 1


print(soma)

