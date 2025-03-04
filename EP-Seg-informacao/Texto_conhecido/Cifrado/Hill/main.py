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


def testa_chave(chave, texto_numerico, textoAberto):
    
    textoDecriptoNum = chave@texto_numerico%26
    textoDecriptoNum = textoDecriptoNum.T.reshape(100)
    textoDecriptoNum = num2texto(textoDecriptoNum)
    
    if textoDecriptoNum in textoAberto:
        return textoDecriptoNum
    else:
        return None

def decripta_encontra_chave_texto(texto_numerico, textoAberto):
    
    for i in range (26):
        for j in range (26):
            for k in range (26):
                for z in range (26):
                    chave = np.array([[i,j],[k,z]])
                    texto_descriptografado = testa_chave(chave,texto_numerico,textoAberto)
                    if(texto_descriptografado):
                        return chave, texto_descriptografado

    return None

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

def decripta(textoCrypto, texto_aberto, alfabeto):

    textoCryptoNum = texto2num(textoCrypto, alfabeto)
    textoCryptoNum = np.array(textoCryptoNum).reshape((50,2)).T
    chave_inv, descripto = decripta_encontra_chave_texto(textoCryptoNum, texto_aberto)
    chave = encontra_inversa2x2(chave_inv)
    
    return chave, chave_inv, descripto
#   return chave, texto_decripto

if __name__ == "__main__":
    
    cifrado = open("Grupo02_texto_cifrado.txt", "r")
    cifrado = cifrado.read()

    texto = open("verificador.txt", "r")
    texto = texto.read()

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    chaveEncript, chaveDecript, texto_aberto = decripta(cifrado, texto, alfabeto)

    # Não faz nada além de passar parametros da variavel chaveDecript(variavel do NUMPY) para a chave_inv(Variavel lista do python)

    chave_inv = [[None,None],[None,None]]
    for x in range(2):
        for y in range (2):
            chave_inv[x][y] = chaveDecript[x,y]


    escreve_arq = open("Grupo02_texto_aberto.txt", "w")
    escreve_arq.write("Texto Aberto = " + str(texto_aberto)+"\n")
    escreve_arq.write("Texto Fechado = " + str(cifrado)+"\n")
    escreve_arq.write("Alfabeto = " + str(alfabeto)+"\n")
    escreve_arq.write("Chave Decript = " + str(list(chave_inv))+"\n")
    escreve_arq.write("Chave Encript = " + str(chaveEncript)+"\n")