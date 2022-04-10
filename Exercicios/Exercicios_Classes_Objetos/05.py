'''
Crie uma classe ControleRemoto cujo atributo é televisão (isso é, recebe um objeto da classe do exercício 4). 
Crie métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo 
canal à lista de canais (somente se esse canal não estiver nessa lista).

'''


class Televisor:

    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.volume = 20
        self.canal_atual = None
        self.canais = []



class ControleRemoto:
    def __init__(self, Televisor):
        self.Televisor = Televisor

    def aumentarVolume(self):
        self.Televisor.volume += 1

    def dimunuirVolume(self):
        self.Televisor.volume -= 1

    def sintonizarCanais(self, lista):
        for c in lista:
            self.Televisor.canais.append(c)

    

tv1 = Televisor('Samsung', 'xptto')

print(tv1.volume)

ControleRemoto(tv1).aumentarVolume()

print(tv1.volume)

ControleRemoto(tv1).dimunuirVolume()

print(tv1.volume)

print(tv1.canais)

ControleRemoto(tv1).sintonizarCanais(['sbt','globo','record'])

print(tv1.canais)