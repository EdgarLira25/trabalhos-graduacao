import re
import multiprocessing

def verificar_linha(linha):
    x = re.findall(padrao, linha)

    if len(x) > 7:
        return linha

padrao = None    
def passo2():
    nome_arquivo = "dicionario.txt"
    
    lista_palavras = []

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavra = linha.strip() 
            lista_palavras.append(palavra)

    global padrao
    
    padrao = '|'.join(lista_palavras)

    with open('saidas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    pool = multiprocessing.Pool()
    lista_resp = pool.map(verificar_linha, linhas)
    pool.close()
    pool.join()

    possibilidades = open("textosPossiveis.txt", "w")
    #print(lista_resp)
    for resp in lista_resp:
        if resp == None:
            pass
        else:
            possibilidades.write(resp)

passo2()