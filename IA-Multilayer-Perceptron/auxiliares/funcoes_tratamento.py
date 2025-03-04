
import csv
import random

def leitura_csv(caminho, lista_caracteres):
    with open(caminho, 'r', encoding='utf-8-sig') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            lista_temp = []
            for elemento in linha:
                lista_temp.append(int(elemento))
            lista_caracteres.append(lista_temp)

def separa_lista_random(lista):

    random.shuffle(lista)
    
    split_point = int(len(lista)*0.33333+1)
    
    lista_treino = lista[split_point:]
    lista_teste = lista[:split_point]
    
    return lista_treino, lista_teste

def separa_lista_por_caracter(lista_caracteres):
    
    listas = { 'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'J': [], 'K': [] }

    for lista in lista_caracteres:

        if lista[-7] == 1: listas['A'].append(lista)
        elif lista[-6] == 1: listas['B'].append(lista)
        elif lista[-5] == 1: listas['C'].append(lista)
        elif lista[-4] == 1: listas['D'].append(lista)
        elif lista[-3] == 1: listas['E'].append(lista)
        elif lista[-2] == 1: listas['J'].append(lista)
        elif lista[-1] == 1: listas['K'].append(lista)

    return listas

def cria_dict_testes(lista):
    dict_folds = {1:[],2:[],3:[]}
    dict_caracteres = separa_lista_por_caracter(lista)

    for lista in dict_caracteres:
        for fold in dict_folds:
            for _ in range (0,3):
                caracter_rand = random.choice(dict_caracteres[lista])
                dict_caracteres[lista].remove(caracter_rand)
                dict_folds[fold].append(caracter_rand)
         
    return dict_folds

def cria_dict_treino(lista_carac, folds_testes):
    folds_treinos = {1:[],2:[],3:[]}
    for x in range(1,4):
        lista_temp = lista_carac.copy()
        for lista in folds_testes[x]:
            if lista in lista_temp:
                lista_temp.remove(lista)
        folds_treinos[x] = lista_temp
    
    return folds_treinos


def aux_fold(lista):
    entrada = []
    saida = []
    for item in lista:
        entrada.append(item[:63])
        saida.append(item[-7:])

    return entrada, saida

def trata_folds(folds_treinos, folds_testes):

    dicionario_generico = {
    "treino": [],
    "saida_treino": [],
    "testes": [],
    "saida_testes": []
    }
    
    folds = { 1:{}, 2:{}, 3:{} } 

    for x in range(1,4):

        dict_temp = dicionario_generico.copy()
        dict_temp["treino"], dict_temp["saida_treino"] = aux_fold(folds_treinos[x])
        dict_temp["testes"], dict_temp["saida_testes"] = aux_fold(folds_testes[x])
        folds[x] = dict_temp
    
    return folds
