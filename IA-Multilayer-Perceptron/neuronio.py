import auxiliares.funcoes_ativacao as funcoes_ativacao
import random

class Neuronio:
    def __init__(self, number):
        
        #Só pra identificar o neurônio
        self.number = number
        
        #Bias
        self.bias = 1
        
        #Peso do Bias
        self.pesoBias = random.uniform(-0.5, 0.5)
        #self.pesoBias = 1
        
        #Lista de Pesos
        self.pesos = []

        #Lista de ajustes, olhar calc_ajustesDePesos e salvarNovosPesos para entender
        self.ajusteDePeso = []

        #Termo de Erro geral
        self.termoErro = None

        #Saida antes de passsar pela função de ativação
        self.saida = None
        
        #Saida após passar pela função de ativação
        self.saidaAtivada = None
        
        #Entradas
        self.entradas = []

    # Inicializa Pesos
    def inicia_pesos(self, num_pesos):
        for x in range(num_pesos):
            self.pesos.append(random.uniform(-0.5, 0.5))
        
    #Calcula saida e saida depois que passa pela função de ativação,
    #Guarda também a saida antes de passar pela função de ativação
    def calc_saida(self):

        saidaX = self.bias*self.pesoBias
        
        for indice in range(0,len(self.entradas)):
            
            saidaX += self.entradas[indice]*self.pesos[indice]

        self.saida = saidaX
        self.saidaAtivada = funcoes_ativacao.tanHip(self.saida)

        return self.saidaAtivada

    # Calcula os ajustes de peso que a rede vai fazer
    def calc_ajustesDePesos(self, taxaAprendizagem):
        
        ajustes = []
        for entrada in self.entradas:
            ajustes.append(taxaAprendizagem*self.termoErro*entrada)
        
        self.ajusteDePeso = ajustes

        self.pesoBias = self.pesoBias + self.termoErro*taxaAprendizagem

    # Aplica os ajustes de pesos calculados previamente
   
    def salvarNovosPesos(self):
        for indice in range(len(self.pesos)):
            self.pesos[indice] = self.pesos[indice] + self.ajusteDePeso[indice]
            
class NeuronioEscondido(Neuronio):
    # Termo de Erro do neuronio escondido
    def calc_termoErro(self, neuroniosProxCamada):

        termoErroTemp = 0  
        for neuronioOut in neuroniosProxCamada:
            termoErroTemp += neuronioOut.termoErro * neuronioOut.pesos[self.number]

        self.termoErro = termoErroTemp*funcoes_ativacao.der_tanHip(self.saida)
        
class NeuronioDeSaida(Neuronio):
    # Termo de Erro neuronio de saida
    def calc_termoErro(self, saida_esperada, saida_atual):
        
        self.termoErro = (saida_esperada[self.number] - saida_atual[self.number])*funcoes_ativacao.der_tanHip(self.saida)