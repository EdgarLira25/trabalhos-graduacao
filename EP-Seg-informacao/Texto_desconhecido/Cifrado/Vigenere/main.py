import random
import multiprocessing

def cria_dicionario(texto,x):
    
    dic = {}
    
    for indice in range(len(texto)):
        chave = texto[indice:indice+x]
        dic[chave] = 0
    
    for indice in range(len(texto)):
        chave = texto[indice:indice+x]
        dic[chave] += 1

    return dic

def texto_para_num(palavra1, palavra2):
    lista = [[]  for _ in range(100)]
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    bans = "wxyk"
    listando = []
    for indice in range(len(palavra1)):
        diff_num = (alfabeto.index(palavra1[indice]) - alfabeto.index(palavra2[indice]))%26 
        listando.append(diff_num)
        for x in range(len(alfabeto)):
            parte1 = alfabeto[x]
            parte2 = alfabeto[(x+diff_num)%26]
            if parte1 not in bans and parte2 not in bans:
                lista[indice].append([parte1, parte2])

    return lista

def decripta_vigenere(lista_mestre, lista_ver):
    
    lista_temp = []
    palavra_decript1 = ""
    palavra_decript2 = ""
    trigramas_aceitos = "do de da lh rr co po lh"

    for indice in range(0,100):
        
        lista_temp = []
        
        if indice > 1:
        
            tri1 = palavra_decript1[-2] + palavra_decript1[-1]
            tri2 = palavra_decript2[-2] + palavra_decript2[-1]        
        
        else:
        
            tri1 = ""
            tri2 = ""

        if tri1 in trigramas_aceitos or tri2 in trigramas_aceitos: 
            for lista in lista_mestre[indice]:

                score = 0
                
                try:
                    score += lista_ver[2][palavra_decript1[-2] + palavra_decript1[-1] + lista[0]] 
                    score += lista_ver[2][palavra_decript2[-2] + palavra_decript2[-1] + lista[1]]
                    lista_temp.append([score,lista])
                
                except:
                    pass
        
        else:

            for lista in lista_mestre[indice]:
                
                score = 0

                try:
                    
                    score += lista_ver[1][palavra_decript1[-1] + lista[0]] 
                    score += lista_ver[1][palavra_decript2[-1] + lista[1]]
                    lista_temp.append([score,lista])
                
                except:
                    pass    

        lista_temp.sort(reverse=True,key=lambda x: x[0])
      
        lista_temp = lista_temp[:5]
      
        lista_pesos = [item[0] for item in lista_temp]
        lista_letras = [item[1] for item in lista_temp]
        try:
            letra = random.choices(lista_letras,weights=lista_pesos,k=1)[0]

        except:
            letra = random.choice(lista_mestre[indice])
            pass

        palavra_decript1 += letra[0]
        palavra_decript2 += letra[1]
      
    return palavra_decript1+" "+palavra_decript2


def decripta_vigenere_parallel(_):
    a = decripta_vigenere(lista, lista_ver)
    return a


if __name__ == "__main__":
    
    cifrado1 = open("Grupo02_texto_cifrado1.txt", "r").read() 
    cifrado2 = open("Grupo02_texto_cifrado2.txt", "r").read()
    cifrado1 = cifrado1.strip()
    cifrado2 = cifrado2.strip()

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    ver = open("verificador.txt", "r")
    ver = ver.read()
    ver = ver.strip()

    lista_ver = []
    lista_cifrado1 = []
    lista_cifrado2 = []

    monograma_ver = cria_dicionario(ver, 1)
    monograma_ver = dict(sorted(monograma_ver.items(),reverse=True, key=lambda item: item[1]))

    bigrama_ver = cria_dicionario(ver, 2)
    bigrama_ver = dict(sorted(bigrama_ver.items(),reverse=True, key=lambda item: item[1]))
    
    trigrama_ver = cria_dicionario(ver, 3)
    trigrama_ver = dict(sorted(trigrama_ver.items(),reverse=True, key=lambda item: item[1]))

    lista_ver.append(monograma_ver)
    lista_ver.append(bigrama_ver)
    lista_ver.append(trigrama_ver)
  
    lista = texto_para_num(cifrado1, cifrado2)
    
    pool = multiprocessing.Pool()
    lista_textos = pool.map(decripta_vigenere_parallel, range(2000000))
    pool.close()
    pool.join()

    texto = open("saidas.txt", "w")
    for text in lista_textos:
        texto.write(text+"\n")
    
    texto.close()
