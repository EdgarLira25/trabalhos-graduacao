#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

int chave[2];
int mod = 26;
int tamanhoAlfabeto = 26;

void encripta(char *mensagem){
    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    int tamMensagem = strlen(mensagem);
    for (int i = 0; i < tamMensagem; i++){
        for (int j = 0; j < tamanhoAlfabeto; j++){
            if (mensagem[i] == alfabeto[j]){
                int total = (chave[0]*j + chave[1]) % mod;
                //printf("letra %c | (3*%d + %d)mod%d = %d | Letra = %c\n",mensagem[i], chave[0], chave[1], mod, total, alfabeto[total]);
                mensagem[i] = toupper(alfabeto[total]);
                break;
            }
        }
    }

}
int inversoAditivo(int num){
    return num + mod;
}
int inversoMultiplicativo(int num){
    if (num < 0){
        num = -num;
    }
    for (int x = 0; x < mod; x++){
        if (((num)*x % mod) == 1){
            return x;
        } 
    }

    return num; 
}

void decripta(char *mensagemCrypto){
    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    
    int tamMensagem = strlen(mensagemCrypto);
    for (int i = 0; i < tamMensagem; i++){
        for (int j = 0; j < tamanhoAlfabeto; j++){
            if (tolower(mensagemCrypto[i]) == alfabeto[j]){
                int total = ((j+inversoAditivo(-chave[1]))*inversoMultiplicativo(chave[0])) % mod;
                //printf("letra %c | (%d + %d)*%d mod %d = %d | Letra = %c\n",mensagemCrypto[i],j, inversoAditivo(-chave[1]),inversoMultiplicativo(chave[0]), mod, total, alfabeto[total]);
                mensagemCrypto[i] = tolower(alfabeto[total]);
                break;
            }
        }
    }
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

void criaChave(){

    extern int chave[2];
    srand(time(NULL));
    //chave[0] = rand() % 12;
    //chave[1] = rand() % 26;
    chave[0] = 3;
    chave[1] = 5;

}

int main(){

    char *nome = pegaString();
    criaChave();
    encripta(nome);
    printf("%s\n", nome);
    decripta(nome);
    printf("%s\n", nome);

    return 0;
}