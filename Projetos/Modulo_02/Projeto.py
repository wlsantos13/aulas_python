import datetime
import os


class Cliente:
    def __init__(self, cpf, nome, email):
        self.cpf = cpf
        self.nome = nome
        self.email = email
    
class Bicicleta:
    tamanhos = ['Adulto', 'Infantil']

    def __init__(self, tamanho, quantidade):
        self.modelo = 'Urbana'
        self.tamanho = tamanho
        self.quantidade = quantidade


class Locacao:

    planos = ['Familiar', 'Individual']
    periodos = ['Horas', 'Dias', 'Semanas']

    def __init__(self, plano, periodo_Locacao, periodo_qtd, clie, qtd_adulto, qtd_infantil, valor):
        self.dataloc = datetime.datetime.now()
        self.dataentrega = None
        self.plano = plano
        self.periodo_Locacao = periodo_Locacao
        self.periodo_qtd = periodo_qtd
        self.cpf = clie.cpf
        self.nome = clie.nome
        self.email = clie.email
        self.qtd_adulto = qtd_adulto
        self.qtd_infantil = qtd_infantil
        self.valor = valor

    def dtentrega(self):
        data = None
        if self.periodo_Locacao == 'Horas':
            data = self.dataloc + datetime.timedelta(hours = self.periodo_qtd)
        elif self.periodo_Locacao == 'Dias':
            data = self.dataloc + datetime.timedelta(days = self.periodo_qtd)
        elif self.periodo_Locacao == 'Semanas':
            data = self.dataloc + datetime.timedelta(weeks = self.periodo_qtd)
        return data

    def __repr__(self):
        return f'############ TICKET #############\nData Locação: {self.dataloc.strftime("%Y-%m-%d %H:%M:%S")}\nData entrega: {self.dtentrega().strftime("%Y-%m-%d %H:%M:%S")}\nCPF: {self.cpf}\nNome: {self.nome}\nPlano: {self.plano}\nTamanho Adulto: {self.qtd_adulto}\nTamanho Infantil: {self.qtd_infantil}\nPeriodo de Locaçao: {self.periodo_qtd} {self.periodo_Locacao}\n\nValor a Pagar: R${self.valor}\n'


class Loja:

    def __init__(self):
        self.bicicletas = []
        self.clientes = []
        self.locacoes = []
        

    def cadastro_bicicletas(self, bicicleta):
        tamanhos = set(())
        if len(self.bicicletas) == 0:
            self.bicicletas.append({'Modelo':bicicleta.modelo, 'Tamanho':bicicleta.tamanho, 'Quantidade':bicicleta.quantidade})
        else:
            for i in range(len(self.bicicletas)):
                tamanhos.add(self.bicicletas[i]['Tamanho']) 
            if bicicleta.tamanho not in tamanhos:
                self.bicicletas.append({'Modelo':bicicleta.modelo, 'Tamanho':bicicleta.tamanho, 'Quantidade':bicicleta.quantidade})
            else: 
                for i in range(len(self.bicicletas)):
                    if self.bicicletas[i]['Tamanho'] == bicicleta.tamanho:
                        self.bicicletas[i]['Quantidade'] = int(self.bicicletas[i]['Quantidade']) + int(bicicleta.quantidade)
            
                    
    def bicicletas_cadastradas(self):
        if len(self.bicicletas) == 0:
            print('\nNão existem bicicletas cadastradas\n')
        else:
            print('------------------------------')
            print(f"{'MODELO':^10s}|{'TAMANHO':^10s}|{'QTD':^10s}")
            for bici in self.bicicletas:
                print(f"{bici['Modelo']:^10s}|{bici['Tamanho']:^10s}|{str(bici['Quantidade']):^10s}")
            print('------------------------------')

    def cadastro_clientes(self, Cliente):
        # self.clientes.append([Cliente.cpf, Cliente.nome, Cliente.email])
        if len(self.clientes) != 0:
            for i in range(len(self.clientes)):
                if self.clientes[i]['CPF'] == Cliente.cpf:
                    self.clientes[i]['Nome'] == Cliente.nome
                    self.clientes[i]['Email'] == Cliente.email
        else:    
            self.clientes.append({'CPF': Cliente.cpf, 'Nome':Cliente.nome, 'Email': Cliente.email})

    def clientes_cadastrados(self):
        if len(self.clientes) == 0:
            print('\nNão existem clientes cadastrados\n')
        else:
            print('----------------------------------------------------')
            print(f"{'CPF':^15s}|{'NOME':^15s}|{'EMAIL':^30s}")
            for cliente in self.clientes:
                print(f"{cliente['CPF']:^15s}|{cliente['Nome']:^15s}|{cliente['Email']:^30s}")
            print('----------------------------------------------------')

    def criar_locacao(self, loc):
        self.locacoes.append({'Data Locação': loc.dataloc.strftime("%Y-%m-%d %H:%M:%S"),'Data entrega': loc.dtentrega().strftime("%Y-%m-%d %H:%M:%S"), 'CPF': loc.cpf, 'Nome': loc.nome, 'Plano': loc.plano, 'Tamanho Adulto': loc.qtd_adulto,'Tamanho Infantil': loc.qtd_infantil, 'Periodo de Locaçao': str(loc.periodo_qtd) + ' ' + loc.periodo_Locacao, 'Valor a Pagar': loc.valor})
    
    def exibir_locacoes(self):
        if len(self.locacoes) == 0:
            print('\nNão existem locações efetuadas\n')
        else:
            for loc in self.locacoes:
                print()
                print(loc)
                print()

    def confirmar_estoque_adulto(self):
        qtd_bicicletas = 0
        qtd_locadas = 0
        for bicicleta in self.bicicletas:
            if bicicleta['Tamanho'] == 'Adulto':
                qtd_bicicletas += int(bicicleta['Quantidade'])

        for loc in self.locacoes:
            qtd_locadas += int(loc['Tamanho Adulto'])

        qtddisponivel = qtd_bicicletas - qtd_locadas
        return qtddisponivel

    def confirmar_estoque_Infantil(self):
        qtd_bicicletas = 0
        qtd_locadas = 0
        for bicicleta in self.bicicletas:
            if bicicleta['Tamanho'] == 'Infantil':
                qtd_bicicletas += bicicleta['Quantidade']
        for loc in self.locacoes:
            qtd_locadas += loc['Tamanho Infantil']
        qtddisponivel = qtd_bicicletas - qtd_locadas
        return qtddisponivel

    def valor_a_pagar(self, plano, periodo, periodoqtd, qtdbici):
        valor = 0
        if plano == 'Individual':
            if periodo == 'Horas':
                valor = 5 * qtdbici * periodoqtd
            elif periodo == 'Dias':
                valor = 25 * qtdbici * periodoqtd
            else:
                valor = 100 * qtdbici * periodoqtd
        else:
            if periodo == 'Horas':
                if qtdbici < 3:
                    valor = 5 * qtdbici * periodoqtd
                else:
                    valor = 5 * qtdbici * periodoqtd * 0.7
            elif periodo == 'Dias':
                if qtdbici < 3:
                    valor = 25 * qtdbici * periodoqtd
                else:
                    valor = 25 * qtdbici * periodoqtd * 0.7
            else:
                if qtdbici < 3:
                    valor = 100 * qtdbici * periodoqtd
                else:
                    valor = 100 * qtdbici * periodoqtd * 0.7
        return round(valor,2)

    def bicicletas_disponiveis(self):
        bici_adulto = self.confirmar_estoque_adulto()
        bici_infantil = self.confirmar_estoque_Infantil()
        if bici_adulto == 0 and bici_infantil == 0:
            print('\nNão temos Bicicletas Disponiveis para Locação\n')
        else:
            print('\nBicicletas Disponíveis:\n')
            print(f'- {bici_adulto} bicicletas tamanho Adulto')
            print(f'- {bici_infantil} bicicletas tamanho Infantil\n')

    def menu(self):
        
        opcao = ''
        while opcao != '0':
            print('######################### MENU #########################')
            print('1 - Cadastro de Cliente')
            print('2 - Cadastro de Bicicleta')
            print('3 - Listar Clientes Cadastrados')
            print('4 - Listar Bicicletas Cadastradas')
            print('5 - Locar Bicicletas')
            print('6 - Listar Locações efetuadas')
            print('7 - Listar Bicicletas Disponiveis')
            print('0 - Sair do Programa\n')
            opcao = input('Selecione a opção desejada: ')
            if opcao == '1':
                os.system('clear')
                print('----Cadastro de Clientes-----:')
                cpf = input('Digite o CPF do Cliente: ')
                nome = input('Digite o nome do Cliente: ')
                email = input('Digite o email do Cliente: ')
                clie = Cliente(cpf, nome, email)
                self.cadastro_clientes(clie)
                print()
                print('------ Cliente Cadastrado com Sucesso ------\n')
                input('Pressione qualquer tecla para continuar.....')
                os.system('clear')
            elif opcao == '2':
                os.system('clear')
                print('----Cadastro de Bicicletas-----:')
                tamanho = ''
                while tamanho not in Bicicleta.tamanhos:
                    print('\nTamanhos disponíveis:')
                    for tamanho in Bicicleta.tamanhos:
                        print('-', tamanho)
                    tamanho = input('Digite o tamanho da bicicleta: ')
                    if tamanho not in Bicicleta.tamanhos:
                        print('\n## Erro ## - Tamanho informado Inválido\n')
                quantidade = int(input('\nDigite a quantidade de Bicicletas: '))
                bici = Bicicleta(tamanho, quantidade)
                self.cadastro_bicicletas(bici)
                print()
                print('------ Bicicleta Cadastrada com Sucesso ------\n')
                input('Pressione qualquer tecla para continuar.....')
                os.system('clear')
            elif opcao =='3':
                os.system('clear')
                self.clientes_cadastrados()
                input('Pressione qualquer tecla para continuar.....')
                os.system('clear')
            elif opcao =='4':
                os.system('clear')
                self.bicicletas_cadastradas()
                input('Pressione qualquer tecla para continuar.....')
                os.system('clear')
            elif opcao == '5':
                os.system('clear')
                plano = ''
                qtd_adulto = 0
                qtd_infantil = 0
                tamanho = ''
                periodo = ''
                bici_adulto = self.confirmar_estoque_adulto()
                bici_infantil = self.confirmar_estoque_Infantil()
                bici_total = bici_adulto + bici_infantil
                valor_Pagamento = 0
                if len(self.clientes) == 0:
                    print('\nNão existem clientes cadastrados no sistema, Não é possivel iniciar a Locação\n')
                    input('Pressione qualquer tecla para continuar.....')
                    os.system('clear')
                    self.menu()
                elif bici_adulto == 0 and bici_infantil == 0:
                    print('\nNão temos Bicicletas Disponiveis para Locação\n')
                    input('Pressione qualquer tecla para continuar.....')
                    os.system('clear')
                    self.menu()
                else: 
                    self.bicicletas_disponiveis()
                    listacpf = []
                    cpf = ''
                    op = '1'
                    for cliente in self.clientes:
                        listacpf.append(cliente['CPF'])
                    while cpf not in listacpf and op == '1':
                        cpf = input('\nDigite o CPF do Cliente: ')
                        if cpf not in listacpf:
                            os.system('clear')
                            print('\nCliente não Cadastrado\n')
                            op = input('Digite 1 para novo CPF ou 2 para voltar ao Menu:')
                    if op == '2':
                        os.system('clear')
                        self.menu()
                    else:
                        while plano not in Locacao.planos:                   
                            print('\nPlanos disponiveis: ')
                            if bici_total < 2:
                                print('- Individual')
                                plano = 'Individual'
                            else:
                                for plano in Locacao.planos:
                                    print('-', plano)
                                plano = input('\nDigite o plano: ')
                            if plano not in Locacao.planos:
                                print('Plano Invalido')
                        if plano == 'Individual':
                            while tamanho not in Bicicleta.tamanhos:
                                if bici_adulto == 0 and bici_infantil > 0:
                                    tamanho = 'Infantil'
                                elif bici_adulto > 0 and bici_infantil == 0:
                                    tamanho = 'Adulto'
                                else:
                                    print('\nTamanhos disponiveis: ')
                                    for tamanho in Bicicleta.tamanhos:
                                        print('-', tamanho)
                                    tamanho = input('Digite um tamanho: ')
                                if tamanho not in Bicicleta.tamanhos:
                                        print('Tamanho digitado Invalido')
                                if tamanho == 'Infantil':
                                    qtd_infantil = 1
                                else:
                                    qtd_adulto = 1
                            while periodo not in Locacao.periodos:
                                print('Escolha um periodo de locação: ')
                                for periodo in Locacao.periodos:
                                    print('-', periodo)
                                periodo = input('Digite o Periodo: ')
                                if periodo not in Locacao.periodos:
                                    print('Periodo Invalido')
                            periodo_qtd = int(input(f'Digite a quantidade de {periodo}: '))
                        elif plano == 'Familiar':
                            print('\nTamanho disponiveis: ')
                            if bici_adulto == 0 and bici_infantil > 0:
                                tamanho = 'Infantil'
                                qtd_infantil = int(input('Quantas Bicicletas Infantis ira locar? '))
                            elif bici_infantil == 0 and bici_adulto > 0:
                                tamanho = 'Adulto'
                                qtd_adulto = int(input('Quantas Bicicletas Tamanho Adulto ira Locar? '))
                            else:
                                for tamanho in Bicicleta.tamanhos:
                                    print('-', tamanho)
                                qtd_adulto = int(input('Quantas Bicicletas Tamanho Adulto ira Locar? '))
                                while qtd_adulto > self.confirmar_estoque_adulto():
                                    print('## ERRO ## - Quantidade informada acima do estoque disponível')
                                    qtd_adulto = int(input('Quantas Bicicletas Tamanho Adulto ira Locar? '))
                                qtd_infantil = int(input('Quantas Bicicletas Tamanho Infantil deseja Locar? '))
                                while qtd_infantil > self.confirmar_estoque_Infantil():
                                    print('## ERRO ## - Quantidade informada acima do estoque disponível')
                                    qtd_infantil = int(input('Quantas Bicicletas Tamanho Infantil deseja Locar? '))
                            while periodo not in Locacao.periodos:
                                print('Escolha um periodo de locação: ')
                                for periodo in Locacao.periodos:
                                    print('-', periodo)
                                periodo = input('Digite o Periodo: ')
                                if periodo not in Locacao.periodos:
                                    print('Periodo Invalido')
                            periodo_qtd = int(input(f'Digite a quantidade de {periodo}: '))
                        qtd_Total = qtd_adulto + qtd_infantil
                        valor_Pagamento = self.valor_a_pagar(plano, periodo, periodo_qtd, qtd_Total)
                    loc = Locacao(plano, periodo, periodo_qtd, clie, qtd_adulto, qtd_infantil, valor_Pagamento)
                    loc.dtentrega()
                    os.system('clear')
                    print('\nLocação efetuada com sucesso\n')
                    print(loc)
                    self.criar_locacao(loc)
                    input('Pressione qualquer tecla para continuar.....')
                    os.system('clear')
            elif opcao == '6':
                os.system('clear')
                self.exibir_locacoes()
                input('Pressione qualquer tecla para continuar.....')
                os.system('clear')
            elif opcao == '7':
                os.system('clear')
                self.bicicletas_disponiveis()
                input('Pressione qualquer tecla para continuar.....')
                os.system('clear')



        print('\nPrograma Finalizado\n')


        

loja1 = Loja()
print('--------------------------------------------------------')
print('Seja Bem vindo ao nosso Sistema de Locação de Bicicletas')
print('-------Trabalhamos somente com bicicletas Urbanas-------')
print('---------------Bicicletas de Cores Unicas---------------')
loja1.menu()

