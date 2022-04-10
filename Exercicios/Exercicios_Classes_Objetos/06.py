'''
O módulo time possui a função time.sleep(x), que faz seu programa “dormir” por x segundos. 
Utilizando essa função, crie uma classe Contagem Regressiva e faça um programa que cronometre o tempo.

'''

import time
import os

class Cronometro:

    def __init__(self,tempo):
        self.tempo = tempo

    def contagem(self):
        contador = self.tempo
        for t in range(self.tempo):
            print(contador)
            time.sleep(1)
            os.system('clear')
            contador -= 1
        print('Fim')
        

crono1 = Cronometro(10)

crono1.contagem()