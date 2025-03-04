import re
import multiprocessing

padrao = None

def verificar_linha(linha):
    x = re.findall(padrao, linha)
    if len(x) > 7:
        return linha
    
def passo2():
    nome_arquivo = "dicionario.txt"  # Nome do arquivo de texto
    
    lista_palavras = []  # Lista vazia para armazenar as palavras

    # Ler o arquivo linha por linha e adicionar as palavras na lista
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavra = linha.strip()  # Remover espaços em branco e quebras de linha
            lista_palavras.append(palavra)

    global padrao
    
    padrao = '|'.join(lista_palavras)

    with open('txts_auxiliares/textosSemChave.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    linhas_contendo_palavras = []

    with multiprocessing.Pool() as executor:
        resultados = executor.map(verificar_linha, linhas)
        for resultado in resultados:
            if resultado:
                linhas_contendo_palavras.append(resultado)

    possibilidades = open("txts_auxiliares/textosPossiveis.txt", "w")

    for linha in linhas_contendo_palavras:
        possibilidades.write(linha.strip())