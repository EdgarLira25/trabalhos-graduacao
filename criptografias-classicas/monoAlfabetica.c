#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include "auxiliares/listaAux.c"

char chave[26];
char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";

char *encripta(char *mensagem)
{

    int tamanho = 26;
    int tamMensagem = strlen(mensagem);

    for (int z = 0; z < tamMensagem; z++)
    {
        char charAtual = mensagem[z];
        for (int k = 0; k < tamanho; k++)
        {
            if (charAtual == alfabeto[k])
            {
                mensagem[z] = chave[k];
            }
        }
    }

    return mensagem;
}

char *decripta(char *mensagemCrypto)
{

    int tamanho = 26;

    int tamMensagem = strlen(mensagemCrypto);

    for (int z = 0; z < tamMensagem; z++)
    {
        char charAtual = mensagemCrypto[z];
        for (int k = 0; k < tamanho; k++)
        {
            if (charAtual == chave[k])
            {
                mensagemCrypto[z] = alfabeto[k];
            }
        }
    }

    return mensagemCrypto;
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

void criaChave()
{
    extern char chave[26];
    int tamanho = 26;

    LISTA lista = inicializar();

    strcpy(chave, alfabeto);
    srand(time(NULL));
    for (int i = 0; i < tamanho; i++)
    {
        chave[i] = toupper(chave[i]);
    }
    for (int i = 0; i < tamanho - 1; i++)
    {

        int j = rand() % tamanho;
        while (buscaChave(lista, j) == 1)
        {
            j = rand() % tamanho;
        }
        inserir(&lista,j);
        char temp = chave[j];
        chave[j] = chave[i];
        chave[i] = temp;
    }

    return;
}

int main()
{
    criaChave();

    char *nome = pegaString();
    encripta(nome);
    printf("Chave Encriptada : %s\n", nome);
    decripta(nome);
    printf("Chave Descriptada: %s\n", nome);
    free(nome);

    return 0;
}