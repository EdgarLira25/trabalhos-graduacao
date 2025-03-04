#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *encripta(char *mensagem)
{
    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    char alfabetoCrypto[26] = "DEFGHIJKLMNOPQRSTUVWXYZABC";
    int tamanho = 26;

    int tamMensagem = strlen(mensagem);

    for (int z = 0; z < tamMensagem; z++)
    {
        char charAtual = mensagem[z];
        for (int k = 0; k < tamanho; k++)
        {
            if (charAtual == alfabeto[k])
            {
                mensagem[z] = alfabetoCrypto[k];
            }
        }
    }

    return mensagem;
}

char *decripta(char *mensagemCrypto)
{

    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    char alfabetoCrypto[26] = "DEFGHIJKLMNOPQRSTUVWXYZABC";
    int tamanho = 26;

    int tamMensagem = strlen(mensagemCrypto);

    for (int z = 0; z < tamMensagem; z++)
    {
        char charAtual = mensagemCrypto[z];
        for (int k = 0; k < tamanho; k++)
        {
            if (charAtual == alfabetoCrypto[k])
            {
                mensagemCrypto[z] = alfabeto[k];
            }
        }
    }

    return mensagemCrypto;
}

char *pegaString(){
    char *nome = NULL;
    size_t tamanhoStr = 0;

    getline(&nome, &tamanhoStr, stdin);

    if (nome[strlen(nome) - 1] == '\n')
    {
        nome[strlen(nome) - 1] = '\0';
    }

    return nome;
}

int main()
{

    char* nome = pegaString();
    
    encripta(nome);

    printf("%s\n", nome);

    decripta(nome);

    printf("%s\n", nome);

    free(nome);

    return 0;
}