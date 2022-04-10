'''
Super Desafio! - Repita o exercício anterior usando recursão, ou seja, uma função que chame ela mesma
, lembrando que 3! = 3*2!, que 2! = 2*1!, que 1! = 1*0! e que 0! = 1.
'''


def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x-1)


print(fatorial(5))