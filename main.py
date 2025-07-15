from gerador import mapa, gerador_campo_de_bombas, gerador_rastreador
from math import sqrt

#variaveis e vetores
opcao = "y"
bombas = 0
pontos = 0
vitoria = 0
elementos = 9
elementos_por_linha = sqrt(elementos)

#laço para multiplas partidas
while opcao.lower() != "n":

    #gerador de mapas
    vetor = gerador_campo_de_bombas(elementos)
    rastreador = gerador_rastreador(vetor,elementos)

    #armazena a pontuação e vitórias da partida
    for i in range(elementos):
            if vetor[i]<1:
                vitoria += 1

    #engine de jogo
    while bombas == 0:
        
        #mostra o mapa de jogo na tela
        mapa(vetor,elementos,elementos_por_linha)
        mapa(rastreador,elementos,elementos_por_linha)
        print(f"pontos {pontos}")
        
        #coleta a coordenada que o jogador escolheu
        linha = int(input("x: "))
        coluna = int(input("y: "))
        
        #transforma coodernadas r2 em r1
        linear = int((coluna*elementos_por_linha)+linha)
        
        #sistema de pontuação
        if vetor[linear] > 0:
                bombas = 1  
                rastreador[linear]= "X"
                mapa(rastreador,elementos, elementos_por_linha)
                print("perdeu")
        else:
            if (rastreador[linear] != "*"):
                rastreador[linear]= "*"
                pontos += 1
        if (pontos == vitoria):
            print("voce ganhou")
            bombas = 1
    opcao = input("new game? [y/n]")
    if opcao == "y":
        bombas = 0
print("end")