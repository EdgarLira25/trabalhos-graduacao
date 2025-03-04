def passo2():
    passo2 = open("txts_auxiliares/passo1.txt", "r")
    passo2 = passo2.read()
    substring_counts = {}
    for i in range(0,len(passo2),10):
        substring = passo2[i:i+10]
        
        if substring in substring_counts:
            
            substring_counts[substring][0] += 1
            substring_counts[substring][1].append(i)

        else:

            substring_counts[substring] = [1,[i]]
    
    dic2 = {}
    
    #guarda os dicionarios com tamanho > 1
    for sub in substring_counts:
    
        if substring_counts[sub][0] > 1:
            dic2[sub] = substring_counts[sub]
    
    texto = open("txts_auxiliares/verificador.txt", "r")
    texto = texto.read()
    
    listaPossibilidades = []
    for sub in dic2:
        listaPossibilidades.append(dic2[sub][1])
    
    
    analise = open("txts_auxiliares/textos_possiveis.txt", "w")
    for listap in listaPossibilidades:
        for item in listap:
            temp = int(item/10)
            analise.write(texto[temp:temp+100]+"\n")