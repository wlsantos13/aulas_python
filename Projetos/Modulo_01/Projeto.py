import json
import os.path
import sys

def obter_dados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    lista = []

    for d in dados:
        if d['categoria'] not in lista:
            lista.append(d['categoria'])
    lista.sort()
    print(lista)

def listar_por_categoria(dados, categoria):

    lista = []

    for d in dados:
        if d['categoria'] == categoria:
            lista.append(d)

    
    print(lista)


def produto_mais_caro(dados, categoria):
    
    lista = {}
    maiorpreco = 0.0
    idproduto = ''
    
    for d in dados:
        if d['categoria'] == categoria:
            if float(d['preco']) > maiorpreco:
                maiorpreco = float(d['preco'])
                idproduto = d['id']
 
    for d in dados:
        if d['id'] == idproduto:
            lista.update(d)
            

    print(lista)
   
def produto_mais_barato(dados, categoria):
    lista = {}   
    menorpreco = 0.0
    idproduto = ''

    for d in dados:
        if d['categoria'] == categoria:
            if float(d['preco']) < menorpreco or menorpreco == 0:
                menorpreco = float(d['preco'])
                idproduto = d['id']

    for d in dados:
        if d['id'] == idproduto:
            lista.update(d)

    print(lista)

def top_10_caros(dados):
    precos = []
    lista = []

    for d in dados:
        precos.append(float(d['preco']))

    precos.sort(reverse=True)

    for i in range(10):
        for d in dados:
            if float(d['preco']) == precos[i]:
                lista.append(d)

    print(lista)

def top_10_baratos(dados):
    precos = []
    lista = []

    for d in dados:
        precos.append(float(d['preco']))

    precos.sort()

    for i in range(10):
        for d in dados:
            if float(d['preco']) == precos[i]:
                lista.append(d)

    print(lista)

def menu(dados):

    opcao = ''

    while opcao != '0':
        print('Escolha uma opção valida:')
        print('1. Listar categorias')
        print('2. Listar produtos de uma categoria')
        print('3. Produto mais caro por categoria')
        print('4. Produto mais barato por categoria')
        print('5. Top 10 produtos mais caros')
        print('6. Top 10 produtos mais baratos')
        print('0. Sair')
        opcao = input('Escolha uma opção valida: ')
        if opcao != '0':
            if opcao == '1':
                print()
                listar_categorias(dados)
                print()
            elif opcao == '2':
                categoria = input('Digite a categoria que deseja: ')
                print()
                listar_por_categoria(dados, categoria)
                print()
            elif opcao == '3':
                categoria = input('Digite a categoria que deseja: ')
                print()
                produto_mais_caro(dados, categoria)
                print()
            elif opcao == '4':
                categoria = input('Digite a categoria que deseja: ')
                print()
                produto_mais_barato(dados, categoria)
                print()
            elif opcao == '5':
                print()
                top_10_caros(dados)
                print()
            elif opcao == '6':
                print()
                top_10_baratos(dados)
                print()
            else:
                print()   
                print('########### Erro - Digite uma opção valida #############')
                print()

    print('Fim')


# Programa Principal - não modificar!
d = obter_dados()
menu(d)
