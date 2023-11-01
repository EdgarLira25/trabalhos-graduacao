def passo3():
    analise = open("txts_auxiliares/textos_possiveis.txt", "r")
    refinamento = open("txts_auxiliares/refinamento.txt", "w")
    linhas = analise.readlines()

    cifra1 = open("Grupo02_texto_cifrado1.txt", "r")
    cifra2 = open("Grupo02_texto_cifrado2.txt", "r")
    cifra1 = cifra1.read()
    cifra2 = cifra2.read()
    listaMaster = []

    for x in range (len(cifra1)):
        if cifra1[x] == cifra2[x]:
            listaMaster.append(x)

    for i in range(0, len(linhas), 2):
        listaTemp = []
        linha1 = linhas[i].strip()  
        linha2 = linhas[i+1].strip() 
         
        for y in range (len(cifra1)):
            if linha1[y] == linha2[y]:
                listaTemp.append(y)

        if listaTemp == listaMaster:

            refinamento.write(linha1+"\n")
            refinamento.write(linha2+"\n")