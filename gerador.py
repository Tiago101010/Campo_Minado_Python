from random import randint
from math import sqrt

class Engine:
    #variaveis 
    opcao = "y"
    def __init__(self):
        self.elementos = 9
        self.elementos_por_linha = sqrt(self.elementos)
        #self.campo_de_bombas = self.mapa_de_bombas
        #self.mapa_do_jogador = self.mapa_do_jogador
        
    #gerador de números aleatório de 0 a 1 que representa a bomba na matriz
    def bomba(self):
            numero = randint(0,1)
            return numero

    #gerador da matriz do campo de bomba
    def gerador_do_mapa_de_bombas(self):  
        mapa_de_bombas = [] 
        for i in range(self.elementos):
          mapa_de_bombas.append(self.bomba())
        return mapa_de_bombas

    #gerador da matriz de rastreamento de bomba
    def geraddor_do_mapa_do_jogador(self, campo_de_bombas):
        mapa_de_bombas = []
        for i in range(self.elementos):
            bomba = 0
            if i == 0:
                bomba += campo_de_bombas[0]
                bomba += campo_de_bombas[1]
                bomba += campo_de_bombas[3]
                bomba += campo_de_bombas[4]
                mapa_de_bombas.append(bomba)
            if i == 1:
                bomba += campo_de_bombas[0]
                bomba += campo_de_bombas[1]
                bomba += campo_de_bombas[2]
                bomba += campo_de_bombas[3]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[5]
                mapa_de_bombas.append(bomba)
            if i == 2:
                bomba += campo_de_bombas[1]
                bomba += campo_de_bombas[2]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[5]
                mapa_de_bombas.append(bomba)
            if i == 3:
                bomba += campo_de_bombas[0]
                bomba += campo_de_bombas[1]
                bomba += campo_de_bombas[3]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[6]
                bomba += campo_de_bombas[7]
                mapa_de_bombas.append(bomba)
            if i == 4:
                bomba += campo_de_bombas[0]
                bomba += campo_de_bombas[1]
                bomba += campo_de_bombas[2]
                bomba += campo_de_bombas[3]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[5]
                bomba += campo_de_bombas[6]
                bomba += campo_de_bombas[7]
                bomba += campo_de_bombas[8]
                mapa_de_bombas.append(bomba)
            if i == 5:
                bomba += campo_de_bombas[1]
                bomba += campo_de_bombas[2]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[5]
                bomba += campo_de_bombas[7]
                bomba += campo_de_bombas[8]
                mapa_de_bombas.append(bomba)
            if i == 6:
                bomba += campo_de_bombas[3]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[6]
                bomba += campo_de_bombas[7]            
                mapa_de_bombas.append(bomba)
            if i == 7:
                bomba += campo_de_bombas[3]
                bomba += campo_de_bombas[4]
                bomba += campo_de_bombas[5]
                bomba += campo_de_bombas[6]
                bomba += campo_de_bombas[7]
                bomba += campo_de_bombas[8]            
                mapa_de_bombas.append(bomba)
            if i == 8:
                bomba += campo_de_bombas[4]   
                bomba += campo_de_bombas[5] 
                bomba += campo_de_bombas[7] 
                bomba += campo_de_bombas[8]          
                mapa_de_bombas.append(bomba)
        return mapa_de_bombas
    
    #mostra na tela o mapa criado
    def mapa(self, campo_de_bombas):
        print("")
        for i in range(self.elementos):
            if (0 == ((1+i)%self.elementos_por_linha)):       
                print(f" {campo_de_bombas[i]}")
            else:
                print(f" {campo_de_bombas[i]} ", end="") 
        print("")

    #laço para multiplas partidas
    def game(self):
        opcao = "y"
        while opcao.lower() != "n":
            bombas = 0
            pontos = 0
            vagos = 0

            #gerador de mapas
            mapa_de_bombas = self.gerador_do_mapa_de_bombas()
            print(" Campo minado\n coodenadoas de 0 a 2. não coloque menor nem maior que isso e nem letras ou caracteres especiais!")
            mapa_do_jogado = self.geraddor_do_mapa_do_jogador(mapa_de_bombas)

            #armazena quantos espaços vazios
            for i in range(self.elementos):
                    if mapa_de_bombas [i]<1:
                        vagos += 1

            #self de jogo
            while bombas == 0:
                
                #mostra o mapa de jogo na tela
                #self.mapa(mapa_de_bombas)
                self.mapa(mapa_do_jogado)
                print(f"pontos: {pontos}")
                
                #coleta a coordenada que o jogador escolheu
                linha = int(input("x: "))
                coluna = int(input("y: "))
                
                #transforma coodernadas r2 em r1
                linear = int((coluna*self.elementos_por_linha)+linha)
                
                #sistema de pontuação
                
                if mapa_de_bombas[linear] > 0:
                        bombas = 1  
                        mapa_do_jogado[linear] = "X"
                        self.mapa(mapa_do_jogado)
                        print("perdeu")
                else:
                    if (mapa_do_jogado[linear] != "*"):
                        mapa_do_jogado[linear]= "*"
                        pontos += 1
                if (pontos == vagos):
                    print("voce ganhou")
                    bombas = 1
            opcao = input("new game? [y/n]")
            if opcao == "y":
                bombas = 0
        print("end")

            
                
