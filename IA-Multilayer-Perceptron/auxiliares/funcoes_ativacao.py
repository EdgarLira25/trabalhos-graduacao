from math import e

# Função Hiperbólica
def tanHip(x):
    return  (e**(2*x) - 1)/(e**(2*x) + 1)

# Derivada da Função Hiperbólica
def der_tanHip(x):
    return 1/(((e**x + e**(-x))/2)*(e**x + e**(-x))/2)