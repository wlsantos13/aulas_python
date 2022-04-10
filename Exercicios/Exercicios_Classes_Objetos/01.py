'''
Crie uma classe Bola cujos atributos são cor e raio. Crie um método que imprime a cor da bola. Crie um método para calcular a área dessa bola. Crie um método para calcular o volume da bola. Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida.

Obs.:

Área da esfera = 4*3.14*r*r;

Volume da esfera = 4*3.14*r*r*r/3
'''

class Bola:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def area(self):
        return 4*3.14*(self.raio**2)

    def volume(self):
        return 4 * 3.14 * (self.raio**3)