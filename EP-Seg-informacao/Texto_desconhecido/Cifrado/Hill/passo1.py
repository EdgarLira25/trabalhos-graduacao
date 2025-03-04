import numpy as np

def inversoMultiplicativo(num, mod):

    for x in range (mod):
        if (((num)*x % mod) == 1):
        
            return x
    return num

def inversoAditivo(num, mod):
    return num + mod

def num2texto(textoNum,alfabeto = "abcdefghijklmnopqrstuvwxyz"):
    
    texto_alf = ""

    for num in textoNum:
        texto_alf += alfabeto[num]

    return texto_alf

def texto2num(texto,alfabeto = "abcdefghijklmnopqrstuvwxyz"):

    textoCryptNum = []
    for letra in texto:
        for x in range (len(alfabeto)):
            if letra == alfabeto[x]:
                textoCryptNum.append(x)

    return textoCryptNum


def testa_chave(chave, texto_numerico, dicionario):
    
    textoDecriptoNum = chave@texto_numerico%26
    textoDecriptoNum = textoDecriptoNum.T.reshape(100)
    textoDecriptoNum = num2texto(textoDecriptoNum)
    
    return textoDecriptoNum
        
def decripta_encontra_chave_texto(texto_numerico, dicionario):
    textosPossiveis = []

    for i in range (26):
        for j in range (26):
            for k in range (26):
                for z in range (26):
    
                    chave = np.array([[i,j],[k,z]])
                    texto_descriptografado = testa_chave(chave,texto_numerico,dicionario)
                    textosPossiveis.append([texto_descriptografado,[[i,j],[k,z]]])
                    #textosPossiveis.append(texto_descriptografado)
    return textosPossiveis

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

def decripta(textoCrypto, dicionario, alfabeto):

    textoCryptoNum = texto2num(textoCrypto, alfabeto)
    textoCryptoNum = np.array(textoCryptoNum).reshape((50,2)).T
    textos_possiveis = decripta_encontra_chave_texto(textoCryptoNum, dicionario)
    #chave = encontra_inversa2x2(chave_inv)
    
    return textos_possiveis
 #   return chave, texto_decripto

def passo1():
    nome_arquivo = "dicionario.txt"  # Nome do arquivo de texto
    lista_palavras = []  # Lista vazia para armazenar as palavras

    # Ler o arquivo linha por linha e adicionar as palavras na lista
    
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavra = linha.strip()  # Remover espaços em branco e quebras de linha
            lista_palavras.append(palavra)

    cifrado = open("Grupo02_texto_cifrado.txt", "r")
    cifrado = cifrado.read()

    texto = open("verificador.txt", "r")
    texto = texto.read()

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    textos_possiveis = decripta(cifrado, lista_palavras, alfabeto)
    
    resp = open("txts_auxiliares/textosComChave.txt", "w")
    for array in textos_possiveis:
        resp.write((str(array))+"\n")
    
    resp = open("txts_auxiliares/textosSemChave.txt", "w")
    for array in textos_possiveis:
        resp.write(str(array[0])+"\n")