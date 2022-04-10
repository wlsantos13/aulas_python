'''
3. Classe Retangulo: Crie uma classe que modele um retangulo:
    - Atributos: Tamanho do lado
    - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
    - Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. O
     programa também deve pedir as medidas de cada piso e rodapé

'''
# 10 cm --> 0,1 m

import math
class Retangulo:
    def __init__(self, lado_a, lado_b):

        self.a = lado_a
        self.b = lado_b

    def muda_valor(self,novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b

    def retorna_lado(self):

        print(f'O Retangulo possui dimensões {self.a} m x {self.b} m')

    def area(self):

        return self.a * self.b


piso_a = int(input("Digite um lado do piso: "))
piso_b = int(input("Digite o outro lado do piso: "))

piso = Retangulo(piso_a, piso_b)

az_a = float(input("Digite o lado do azulejo: "))
az_b = float(input("Digite o outro lado do azulejo: "))

azulejo = Retangulo(az_a, az_b)

area_piso = piso.area()
area_az = azulejo.area()

qntd_az = area_piso / area_az

if area_piso % area_az == 0:
    print(f'A quantidade exata de azulejos para preencher o piso é de {qntd_az}')

else:
    print(f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_az)}')
    



