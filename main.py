from random import randint
from math import sqrt

#gerador de números aleatório de 0 a 1 que representa a bombas na matriz
def bomba():
    numero = randint(0,1)
    return numero

#gerador da matriz do campo minado 
max= 9

vetor = []
def campo():
    for i in range(max+1):
        vetor.append(bomba())

#mostra o campo
repeticao = sqrt(max)
def mostrar(vet):
    print("")
    for i in range(max):
            if (0 == ((1+i)%repeticao)):       
                print(f" {vet[i]}")
            else:
                print(f" {vet[i]} ", end="") 
    print("")
                
# função que armazena quantas bombas estão em volta
rastreia_bomba = []
bombas = 0
def rastreador ():
    for i in range(max):
        bombas =0
        if i == 0:
            bombas += vetor[0]
            bombas += vetor[1]
            bombas += vetor[3]
            bombas += vetor[4]
            rastreia_bomba.append(bombas)
        if i == 1:
            bombas += vetor[0]
            bombas += vetor[1]
            bombas += vetor[2]
            bombas += vetor[3]
            bombas += vetor[4]
            bombas += vetor[5]
            rastreia_bomba.append(bombas)
        if i == 2:
            bombas += vetor[1]
            bombas += vetor[2]
            bombas += vetor[4]
            bombas += vetor[5]
            rastreia_bomba.append(bombas)
        if i == 3:
            bombas += vetor[0]
            bombas += vetor[1]
            bombas += vetor[3]
            bombas += vetor[4]
            bombas += vetor[6]
            bombas += vetor[7]
            rastreia_bomba.append(bombas)
        if i == 4:
            bombas += vetor[0]
            bombas += vetor[1]
            bombas += vetor[2]
            bombas += vetor[3]
            bombas += vetor[4]
            bombas += vetor[5]
            bombas += vetor[6]
            bombas += vetor[7]
            bombas += vetor[8]
            rastreia_bomba.append(bombas)
        if i == 5:
            bombas += vetor[1]
            bombas += vetor[2]
            bombas += vetor[4]
            bombas += vetor[5]
            bombas += vetor[7]
            bombas += vetor[8]
            rastreia_bomba.append(bombas)
        if i == 6:
            bombas += vetor[3]
            bombas += vetor[4]
            bombas += vetor[6]
            bombas += vetor[7]            
            rastreia_bomba.append(bombas)
        if i == 7:
            bombas += vetor[3]
            bombas += vetor[4]
            bombas += vetor[5]
            bombas += vetor[6]
            bombas += vetor[7]
            bombas += vetor[8]            
            rastreia_bomba.append(bombas)
        if i == 8:
            bombas += vetor[4]   
            bombas += vetor[5] 
            bombas += vetor[7] 
            bombas += vetor[8]          
            rastreia_bomba.append(bombas)

#interaje como usuario


campo()
rastreador()

#coleta a posiçãodo número

#Revela se tem bomba sendo o * sem bomba e o X com bomba
bombas = 0
pontos = 0
vitoria = 0
for i in range(max):
    if vetor[i]<1:
        vitoria += 1
print(vitoria)
while bombas == 0:
    mostrar(vetor)
    mostrar(rastreia_bomba)
    print(f"pontos {pontos}")
    linha = int(input("x: ")0)
    coluna = int(input("y: "))
    linear = ((coluna*3)+linha)
    if vetor[linear] > 0:
            bombas = 1  
    if bombas > 0 : 
        rastreia_bomba[linear]= "X"
        mostrar(rastreia_bomba)
        print("perdeu")
    else:
        if (rastreia_bomba[linear] != "*"):
            rastreia_bomba[linear]= "*"
            pontos += 1
    if (pontos == vitoria):
        print("voce ganhou")
        bombas = 1
