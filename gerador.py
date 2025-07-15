from random import randint

# variaveis e vetores


#gerador de números aleatório de 0 a 1 que representa a bombas na matriz
def bombas():
        numero = randint(0,1)
        return numero

#gerador da matriz do campo de bombas
def gerador_campo_de_bombas(elementos):  
    campo_bombas = [] 
    for i in range(elementos):
       campo_bombas.append(bombas())
    return campo_bombas

#gerador da matriz de rastreamento de bombas

def gerador_rastreador (vet,elementos):
    vetor = []
    for i in range(elementos):
        bombas = 0
        if i == 0:
            bombas += vet[0]
            bombas += vet[1]
            bombas += vet[3]
            bombas += vet[4]
            vetor.append(bombas)
        if i == 1:
            bombas += vet[0]
            bombas += vet[1]
            bombas += vet[2]
            bombas += vet[3]
            bombas += vet[4]
            bombas += vet[5]
            vetor.append(bombas)
        if i == 2:
            bombas += vet[1]
            bombas += vet[2]
            bombas += vet[4]
            bombas += vet[5]
            vetor.append(bombas)
        if i == 3:
            bombas += vet[0]
            bombas += vet[1]
            bombas += vet[3]
            bombas += vet[4]
            bombas += vet[6]
            bombas += vet[7]
            vetor.append(bombas)
        if i == 4:
            bombas += vet[0]
            bombas += vet[1]
            bombas += vet[2]
            bombas += vet[3]
            bombas += vet[4]
            bombas += vet[5]
            bombas += vet[6]
            bombas += vet[7]
            bombas += vet[8]
            vetor.append(bombas)
        if i == 5:
            bombas += vet[1]
            bombas += vet[2]
            bombas += vet[4]
            bombas += vet[5]
            bombas += vet[7]
            bombas += vet[8]
            vetor.append(bombas)
        if i == 6:
            bombas += vet[3]
            bombas += vet[4]
            bombas += vet[6]
            bombas += vet[7]            
            vetor.append(bombas)
        if i == 7:
            bombas += vet[3]
            bombas += vet[4]
            bombas += vet[5]
            bombas += vet[6]
            bombas += vet[7]
            bombas += vet[8]            
            vetor.append(bombas)
        if i == 8:
            bombas += vet[4]   
            bombas += vet[5] 
            bombas += vet[7] 
            bombas += vet[8]          
            vetor.append(bombas)
    return vetor
   
#mostra na tela o mapa criado
def mapa(vet,elementos,elementos_por_linha):
    print("")
    for i in range(elementos):
        if (0 == ((1+i)%elementos_por_linha)):       
            print(f" {vet[i]}")
        else:
            print(f" {vet[i]} ", end="") 
    print("")
    
