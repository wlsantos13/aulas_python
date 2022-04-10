'''
Crie uma classe Data cujos atributos são dia, mês e ano. Implemente métodos _ repr _ e para comparação: 
igualdade (==) e desigualdades (!=, <=, >=, < e >).

'''

class Calendario:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __repr__(self):
        return f'{str(self.dia)}/{self.mes}/{self.ano}'

    def conversao(datastring):
        lista = datastring.split('/')
        return lista


print(Calendario.conversao('01/12/2020'))
data = Calendario.conversao('01/12/2020')
dia = int(data[0])
print(dia)
mes = int(data[1])
print(mes)
ano = int(data[2])
print(ano)

DataFinal =  Calendario(dia, mes, ano)
print(DataFinal)