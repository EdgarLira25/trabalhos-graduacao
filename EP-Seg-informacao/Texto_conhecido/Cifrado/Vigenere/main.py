from passo1 import passo1
from passo2 import passo2
from passo3 import passo3
from passo4 import passo4
import time

if __name__ == "__main__":

    inicio = time.time()
    #Encontro todos as posições onde as letras se repetem e "reduzo" o tamanho de cada possibilidade de comparação para o tamanho de repetições
    passo1()
    fim1 = time.time()
    print("Passo 1 Duração =", round(fim1-inicio, 2),"Segundos")
    #Utilizo o arquivo que possui cada possibilidade e separo pares de strings com o mesmo padrão(posições onde as letras se repetem) 
    #E após isso, "descompacto as strings novamento"
    passo2()
    fim2 = time.time()
    print("Passo 2 Duração =", round(fim2-fim1,2), "Segundos")
    #Faço um refinamento das strings, faço com que sigam mais estritamente esse padrão, pois no passo anterior eu comparava as strings compactadas
    passo3()
    fim3 = time.time()
    print("Passo 3 Duração =", round(fim3-fim2,2),"Segundos")
    #Agora que tenho as possibilidades de string, tento encontrar o padrão comparando com o arquivo criptografado, e quando houver repetição, sei qual é o texto
    chave = passo4()
    fim4 = time.time()
    print("Passo 4 Duração =", round(fim4-fim3,2), "Segundos")

    file = open("Grupo02_textos_abertos.txt", "w")

    
    refinados = open("txts_auxiliares/refinamento.txt", "r")
    refinados = refinados.readlines()

    file.write("Chave: " + str(chave)+"\n")
    for line in refinados:
        file.write("Texto Descriptografado: " + line)
    
