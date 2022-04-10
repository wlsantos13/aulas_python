'''
Crie uma classe Retângulo cujos atributos são lado_a e lado_b. Crie um método para calcular a área desse retângulo.
Crie um objeto dessa classe e calcule a área e a imprima em seguida.
'''


class Retangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def Area(self):
        return self.lado_a * self.lado_b



ret1 = Retangulo(10, 25)

area = ret1.Area()

print(area)