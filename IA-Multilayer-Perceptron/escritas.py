import os

# Verifica se tem muitos arquivos e apaga se chegou a 7
def verificador(string_base):
    if os.path.exists("saidas/"+ string_base + str(7)+ ".txt"):
        for x in range (1,8):
            os.remove("saidas/"+ string_base + str(x)+ ".txt")


def escreve_saidas_testes(self, string_base, saidas, saidas_esperadas):
    
    verificador(string_base)
    
    
    
    for x in range (1,8):
        caminho_arquivo = "saidas/saidas_testes/"+ string_base + str(x)+ ".txt"

        if os.path.exists(caminho_arquivo):
        
            pass
        else:
            alfabeto = "ABCDEJK"

            pes = open("saidas/saidas_testes/"+ string_base + str(x)+ ".txt", "w")
            pes.write( "Letra Certa, Letra Predita, Saida da Rede\n" )
                
            for x in range(0,len(saidas)):
                letra_da_rede = saidas[x].index(max(saidas[x]))
                letra = saidas_esperadas[x].index(max(saidas_esperadas[x]))
                pes.write(alfabeto[letra]+ ", " + alfabeto[letra_da_rede] + ", ")
                pes.write(str(saidas[x])+"\n")
            return

def escreve_pesos(self, string_base):

    verificador(string_base)

    for x in range (1,8):
        caminho_arquivo = "saidas/"+ string_base + str(x)+ ".txt"
        if os.path.exists(caminho_arquivo):
            pass
        else:
            pes = open("saidas/"+ string_base + str(x)+ ".txt", "w")
            for neuronioInt in self.neuroniosInternos:
                neuronioInterno_temp = neuronioInt.pesos.copy()
                bias = neuronioInt.pesoBias
                neuronioInterno_temp.insert(0,bias)
                pes.write(str(neuronioInterno_temp))
                pes.write("\n")

            for neuronioSaida in self.neuroniosSaida:
                neuronioSaida_temp = neuronioSaida.pesos.copy()
                bias = neuronioSaida.pesoBias
                neuronioSaida_temp.insert(0,bias)
                pes.write(str(neuronioSaida_temp))
                pes.write("\n")
                
            return

def escreve_hiperparametros(self, string_base):

    verificador(string_base)
    
    for x in range (1,8):
        caminho_arquivo = "saidas/"+ string_base + str(x)+ ".txt"
        if os.path.exists(caminho_arquivo):
            pass
        else:
            pes = open("saidas/"+ string_base + str(x)+ ".txt", "w")
            pes.write("Taxa de Aprendizagem = " + str(self.taxaAprendizagem))
            pes.write("\n")
            pes.write("Número de neurônios na camada de entradas = " + str(self.num_entradas))
            pes.write("\n")
            pes.write("Número de neurônios na camada escondida = " + str(self.num_internos))
            pes.write("\n")
            pes.write("Número de neurônios na camada de saida = " + str(self.num_saida))
            pes.write("\n")
            pes.write("Função de ativação = Tangente Hiperbólica")
            pes.write("\n")

            return

def escrita_erro(self, string_base):
        
    verificador(string_base)

    for x in range (1,8):
        caminho_arquivo = "saidas/"+ string_base + str(x)+ ".txt"
        if os.path.exists(caminho_arquivo):
            pass
        else:
            return open("saidas/"+ string_base + str(x)+ ".txt", "w")