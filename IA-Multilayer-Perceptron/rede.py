from neuronio import *
from escritas import *

class rede:
    def __init__(self, num_entradas : int, num_internos : int, num_saida: int, entradas:list, saidas_esperadas:list, entradas_testes : list, saidas_testes : list, taxaAprendizagem:float):
        
        #Numeros de Entradas
        self.num_entradas = num_entradas
        self.num_internos = num_internos
        self.num_saida = num_saida
        self.taxaAprendizagem = taxaAprendizagem

        #Neuronios internos e de saida são uma lista de neuronios
        self.neuroniosInternos = []
        self.neuroniosSaida = []
        
        #entradas e saidas esperadas do programa
        self.entradas = entradas
        self.saidas_esperadas = saidas_esperadas

        #entradas e saidas esperadas dos testes
        self.entradas_testes = entradas_testes
        self.saidas_testes = saidas_testes

    
    def inicializa_rede(self):
        escreve_hiperparametros(self,"hiperparametros/Hiper_Parametros")
        #inicia neuronios internos de acordo com a quantidade passada
        for x in range(self.num_internos):
            self.neuroniosInternos.append(NeuronioEscondido(x))
        
        #inicia neuronios de saida de acordo com a quantidade passada como parametro
        for x in range(self.num_saida):
            self.neuroniosSaida.append(NeuronioDeSaida(x))
        
        #inicializa os pesos dos neuronios escondidos de acordo com o numero de entradas na rede
        for neuronio in self.neuroniosInternos:
            neuronio.inicia_pesos(self.num_entradas)
        
        #inicializa os pesos do neuronios de saida de acordo com o numero de neuronios internos
        for neuronio in self.neuroniosSaida:
            neuronio.inicia_pesos(self.num_internos)

        escreve_pesos(self,"pesos_iniciais/Pesos_Iniciais")

    def feedForward(self, indice, entradaTreino = None):

        saidaAtual = []

        #Entradas dos neurônios da primeira camada escondida
        if entradaTreino == None:        
            for neuronio in self.neuroniosInternos:
                neuronio.entradas = self.entradas[indice]
        else:
            for neuronio in self.neuroniosInternos:
                neuronio.entradas = entradaTreino
        
        #zero as entradas dos neuronios de saida
        for neuronioSaida in self.neuroniosSaida:
            neuronioSaida.entradas = []

        #passa a saida dos neuronios internos para entrada dos neuronios de saida
        for neuronio in self.neuroniosInternos:
            res = neuronio.calc_saida()
            for neuronioSaida in self.neuroniosSaida:
                neuronioSaida.entradas.append(res)
    
        #Temos a saida do neuronio de saida
        for neuronioOut in self.neuroniosSaida:
            saidaAtual.append(neuronioOut.calc_saida())
        
        return saidaAtual
    
    # Realiza RetroPropagação
    def retroPropagation(self,saidaEsperada,saidaAtual):
        #Cada neuronio de saida calcula seu termo de erro e seus ajustes que serão feitos mais tarde
        for neuronioSaida in self.neuroniosSaida:
            neuronioSaida.calc_termoErro(saidaEsperada, saidaAtual)
            neuronioSaida.calc_ajustesDePesos(self.taxaAprendizagem)

        #Cada neuronio interno calcula seu termo de erro(baseados nos neuronios de saida) e seus ajustes que serão feitos mais tarde
        for neuronioInterno in self.neuroniosInternos:
            neuronioInterno.calc_termoErro(self.neuroniosSaida)
            neuronioInterno.calc_ajustesDePesos(self.taxaAprendizagem)
    
    # Altera os pesos
    def alteraPeso(self):

        #Função que altera peso dos neurônios internos e de saida
        for neuronioInterno in self.neuroniosInternos:
            neuronioInterno.salvarNovosPesos()
        for neuronioSaida in self.neuroniosSaida:
            neuronioSaida.salvarNovosPesos()
    
    # Treina uma época
    def treina_Epoca(self, acertos):

        teste = []
        for x in range(0,len(self.entradas)):
            #Realiza o feedforward e guarda a saida
            resFeed = self.feedForward(x)
            teste.append(resFeed)
            ajus = 7
            
            #Verifica a corretude da saida
            for y in range(len(self.saidas_esperadas[x])):

                if (self.saidas_esperadas[x][y] == -1 and resFeed[y] < -0.95) or (self.saidas_esperadas[x][y] == 1 and resFeed[y] > 0.95):
                        ajus -= 1              

            # Se a saida nao estiver correta entra nesse if, faz a retropropagação e ajusta os pesos
            if ajus > 0:
                acertos = acertos - 1
                self.retroPropagation(self.saidas_esperadas[x],resFeed)
                self.alteraPeso()
            
        return acertos
    
    # Utiliza os dados de testes, para testar a rede
    # Cria matriz de confusão e outros calculos uteis como acurácia
    def testa_rede(self, matriz_conf = False):

        teste = []
        acertos = len(self.saidas_testes)

        #Cálcula acurácia para os dados de teste
        for x in range(0, len(self.entradas_testes)):
            
            resFeed = self.feedForward(x, entradaTreino = self.entradas_testes[x])
            teste.append(resFeed)

            letra_da_rede = resFeed.index(max(resFeed))

            letra = self.saidas_testes[x].index(max(self.saidas_testes[x]))
            
           
            if letra != letra_da_rede:
                acertos -= 1

        #Cálculo do erro quadrático médio
        erro_quadratico_medio = 0
        for x in range(0, len(self.entradas_testes)):
            for y in range (0,len(teste[x])):
                erro_quadratico_medio += ((self.saidas_testes[x][y]-teste[x][y])**2)

        erro_quadratico_medio = erro_quadratico_medio/(len(self.entradas_testes))
        
        
        # Cria Matriz de Confusão
        matriz = [[0] * 7 for _ in range(7)]
        #[0, 0, 0, 0, 0, 0, 0]
        #[0, 0, 0, 0, 0, 0, 0]
        #[0, 0, 0, 0, 0, 0, 0]
        #[0, 0, 0, 0, 0, 0, 0]
        #[0, 0, 0, 0, 0, 0, 0]
        #[0, 0, 0, 0, 0, 0, 0]
        #[0, 0, 0, 0, 0, 0, 0]
        
        #Se é a ultima interação entra nesse IF
        if matriz_conf == True:

            #Cria Matriz de confusão
            for x in range(0, len(self.entradas_testes)):  
                letra_da_rede = teste[x].index(max(teste[x]))
                letra = self.saidas_testes[x].index(max(self.saidas_testes[x]))
                matriz[letra][letra_da_rede] += 1

            escreve_saidas_testes(self, "saidas_Testes", teste,self.saidas_testes)

            return acertos/len(self.saidas_testes), acertos, matriz , erro_quadratico_medio
        
        return acertos/len(self.saidas_testes), erro_quadratico_medio
    
    
    # Treina a rede
    # Valores padrões para parada, caso seja true, terá parada antecipada
    # Caso haja dados de validacao, adicionar uma tupla com 2 listas, 1 de entradas e 1 de saidas esperadas da validação
    def treina_rede(self, tupla_validacao = None, parada = False):
        
        if parada == True:
            acuraciaMax = 0
            melhores_pesos = None
        
        pes = escrita_erro(self,"erros/Erro_Por_interação" )        
        acertosEsperados = len(self.entradas)
        cont = 0
        pes.write("Interação" + ", " + "Acurácia"+ ", Erro Quadrático médio"+"\n")
        
        #While que gerencia as funções principais de treinamento
        while(True):
            
            #Verifica se usa os dados de validação ou de teste para realizar alguns calculos
            if tupla_validacao:
                acuracia, erro = self.valida_rede(tupla_validacao)
            else:
                acuracia, erro = self.testa_rede()
                
            # Se usamos parada antecipada, entramos neste IF
            if parada == True and acuracia > acuraciaMax:
                acuraciaMax = acuracia
                melhores_pesos = self.guarda_peso()

            pes.write(str(cont) + ", " + str(acuracia)+ ", " + str(erro)+"\n")
            
            #Chama treinar epoca 
            acertos_treino = self.treina_Epoca(acertosEsperados)
            
            print(acertos_treino, acuracia, erro)

            # Condição de Parada
            if ((acertos_treino == acertosEsperados or cont == 500)):
               
                if parada == True:
                    self.ajusta_peso_rede(melhores_pesos)
                
                acuracia, acertos_testes, matriz, erro = self.testa_rede(matriz_conf=True)

                if parada == True:
                    acuracia = acuraciaMax
            
            # Prints da tela
                print("Acurácia =", acuracia, "| Acertos no conjunto de teste =", acertos_testes)
                print("Erro Quadrático Médio Com Conjunto de Teste =", erro)
                print("Matriz de Confusão")
                for elem in matriz:
                    print(elem)

                escreve_pesos(self,"pesos_finais/Pesos_Finais")            
                break

            #Caso passe de 200 épocas
            if cont == 200:
                print("Taxa de Aprendizagem incrementada em 0.1")
                self.taxaAprendizagem += 0.1

            cont += 1
        print("Interações totais = ",cont)

        return acuracia, erro
    
############################ CODIGOS PARA CONJUNTO DE VALIDAÇÃO ##########################################3
    # Caso haja dados de validação a validação usará esta função
    # Muito Similar a função de Testar Rede
    
    # validação é lista de lista 
    def valida_rede(self, validacao):
        #Separa a entrada, da saida esperada
        entrada_validacao = validacao[0]
        saida_validacao = validacao[1]

        #Acertos = max de acertos possiveis
        acertos = len(saida_validacao)

        valid = []
        
        #Cálcula acurácia para os dados de validação
        for x in range(0, len(saida_validacao)):

            resFeed = self.feedForward(x, entradaTreino = entrada_validacao[x])
            valid.append(resFeed)
            letra_da_rede = resFeed.index(max(resFeed))
            letra = saida_validacao[x].index(max(saida_validacao[x]))
            if letra != letra_da_rede:
                acertos -= 1

        erro_quadratico_medio = 0
        
        #Cálcula o erro quadratico médio
        for x in range(0, len(entrada_validacao)):
            for y in range (0,len(valid[x])):
                erro_quadratico_medio += ((saida_validacao[x][y]-valid[x][y])**2) 
                    
        erro_quadratico_medio = erro_quadratico_medio/len(entrada_validacao)


        return acertos/len(saida_validacao), erro_quadratico_medio

#################################### CODIGOS DA PARADA ANTECIPADA ##########################################3
    # Guarda os pesos que melhor se adaptaram aos dados de validação
    
    # Usado apenas na parada antecipada
    # Guarda os pesos da rede no seu "melhor momento"

    def guarda_peso(self):
        lista_pesos = []

        for neuronioInt in self.neuroniosInternos:
            
            temp = neuronioInt.pesos.copy()
            bias = neuronioInt.pesoBias
            temp.insert(0, bias)
            lista_pesos.append(temp)
            
        for neuronioSaida in self.neuroniosSaida:
            
            temp = neuronioSaida.pesos.copy()
            bias = neuronioSaida.pesoBias
            temp.insert(0, bias)
            lista_pesos.append(temp)

        return lista_pesos
    
    
    # Utilizado apenas na parada antecipada
    # Muda os Pesos para os melhores pesos
    def ajusta_peso_rede(self, melhores_pesos):

        for neuronioInt in self.neuroniosInternos:
            neuronioInt.pesobias = melhores_pesos[0][0] 
            neuronioInt.pesos = melhores_pesos[0][1:]
            melhores_pesos.pop(0)

        for neuronioSaida in self.neuroniosSaida:
            neuronioSaida.pesobias = melhores_pesos[0][0] 
            neuronioSaida.pesos = melhores_pesos[0][1:]
            melhores_pesos.pop(0)