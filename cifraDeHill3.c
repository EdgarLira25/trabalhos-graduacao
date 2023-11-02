#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

int nCol = 3;
int mod = 26;

int chave[3][3] = {{17, 17, 5},
                   {21, 18, 21},
                   {2, 2, 19}};

//int chave[3][3] = {{4, 9, 15},
//                   {15, 17, 6},
//                   {24, 0, 17}};
//int chave[2][2] = {{15,16},
//                   {8,9}};


void multiplicaMatrizes(int mat1[][nCol], int mat2[][nCol], int res[][nCol])
{
    int i, j, k;
    for (i = 0; i < nCol; i++)
    {
        for (j = 0; j < nCol; j++)
        {
            res[i][j] = 0;
            for (k = 0; k < nCol; k++)
            {   
                //printf("%d(%d %d)*%d(%d %d) + ", mat1[i][k], i, k,mat2[k][j], k, j);
                res[i][j] += mat1[i][k] * mat2[k][j];
            }
            //printf("|");
        }
        //printf("\n");
    }
}

int determinante(int n, int A[][n])
{
    if (n == 1)
    {
        return A[0][0];
    }
    else
    {
        int i, j, k;
        int det = 0, sinal = 1;
        int B[n - 1][n - 1];

        for (k = 0; k < n; k++)
        {
            for (i = 1; i < n; i++)
            {
                for (j = 0; j < n; j++)
                {
                    if (j != k)
                    {
                        B[i - 1][j - (j > k)] = A[i][j];
                    }
                }
            }
            det += sinal * A[0][k] * determinante(n - 1, B);
            sinal = -sinal;
        }
        return det;
    }
}
void obter_submatriz(int n, int i, int j, int A[][n], int B[][n - 1])
{
    int m, k;
    int linha, coluna;
    linha = coluna = 0;
    for (m = 0; m < n; m++)
    {
        if (m == i)
            continue;
        coluna = 0;
        for (k = 0; k < n; k++)
        {
            if (k == j)
                continue;
            B[linha][coluna] = A[m][k];
            coluna++;
        }
        linha++;
    }
}

void matriz_adjunta(int n, int A[][n], int adjA[][n])
{
    int i, j;
    int B[n - 1][n - 1];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            obter_submatriz(n, i, j, A, B);
            int det = determinante(n - 1, B);
            adjA[j][i] = pow(-1, i + j) * det;
        }
    }
}

void matriz_inversa(int n, int A[][n], int inv[][n])
{
}

int inversoMultiplicativo(int num, int mod)
{

    for (int x = 0; x < mod; x++)
    {
        if (((num)*x % mod) == 1)
        {
            return x;
        }
    }

    return num;
}

int inversoAditivo(int num, int mod)
{
    return num + mod;
}

void encriptar(char *mensagem)
{

    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    int tamMensagem = strlen(mensagem);
    int tamanho = 26;
    int mensagemNum[tamMensagem];
    printf("mensagem em numero\n");
    for (int i = 0; i < tamMensagem; i++)
    {
        char charAtual = mensagem[i];
        for (int j = 0; j < tamanho; j++)
        {
            if (charAtual == alfabeto[j])
            {
                mensagemNum[i] = j;
                printf("%d|", j);
                break;
            }
        }
        
    }
    printf("\n");
    int matrizMsg[3][3];
    int x = 0;
    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {
            matrizMsg[j][i] = mensagemNum[x];
            x = x + 1;
        }
    }

    printf("Matriz Mensagem\n");
    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {
            printf("%d|",matrizMsg[i][j]);
            
        }
        printf("\n");
    }

    int res[3][3];
    x = 0;
    multiplicaMatrizes(chave, matrizMsg, res);
    printf("Matriz resultante\n");
    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {
            printf("%d|",res[i][j]%26);
            
        }
        printf("\n");
    }

    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {

            mensagem[x] = toupper(alfabeto[res[j][i] % 26]);
            x = x + 1;
        }
    }

}

void decriptar(char *mensagemCrypto)
{
    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    int tamMensagem = strlen(mensagemCrypto);
    int tamanho = 26;
    int mensagemNum[tamMensagem];
    int inversa[3][3];
    int temp[2][2];
    int res[3][3];

    for (int x = 0; x < tamMensagem; x++)
    {

        mensagemCrypto[x] = tolower(mensagemCrypto[x]);
    }

    for (int i = 0; i < tamMensagem; i++)
    {
        char charAtual = mensagemCrypto[i];
        for (int j = 0; j < tamanho; j++)
        {
            if (charAtual == alfabeto[j])
            {
                mensagemNum[i] = j;
                break;
            }
        }
    }
    int matrizMsgCrypto[3][3];
    int x = 0;
    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {
            matrizMsgCrypto[j][i] = mensagemNum[x];
            x = x + 1;
        }
    }

    int detMatrizKey = determinante(nCol, chave) % mod;

    if (detMatrizKey < 0)
    {
        detMatrizKey = inversoAditivo(detMatrizKey, mod);
    }

    detMatrizKey = inversoMultiplicativo(detMatrizKey, mod);
    
    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {

            obter_submatriz(nCol, j, i, chave, temp);
            
            int det = determinante(2, temp) % mod;
            det = det * pow(-1, i + j);

            if (det < 0)
            {
                det = inversoAditivo(det, mod);
            }
            inversa[i][j] = (detMatrizKey * det) % mod;
        }
    }
    
    multiplicaMatrizes(inversa, matrizMsgCrypto, res);
    x = 0;
    for (int i = 0; i < nCol; i++)
    {
        for (int j = 0; j < nCol; j++)
        {

            mensagemCrypto[x] = alfabeto[res[j][i] % 26];
            x = x + 1;
        }
    }
}

char *pegaString()
{
    char *nome = NULL;
    size_t tamanhoStr = 0;

    getline(&nome, &tamanhoStr, stdin);

    if (nome[strlen(nome) - 1] == '\n')
    {
        nome[strlen(nome) - 1] = '\0';
    }

    return nome;
}

void geraKey(){
    extern int chave[3][3];
    srand(time(NULL));
    for (int i = 0; i < nCol; i++)
        for (int j = 0; j<nCol;j++)
            chave[i][j] = rand() % 200;
}

int main()
{
    char *mensagem = pegaString();
    //char *mensagem = "valdineiz";
    
    encriptar(mensagem);
    printf("%s\n", mensagem);
    decriptar(mensagem);
    printf("%s\n", mensagem);

    return 0;
}