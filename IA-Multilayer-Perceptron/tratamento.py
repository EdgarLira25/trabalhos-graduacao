from auxiliares.funcoes_tratamento import *
# Retorna uma lista de treino e uma de testes, criadas aleatoriamente
def tratamento_comum():

    lista_caracteres = []

    leitura_csv("entradas/caracteres-limpo.csv", lista_caracteres)
    leitura_csv("entradas/caracteres-ruido.csv", lista_caracteres)
    leitura_csv("entradas/caracteres_ruido20.csv", lista_caracteres)
    
    lista_caracteres_treino, lista_caracteres_teste = separa_lista_random(lista_caracteres)
    
    lista_entradas_treino = []
    lista_saidas_esperadas_treino = []
    lista_entradas_teste = []
    lista_saidas_esperadas_teste = []

    for element in lista_caracteres_treino:
        
        lista_entradas_treino.append(element[:63])
        lista_saidas_esperadas_treino.append(element[-7:])

    for element in lista_caracteres_teste:

        lista_entradas_teste.append(element[:63])
        lista_saidas_esperadas_teste.append(element[-7:])
    
    return lista_entradas_treino, lista_saidas_esperadas_treino, lista_entradas_teste, lista_saidas_esperadas_teste

# Cria dados para Cross_Validação, aleatórios tomando os devidos cuidados para não repetir dados de treino e testes
def cross_val():

    lista_caracteres = []

    leitura_csv("entradas/caracteres-limpo.csv", lista_caracteres)
    leitura_csv("entradas/caracteres-ruido.csv", lista_caracteres)
    leitura_csv("entradas/caracteres_ruido20.csv", lista_caracteres)

    folds_testes = cria_dict_testes(lista_caracteres.copy())
    folds_treinos = cria_dict_treino(lista_caracteres.copy(),folds_testes)
    
    return trata_folds(folds_treinos,folds_testes)

# Cria dados de Treino - Validação - Testes, não é totalmente aleatório
def cria_treino_val_teste():

    lista1 = []
    lista2 = []
    lista3 = []

    leitura_csv("entradas/caracteres-limpo.csv", lista1)
    leitura_csv("entradas/caracteres-ruido.csv", lista2)
    leitura_csv("entradas/caracteres_ruido20.csv", lista3)

    limpo_entrada, limpo_saida = aux_fold(lista1)
    ruido_entrada, ruido_saida = aux_fold(lista2)
    ruido20_entrada, ruido20_saida = aux_fold(lista3)
    
    dict_listas = {"limpo":[limpo_entrada, limpo_saida],
                   "ruido":[ruido_entrada, ruido_saida],
                   "ruido20":[ruido20_entrada, ruido20_saida]}
    
    return dict_listas