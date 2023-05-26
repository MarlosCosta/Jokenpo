import random # Importa a biblioteca random para gerar jogadas aleatórias


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador_um, jogador_dois):
    global empate, pontos_jogador_um, pontos_jogador_dois
    if jogador_um == 1: #Pedra
        if jogador_dois == 1: #Pedra
            empate += 1

        elif jogador_dois == 2: #Papel
            pontos_jogador_dois += 1

        elif jogador_dois == 3: #Tesoura
            pontos_jogador_um += 1

    elif jogador_um == 2: #Papel
        if jogador_dois == 1: #Pedra
            pontos_jogador_um += 1

        elif jogador_dois == 2:#Papel
            empate += 1

        elif jogador_dois == 3: #Tesoura
            pontos_jogador_dois += 1

    elif jogador_um == 3:  #Tesoura
        if jogador_dois == 1: #Pedra
            pontos_jogador_dois += 1

        elif jogador_dois == 2:#Papel
            pontos_jogador_um += 1

        elif jogador_dois == 3: #Tesoura
            empate += 1
    resultados = [pontos_jogador_um, pontos_jogador_dois, empate]
    return resultados


#Principal
print('JOKENPO')
print('1 = Pedra')
print('2 = Papel')
print('3 = Tesoura')

resultados = [] # Lista para armazenar os resultados das partidas
jogadas = [] # Lista para armazenar as jogadas de cada partida
pontos_jogador_um = 0
pontos_jogador_dois = 0
empate = 0

while True:
    jogada_jogador_um = valida_int('Escolha sua jogada: ', 0, 3)
    if not jogada_jogador_um:
        break
    jogada_jogador_dois = random.randint(1,3)
    jogadas.append([jogada_jogador_um, jogada_jogador_dois])
    resultados = vencedor(jogada_jogador_um, jogada_jogador_dois)
    #print(resultados)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Numero de vitorias do Jogador 1: {}' .format(resultados[0]))
print('Numero de vitorias do Jogador 2: {}' .format(resultados[1]))
print('Numero de empates: {}' .format(resultados[2]))

