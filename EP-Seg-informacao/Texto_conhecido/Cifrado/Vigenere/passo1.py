def passo1():
    cifra1 = open("Grupo02_texto_cifrado1.txt", "r")
    cifra2 = open("Grupo02_texto_cifrado2.txt", "r")
    texto = open("txts_auxiliares/verificador.txt", "r")
    cifra1 = cifra1.read()
    cifra2 = cifra2.read()
    texto = texto.read()
    
    pontosComuns = []
    
    for x in range (len(cifra1)):
        if cifra1[x] == cifra2[x]:
            
            pontosComuns.append(x)
    
    newTexto = ""
    
    for i in range(len(texto)-99):
        for indice in pontosComuns:
            newTexto += texto[i+indice]
    newF = open("txts_auxiliares/passo1.txt", "w")
    newF.write(newTexto)