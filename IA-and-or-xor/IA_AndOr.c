#include <stdio.h>
#include <stdlib.h>

double taxaAprendizagem = 0.1;
int interacoes = 4;
double bias = 1;
double pesoBias = 0;

void mudarPesos(double *pesos, double saida_esperada, double resultado, double entrada1, double entrada2){
    
    extern double pesoBias;
    double altBias = taxaAprendizagem * 1 * saida_esperada;
    pesoBias = pesoBias + altBias;

    double alt1 = (taxaAprendizagem * entrada1 * saida_esperada);
    pesos[0] = pesos[0] + alt1;

    double alt2 = (taxaAprendizagem * entrada2 * saida_esperada);
    pesos[1] = pesos[1] + alt2;

}

double funcaoDeAtivacao(double entrada1, double entrada2, double *pesos)
{

    double resultado = entrada1 * pesos[0] + entrada2 * pesos[1] + bias * pesoBias;

    if (resultado >= 0)
        return 1;
    else
        return -1;
}

void funcaoDeTreinamento(double entradas[][2], double *saidas, double *pesos, double *resultados)
{

    for (int i = 0; i < 4; i++)
    {

        double entrada1 = entradas[i][0];
        double entrada2 = entradas[i][1];
        resultados[i] = funcaoDeAtivacao(entrada1, entrada2, pesos);

        if (saidas[i] != resultados[i])
        {

            mudarPesos(pesos, saidas[i], resultados[i], entrada1, entrada2);

        }
    }
}

int main()
{
    // ### OR ###//
    double entradas[4][2] = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
    double saidas_esperadas[4] = {-1, 1, 1, 1};

    // ### AND ###//
    // double entradas[4][2] = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
    // double saidas_esperadas[4] = {-1, -1, -1, 1};

    double pesos[2] = {4, 4};
    int acertos;
    double saidasatuais[4] = {100, 100, 100, 100};
    int epocas = 0;
    while (1)
    {

        funcaoDeTreinamento(entradas, saidas_esperadas, pesos, saidasatuais);

        acertos = 0;
        for (int i = 0; i < 4; i++)
        {
            if (saidas_esperadas[i] == saidasatuais[i])
            {
                acertos++;
            }
        }

        if (acertos == 4)
        {
            break;
        }
        
    }

    printf("\n");

    for (int x = 0; x < 4; x++)
    {
        printf("Saida = %.0lf | Saida Esperada = %.0lf\n", saidasatuais[x], saidas_esperadas[x]);
    }

    printf("Peso 1 = %.2lf | Peso 2 = %.2lf | Peso Bias = %.2lf \n\n", pesos[0], pesos[1], pesoBias);

    printf("epocas %d\n", epocas);
    return 0;
}