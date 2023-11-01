def decripta_aux(trechoCripto, trechoTeste, dictCripto):
    listTeste = []
    
    # Crio uma lista de letras -- sem repetição -- das letras presentes no trecho do livro do Lima Barreto
    for letra in trechoTeste:
        if letra in listTeste:
            pass
        else: 
            listTeste.append(letra)

    # Verifico se tem a mesma quantidade de letras
    if len(listTeste) != len(dictCripto):
        return None
    
    # Percorre todas as posições tanto do dicionario quanto da lista
    for x in range(len(trechoTeste)):
        
        # Guardo a letra da posição X na chave do dicionario de letras da criptografia
        if dictCripto[trechoCripto[x]] == None:
            dictCripto[trechoCripto[x]] = trechoTeste[x]
        # Se a letra já estiver no dicionário verifico se corresponde a letra que o dicionário guardou
        elif (dictCripto[trechoCripto[x]] == trechoTeste[x]):

            pass
        # Se a letra-chave não for correspondente a letra-valor retornamos None
        else:

            return None
        
    return dictCripto

def decripta(trechoCripto, texto):


    # Estrutura do dicionario {Chave : Valor}
    # Conseguimos mapear a chave de decriptografia enquanto comparamos o texto
    dicionario = {}
    for letra in trechoCripto:
        if letra in dicionario:
            pass
        else: 
            dicionario[letra] = None
    

    for i in range(len(texto)-len(trechoCripto)):
        verificadorDic = decripta_aux(trechoCripto, texto[i:i+len(trechoCripto)], dicionario.copy())
        if (verificadorDic != None):
            return texto[i:i+100], verificadorDic
            

if __name__ == "__main__":

    cifrado = open("Grupo02_texto_cifrado.txt", "r")
    cifrado = cifrado.read()

    texto = open("verificador.txt", "r")
    texto = texto.read()

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    texto_aberto, verificadorDic = decripta(cifrado,texto)   

    #Encontro a Chave de Decriptação a partir do dicionário retornado
    chaveDecript = ""
    for letra in alfabeto:
        if letra in verificadorDic:
            chaveDecript += verificadorDic[letra]
        else:
            chaveDecript +="_"
    
    # Transformo a Chave em valor e o valor em chave
    dicionario_invertido = {valor: chave for chave, valor in verificadorDic.items()}
    
    # Encontro a chave de Encriptação
    chaveEncript = ""
    for letra in alfabeto:
        if letra in dicionario_invertido:
            chaveEncript += dicionario_invertido[letra]
        else:
            chaveEncript+="_"

    escreve_arq = open("Grupo02_texto_aberto.txt", "w")
    escreve_arq.write("Texto Aberto  = " + str(texto_aberto)+"\n")
    escreve_arq.write("Texto Fechado = " + str(cifrado)+"\n")
    escreve_arq.write("Alfabeto =      " + str(alfabeto)+"\n")
    escreve_arq.write("Chave Decript = " + str(chaveDecript)+"\n")
    escreve_arq.write("Chave Encript = " + str(chaveEncript)+"\n")