'''
Enunciado
Crie uma classe Televisor cujos atributos são:

a. fabricante;

b. modelo;

c. canal atual;

d. lista de canais; e

e. volume.

Faça métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.

Obs.: O volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.
'''



class Televisor:

    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = None
        self.lista_canais = []
        self.volume = 20

    def aumentar_volume(self, valor):
        if (self.volume + valor) <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuir_volume(self, valor):
        if (self.volume - valor) >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def sintonizar_canal(self, canal):
        if canal not in self.lista_canais:
            self.lista_canais.append(canal)
        else:
            print('Canal já sintonizado')

    def mudar_canal(self, canal):
        if canal in self.lista_canais:
            self.canal_atual = canal
        else:
            print( 'canal invalido')