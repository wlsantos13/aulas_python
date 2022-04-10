import datetime

lista = [1, 2, 3, 4 ,5]

for i in range(len(lista)):
    print(i)

valor = 3
data = datetime.datetime.now()
data2 = data + datetime.timedelta(hours = valor)

print(data.strftime("%Y-%m-%d %H:%M:%S"))
print(data2.strftime("%Y-%m-%d %H:%M:%S"))
print(len(lista))


arquivo = {'Data Locação': '2022-02-18 11:53:24', 'Data entrega': '2022-02-18 14:53:24', 'CPF': '04787606638', 'Nome': 'wangles', 'Plano': 'Familiar', 'Tamanho Adulto': 3, 'Tamanho Infantil': 0, 'Periodo de Locaçao': '3 Horas', 'Valor a Pagar': 31.499999999999996}

teste = set((1,2,3,4,4))
teste.add(5)
teste.add(5)
print(arquivo)