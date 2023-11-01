#include <stdio.h>
#include <stdlib.h>

double taxaAprendizagem = 0.1;
int interacoes = 4;
double bias = 1;
double pesoBias = 0;

void mudarPesos(double *pesos, double saida_esperada, double resultado, double entrada1, double entrada2)
{

    if (resultado == 1 && saida_esperada == -1)
    {
        extern double pesoBias;
        double altBias = taxaAprendizagem * 1 * saida_esperada;

        if (altBias > 0)
        {
            altBias = -altBias;
        }

        pesoBias = pesoBias + altBias;

        if (entrada1 == 1)
        {
            double alt = (taxaAprendizagem * entrada1 * saida_esperada);

            if (alt > 0)
            {
                alt = -alt;
            }

            pesos[0] = pesos[0] + alt;
        }
        else if (entrada1 == -1)
        {
            double alt = (taxaAprendizagem * entrada1 * saida_esperada);

            if (alt < 0)
            {
                alt = -alt;
            }

            pesos[0] = pesos[0] + alt;
        }
        if (entrada2 == 1)
        {
            double alt = (taxaAprendizagem * entrada2 * saida_esperada);

            if (alt > 0)
            {
                alt = -alt;
            }

            pesos[1] = pesos[1] + alt;
        }
        else if (entrada2 == -1)
        {
            double alt = (taxaAprendizagem * entrada2 * saida_esperada);

            if (alt < 0)
            {
                alt = -alt;
            }

            pesos[1] = pesos[1] + alt;
        }
    }
    else if (resultado == -1 && saida_esperada == 1)
    {
        extern double pesoBias;
        double altBias = taxaAprendizagem * 1 * saida_esperada;

        if (altBias < 0)
        {
            altBias = -altBias;
        }

        pesoBias = pesoBias + altBias;

        if (entrada1 == 1)
        {
            double alt = (taxaAprendizagem * entrada1 * saida_esperada);

            if (alt < 0)
            {
                alt = -alt;
            }

            pesos[0] = pesos[0] + alt;
        }
        else if (entrada1 == -1)
        {
            double alt = (taxaAprendizagem * entrada1 * saida_esperada);

            if (alt > 0)
            {
                alt = -alt;
            }

            pesos[0] = pesos[0] + alt;
        }
        if (entrada2 == 1)
        {
            double alt = (taxaAprendizagem * entrada2 * saida_esperada);

            if (alt < 0)
            {
                alt = -alt;
            }

            pesos[1] = pesos[1] + alt;
        }
        else if (entrada2 == -1)
        {
            double alt = (taxaAprendizagem * entrada2 * saida_esperada);

            if (alt > 0)
            {
                alt = -alt;
            }

            pesos[1] = pesos[1] + alt;
        }
    }
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
    // ### XOR ###//
    double entradas[4][2] = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
    double saidas_esperadas[4] = {-1, 1, 1, -1};
    double pesos[2] = {0, 0};
    int acertos;
    double saidasatuais[4] = {100, 100, 100, 100};


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
        printf("Saida = %lf | Saida Esperada = %lf\n", saidasatuais[x], saidas_esperadas[x]);
    }

    printf("Peso 1 = %lf, Peso 2 = %lf, Peso Bias = %lf \n\n", pesos[0], pesos[1], pesoBias);

    return 0;
}