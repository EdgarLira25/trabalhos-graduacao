import ast
import numpy as np

def inversoMultiplicativo(num, mod):

    for x in range (mod):
        if (((num)*x % mod) == 1):
        
            return x
    return num

def inversoAditivo(num, mod):
    return num + mod

def encontra_inversa2x2(matriz):
    det = np.linalg.det(matriz)

    deter = inversoMultiplicativo(int(det),26)

    chave = [[None,None],[None,None]]
    for i in range(2):
        for j in range(2):
            temp = (deter*matriz[(j+1)%2][(i+1)%2]*((-1)**(i+j)))%26
            if temp < 0:
                temp = inversoAditivo(temp,26)
            chave[i][j] = int(temp)

    return chave

def passo3():
    
    textoProvavel = open("txts_auxiliares/textosPossiveis.txt", "r").read()

    chavesEtextos = open("txts_auxiliares/textosComChave.txt", "r")
    
    linhas = chavesEtextos.readlines() 
    
    linhaExata = ""
    for linha in linhas:
        if textoProvavel in linha:
            linhaExata = linha
            break

    textoEchave_inversa = ast.literal_eval(linhaExata)
    
    texto = str(textoEchave_inversa[0])
    
    chave_inversa = list(textoEchave_inversa[1])

    chave = encontra_inversa2x2(chave_inversa)

    cifrado = open("Grupo02_texto_cifrado.txt", "r")

    cifrado = cifrado.read()

    decript = open("Grupo02_Hill_descriptografado.txt", "w")

    decript.write("Texto Cifrado: "+ cifrado+"\n")
    decript.write("Chave: "+ str(chave)+"\n")
    decript.write("Chave Inversa: "+ str(chave_inversa)+"\n")
    decript.write("Texto Aberto: "+ texto+"\n")