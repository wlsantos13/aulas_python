# exercício 20 - Black Jack
# Helldânio Barros - 2022 - Let's Code - Magalu
import random

# GERAR BARALHO
def baralho_cria():
    '''
    O.Ouro
    C.Copas
    E.Espada
    P.Paus
    '''
    for x in range(4):  #definindo os naipes
        for y in range(13): #definindo as cartas para cada naipe
            if x == 0:
                baralho.append(['O'+str(y+1),y+1])
            elif x == 1:
                baralho.append(['C'+str(y+1),y+1])
            elif x == 2:
                baralho.append(['E'+str(y+1),y+1])
            elif x == 3:
                baralho.append(['P'+str(y+1),y+1])

def escolher_carta():
    # Se o baralho tiver mais de uma carta, a função escolherá aleatoriamente uma delas, caso contrário retorna
    # a carta que sobrou. Após a escolha, a carta é retirada do baralho.
    if len(baralho) > 1:
        numero = random.randint(0,len(baralho)-1)  # o termo da lista inicia em 0 e termina em 51, por isso "len(baralho)-1"
    else:
        if len(baralho) == 1:
            numero = 0
        else:
            print('O baralho não possui mais cartas disponíveis!')
            for w in range(len(jogadores)):
                jogadores[w][2] = False
            return('FIM')
    carta = baralho[numero]
    baralho.remove(carta)
    return(carta)

def verifica_ganhador(x_jogadores):
    x_jogadores = sorted(x_jogadores, key=lambda x: x[1], reverse=True)  #ordenando a lista em ordem decrescente de pontos
    print('-----------------------------')
    print('    PLACAR FINAL DO JOGO')
    print('-----------------------------')
    for x in range(len(x_jogadores)):
        print(f'{x_jogadores[x][0]} - Pontos: {x_jogadores[x][1]}')
        if x_jogadores[x][0] == 'Computador':
            print('     Cartas escolhidas pelo Computador:')
            print('     ----------------------------------')
            for w in range(len(jogadores_carta)):
                if jogadores_carta[w][0] == 'Computador':
                    identifica_carta(jogadores_carta[w][1],1)
        print('-----------------------------')
    print()
    for w in range(len(x_jogadores)):
        if x_jogadores[w][1] <= 21:   #o primeiro jogador encontrado com 21 ou imediatamente menor é declarado vencedor 
            print('O ganhador é: ',x_jogadores[w][0],'com',x_jogadores[w][1],'pontos')
            break  

def identifica_carta(carta,modo=0):
    nome_carta = ''
    tipo_carta = ''
    numero_carta = int(carta[1:])
    if numero_carta == 1: nome_carta = 'ÁS'
    if numero_carta == 2: nome_carta = 'Dois'
    if numero_carta == 3: nome_carta = 'Três'
    if numero_carta == 4: nome_carta = 'Quatro'
    if numero_carta == 5: nome_carta = 'Cinco'
    if numero_carta == 6: nome_carta = 'Seis'
    if numero_carta == 7: nome_carta = 'Sete'
    if numero_carta == 8: nome_carta = 'Oito'
    if numero_carta == 9: nome_carta = 'Nove'
    if numero_carta == 10: nome_carta = 'Dez'
    if numero_carta == 11: nome_carta = 'Valete'
    if numero_carta == 12: nome_carta = 'Dama'
    if numero_carta == 13: nome_carta = 'Reis'
    if carta[0] == 'O': tipo_carta = 'Ouro'
    elif carta[0] == 'C': tipo_carta = 'Copas'
    elif carta[0] == 'E': tipo_carta = 'Espadas'
    elif carta[0] == 'P': tipo_carta = 'Paus'
    if modo == 0:
        print('A carta é:',nome_carta,'de',tipo_carta)
    else:
        print('     ',nome_carta,'de',tipo_carta)

def computador_joga():  # ESTA FUNCAO FARÁ COM QUE O COMPUTADOR ESCOLHA UMA CARTA DENTRO DA PROBABILIDADE DE 50% DE CHANCES DE NÃO ESTOURAR A PONTUAÇÃO
    while jogadores[0][1] <= 21:
        pontuacao = jogadores[0][1]
        carta = escolher_carta()
        if carta[1] > 10:  # SE O VALOR DA CARTA CORRESPONDER A 11, 12 OU 13 (DAMA, VALETE E REIS)
            pontuacao = 10
        else:
            pontuacao = carta[1]                
        jogadores[0][1] += pontuacao
        jogadores_carta.append([jogadores[0][0],carta[0],pontuacao])        
        if jogadores[0][1] > 21:
            jogadores[0][2] = False
        else:
            if jogadores[0][1] > 17: break # SE A PONTUAÇÃO ATUAL FOR MAIOR QUE 17 PONTOS, O COMPUTADOR PARA DE ARRISCAR.
            elif jogadores[0][1] > 11: # SE A PONTUAÇÃO FOR MAIOR QUE 11 PONTOS E A PENULTIMA CARTA ESCOLHIDA TIVER SIDO MENOR QUE 6, O COMPUTADOR PARA DE ARRISCAR.
                ultima_pontuacao = jogadores_carta[len(jogadores_carta)-1][2]
                if ultima_pontuacao < 6:
                    break
    jogadores[0][2] = False

def inicio():
    # o máximo de 5 apenas por questão de estratégia
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('▓                   B L A C K   J A C K   2 1                     ▓')
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    print("       By Helldânio Barros - CopyRight(2022) - Let's Code")
    print('-------------------------------------------------------------------')
    print('SE VOCÊ ESCOLHER APENAS 1 JOGADOR, O COMPUTADOR SERÁ SEU ADVERSÁRIO')
    print('Obs: O computador também arrisca e pode estourar a pontuação')
    print('-------------------------------------------------------------------')
    n_jogadores = 0
    while n_jogadores == 0:
        n_jogadores = input('Quantos jogadores (máximo 5): ')
        if n_jogadores.isdigit():
            n_jogadores = int(n_jogadores)
        else:
            n_jogadores = 0
    if n_jogadores > 5: return
    if n_jogadores == 1:
        jogadores.append(['Computador',0,True])
    for x in range(n_jogadores):
        # jogadores = [Nome,Pontuação,Status(True-Ativo False-Inativo)]
        jogadores.append([input(f'Informe o nome do jogador {x+1}: '),0,True])

    baralho_cria()

    if jogadores[0][0] == 'Computador':
        computador_joga()

    for w in range(len(jogadores)):
        while jogadores[w][2]:
            print(f'Sr.(a) {jogadores[w][0]}')
            if input('Deseja comprar uma carta?') in ['S','s']:                
                pontuacao = jogadores[w][1]
                carta = escolher_carta()
                if carta == 'FIM': break
                identifica_carta(carta[0])
                if carta[1] > 10:  # SE O VALOR DA CARTA CORRESPONDER A 11, 12 OU 13 (DAMA, VALETE E REIS)
                    pontuacao = 10
                else:
                    pontuacao = carta[1]                
                jogadores[w][1] += pontuacao
                jogadores_carta.append([jogadores[w][0],carta[0],pontuacao])
                if jogadores[w][1] > 21:
                    jogadores[w][2] = False
                    print(f'O jogador {jogadores[w][0]} está fora do jogo!')

            else:
                jogadores[w][2] = False
    
    verifica_ganhador(jogadores)

vamos_jogar = 'S'
while vamos_jogar == 'S':
    jogadores = []
    jogadores_carta = []
    baralho = []
    inicio()
    vamos_jogar = input('Vamos jogar novamente?').upper()
