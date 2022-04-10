dicio1 = {'nome':'wangles', 'idade':41, 'email':'wangles.santos@gmail.com'}
dicio2 = {'nome':'luan', 'idade':18, 'email':'teste@gmail.com'}
lista = []

lista.append(dicio1)
lista.append(dicio2)

print(lista)

for i in range(len(lista)):
    if lista[i]['nome'] == 'wangles':
        lista[i]['idade'] = 40


print(lista)


