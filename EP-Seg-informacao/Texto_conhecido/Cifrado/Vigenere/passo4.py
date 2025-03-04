
def possivelChave(texC, texD):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    chave = ""
    for i in range(len(texC)):
        
        posC = None
        posD = None
        
        for j in range(len(alfabeto)):
            if texC[i] == alfabeto[j]:
                posC = j
            if texD[i] == alfabeto[j]:
                posD = j
        x = (posC-posD)%26
        chave += alfabeto[x]            
    
    return chave

def criptografando(linha,chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cript = ""
    for i in range(len(linha)):
        posC = None
        posL = None
        for j in range(len(alfabeto)):
            if chave[i] == alfabeto[j]:
                posC = j
            if linha[i] == alfabeto[j]:
                posL = j
        x = (posL + posC)%len(alfabeto) 
        if x < 0:
            x = x + len(alfabeto)
        cript += alfabeto[x]            
    return cript

def passo4():
    
    cifra1 = open("Grupo02_texto_cifrado1.txt", "r")
    cifra2 = open("Grupo02_texto_cifrado2.txt", "r")
    
    refinamento = open("txts_auxiliares/refinamento.txt", "r")

    cifra1 = cifra1.read()
    cifra2 = cifra2.read()
    
    linha1 = refinamento.readline().strip()
    linha2 = refinamento.readline().strip()
    
    lastDicionario = {}
    chave_Real = ""

    if possivelChave(cifra1, linha1) not in lastDicionario:
        lastDicionario[possivelChave(cifra1, linha1)] = 1
    else:
        chave_Real = possivelChave(cifra1, linha1)
    
    if possivelChave(cifra1, linha2) not in lastDicionario:
        lastDicionario[possivelChave(cifra1, linha2)] = 1
    else:
        chave_Real = possivelChave(cifra1, linha2)
    
    if possivelChave(cifra2, linha1) not in lastDicionario:
        lastDicionario[possivelChave(cifra2, linha1)] = 1
    else:
        chave_Real = possivelChave(cifra2, linha1)

    if possivelChave(cifra2, linha2) not in lastDicionario:
        lastDicionario[possivelChave(cifra2, linha2)] = 1
    else:
        chave_Real = possivelChave(cifra2, linha2)
    
    return chave_Real