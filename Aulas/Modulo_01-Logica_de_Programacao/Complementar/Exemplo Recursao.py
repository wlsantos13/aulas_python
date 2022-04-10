'''
2**4 = 2*2*2*2*1
       2*(2*2*2*1)
       2*(2**3)

2**3 = 2*2*2*1
       2*(2*2)
       2*(2**2)

2**2 = 2*(2*1)
       2*(2**1)

2**1 = 2*1
       2*(1)
       2*(2**0)

2**0 = 1 <------ caso base!


2**4 = 2*(2**3)

2**3 = 2*(2**2)

2**2 = 2*(2**1)

2**1 = 2*(2**0)
2**1 = 2*1 = 2
2**2 = 2*2 = 4
2**3 = 2*(2**2) = 2*4 = 8
2**4 = 2*(2**3) = 2*8 = 16


F(n) =     1, se n = 0            -------> caso base
           2*(F(n-1)), se n > 0   -------> caso recursivo, caso geral
'''

def potencia_de_2_iterativo(expoente):
    produto = 1
    for contador in range(expoente):
        produto = produto * 2
    return produto

def potencia_de_2_recursivo(expoente):
    if expoente == 0:
        return 1
    else:
        return 2*potencia_de_2_recursivo(expoente-1)

'''
FATORIAL
5! = 5*4*3*2*1
     5*(4*3*2*1)
     5*4!

Você pode seguir decompondo 4!, 3!, 2!...
'''

'''
Sequência de Fibonacci

F(0) = 0
F(1) = 1

F(n) = F(n-1) + F(n-2)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
'''
