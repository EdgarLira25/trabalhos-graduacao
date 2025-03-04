import numpy as np
from keras.callbacks import Callback
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import random

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

def escreve_erro(history):
    interccao = 0
    with open("saidas/erro_por_interação.txt", "w") as pes:
        pes.write("Interacao, Erro Quadratico Medio\n")
        for loss in history.losses:
            pes.write(str(interccao) + ", "+ str(loss) + "\n")
            interccao += 1

def escreve_hiperparametros(epocas,batch):
    with open("saidas/hiperparametros.txt", "w") as hiper:
        hiper.write("Epocas = "+str(epocas)+"\n")
        hiper.write("Batch_size = "+str(batch)+"\n")
        hiper.write("Chamando o Modelo:\n" + "model.fit(x_train, y_train, epochs=epocas, batch_size=batch, validation_data=(x_test, y_test), callbacks=[history])"+"\n")

def escreve_saidas(y_pred, y_test):
    
    y_pred = y_pred.tolist()
    y_test = y_test.tolist()

    with open("saidas/saidas_rede.txt", "w") as tes:
        tes.write("Saida_predita, Saida_verdadeira\n")
        for x in range (0,len(y_pred)):
            tes.write(str(y_pred[x])+", "+str(y_test[x])+"\n")
  
def modelo_base():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    print( model.output_shape)
    model.add(MaxPooling2D((2, 2)))
    print( model.output_shape)
    model.add(Conv2D(64, (3, 3), activation='relu'))
    print( model.output_shape)
    model.add(MaxPooling2D((2, 2)))
    print( model.output_shape)
    model.add(Conv2D(64, (3, 3), activation='relu'))
    print( model.output_shape)
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    print(model.output_shape)
    return model
if __name__ == "__main__":
    
    # Carregando o conjunto de dados MNIST
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    num_saidas = 10

    # Pergunta se deseja treinar o modelo com 2 números
    print("#"*20)
    if input("\nDigite 0 e pressione enter se deseja treinar apenas com 2 digítos, \ncaso deseje treinar com os 10 dígitos apenas aperte enter:\n") == "0":
        
        num0 = random.randint(0,9)
        num1 = random.randint(0,9)
        
        while num0 == num1:
            num1 = random.randint(0,9)
        
        if num0 > num1:
            num_saidas = num0 + 1
        else:
            num_saidas = num1 + 1
        print("Primeiro número selecionado: " , num0)
        print("Segundo número selecionado: " , num1)

        train_filter = np.where((y_train == num0) | (y_train == num1))
        test_filter = np.where((y_test == num0) | (y_test == num1))
        x_train, y_train = x_train[train_filter], y_train[train_filter]
        x_test, y_test = x_test[test_filter], y_test[test_filter]
    else: 
        pass
    
    # Pré-processamento dos dados
    x_train = np.expand_dims(x_train, axis=-1)  # Adicionando uma dimensão para canais de cor (1 canal, pois as imagens são em escala de cinza)
    x_test = np.expand_dims(x_test, axis=-1)
    y_train = to_categorical(y_train)  # Convertendo rótulos para one-hot encoding
    y_test = to_categorical(y_test)

    # Definindo a arquitetura da CNN
    model = modelo_base()
    model.add(Dense(num_saidas, activation='softmax'))  
    print(model.output_shape)

    # Guarda os Erros
    history = LossHistory()
    
    # Compilando o modelo
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])    
    
    #Salva Pesos Iniciais
    model.save_weights('saidas/pesos_iniciais_modelo.h5')

    # Hiperparametros do modelo
    epocas = 5
    batch = 200
    # Escreve os txt dos HiperParametros
    escreve_hiperparametros(epocas,batch)
    # Treinando a CNN
    model.fit(x_train, y_train, epochs=epocas, batch_size=batch, validation_data=(x_test, y_test), callbacks=[history])

    # Avaliando o desempenho do modelo
    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

    # Obtendo as previsões do modelo para os dados de teste
    y_pred = model.predict(x_test)
    
    # Convertendo as previsões em rótulos numéricos
    y_pred = np.argmax(y_pred, axis=1)  
    y_test = np.argmax(y_test, axis=1)
    
    # Cria a matriz de confusão
    cm = confusion_matrix(y_test , y_pred)
    print("Matriz de Confusão:")
    print(cm)

    # Escreve os Pesos
    model.save_weights('saidas/pesos_finais_modelo.h5')

    # Escreve as Saidas
    escreve_saidas(y_pred, y_test)
    
    # Escreve o Erro por Interação
    escreve_erro(history)