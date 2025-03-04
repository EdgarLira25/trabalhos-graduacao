from auxiliares.funcoes_ativacao import *
from rede import *
from tratamento import *


def rede_comum(camada_escondida = 21,taxaDeAprendizagem = 0.1):

    # Tratamento das entradas
    entradas_treino, saidas_esperadas_treino, entradas_teste, saidas_esperadas_teste = tratamento_comum()
    
    # Instacia a rede
    redeMult = rede(63,camada_escondida,7, entradas_treino, saidas_esperadas_treino,entradas_teste, saidas_esperadas_teste, taxaDeAprendizagem)
    
    # Inicializa rede (pesos, etc)
    redeMult.inicializa_rede()
    
    # Treina rede
    acuracia, erro = redeMult.treina_rede()

    print("#"*20)
    print("Acuracia da Rede comum: ", acuracia)
    print("Erro Quadrático médio da Rede comum: ", erro)

def rede_validacao_cruzada(camada_escondida = 21,taxaDeAprendizagem = 0.1):
    
    folds = cross_val()
    
    #Estilos das folds
   
    #"Fold1 = {testes: [], saida_teste: [], treino: [], saida_treino: []}"    
    #"Fold2 = {testes: [], saida_teste: [], treino: [], saida_treino: []}"
    #"Fold3 = {testes: [], saida_teste: [], treino: [], saida_treino: []}"

    acuracia = 0
    erro = 0

    for chave in folds:

        # Instancia a Rede
        redeMult = rede(63,camada_escondida,7, folds[chave]["treino"], folds[chave]["saida_treino"],folds[chave]["testes"], folds[chave]["saida_testes"], taxaDeAprendizagem)
        # Inicializa a rede 
        redeMult.inicializa_rede()
        # Treina a Rede e soma a acurácia
        acuracia_temp, erro_temp = redeMult.treina_rede()

        acuracia += acuracia_temp
        erro += erro_temp
        
        if chave < 3:
            print("#"*20)
            input("Pressione Enter para iniciar o treinamento da Próxima Fold:\n")

        else:
            # Tira médias
            acuracia_media = acuracia/3
            erro_medio = erro/3
            print("#"*20)
            print("Acuracia da Rede Com Validação Cruzada: ", acuracia_media)
            print("Erro Quadrático médio da Rede Com Validação Cruzada: ", erro_medio)
            
            

def rede_validacao_e_parada(camada_escondida = 21,taxaDeAprendizagem = 0.1):
    
    # Trata folds
    folds = cria_treino_val_teste()
    acuracia = 0
    cont = 0
    erro = 0

    # Cada Treino recebera os parâmetros nesta ordem
    # Treino - Validação - Teste
    tres_treinos = [["limpo", "ruido", "ruido20"],["ruido20", "ruido", "limpo"],["ruido", "limpo", "ruido20"]]
    
    for treinos in tres_treinos:
        
        # Instancia a Rede
        redeMult = rede(63,camada_escondida,7, folds[treinos[0]][0], folds[treinos[0]][1],folds[treinos[2]][0], folds[treinos[2]][1], taxaDeAprendizagem)
        
        # Inicializa os Pesos da Rede
        redeMult.inicializa_rede()
        
        # Soma a acurácia do treinamento
        acuracia_temp, erro_temp = redeMult.treina_rede(tupla_validacao=folds[treinos[1]], parada=True)

        acuracia += acuracia_temp
        erro += erro_temp

        if cont < 2:
            print("#"*20)
            input("Pressione Enter para iniciar o treinamento da Próxima Fold:\n")
        else:
            
            acuracia_media = acuracia/3
            erro_medio = erro/3
            print("#"*20)
            print("Acuracia da Rede Com Validação Cruzada E Parada Antecipada: ", acuracia_media)
            print("Erro Quadrático médio da Rede Com Validação Cruzada E Parada Antecipada: ", erro_medio)
            
        cont += 1

if __name__ == "__main__":
        print()
        while( True):
            treino = int(input("Digite 1 para Treinar rede comum\nDigite 2 para treinar rede com validação cruzada\nDigite 3 para treinar rede com validação cruzada e parada antecipada:\nDigite 4 para sair do programa:\n"))
            if treino == 1:
                input("Pressione Enter para iniciar o treinamento Comum(70% treino, 30% teste, totalmente aleatório):\nAcertos(C.Treino) - Acuracia(C.Teste) - EQM(C.Teste)\n")
                rede_comum()
            elif treino == 2:
                input("Pressione Enter para iniciar o treinamento com Validação Cruzada\n(66,66% Treino, 33,33% Teste, Aleatório por tipo de Letra)\n3 Folds ao todo:\nAcertos(C.Treino) - Acuracia(C.Teste) - EQM(C.Teste)\n")
                rede_validacao_cruzada()
            elif treino == 3:
                input("Pressione Enter para iniciar o treinamento com Parada Antecipada e Validação Cruzada\n Treino, Validação, Teste\n limpo - ruido - ruido20 ||| ruido20 - ruido - limpo ||| ruido - limpo - ruido20 \nAcertos - Acuracia - EQM\n")
                rede_validacao_e_parada()
            else: 
                break
            print("#"*20)