from passo1 import passo1
from passo2 import passo2
from passo3 import passo3
import time

if __name__ == "__main__":

    # Passo 1 Duração = 10.06 Segundos
    # Passo 2 Duração = 684.05 Segundos
    # Passo 3 Duração = 0.09 Segundos

    inicio = time.time()
    passo1()
    fim1 = time.time()
    print("Passo 1 Duração =", round(fim1-inicio, 2),"Segundos")

    passo2()
    fim2 = time.time()
    print("Passo 2 Duração =", round(fim2-fim1,2), "Segundos")

    passo3()
    fim3 = time.time()
    print("Passo 3 Duração =", round(fim3-fim2,2),"Segundos")
