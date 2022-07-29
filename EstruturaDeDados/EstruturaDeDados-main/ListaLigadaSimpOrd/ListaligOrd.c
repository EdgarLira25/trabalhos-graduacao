#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef int TIPOCHAVE;
#define MAX 50

//Estrutura Registro
typedef struct {
 TIPOCHAVE chave;
} REGISTRO;

//Estrutura Lista
    typedef struct {
 
 REGISTRO A[MAX];
 int nroElem;
} LISTA;

void iniciaLista(LISTA *l){
    l->nroElem = 0;
}

void veTamanho(LISTA l){    
    printf("Tamanho = %d\n", l.nroElem);
}

void insere(LISTA *l, TIPOCHAVE ch){
    
    if (l->nroElem == 0){
        l->A[0].chave = ch;
    }
    else{
        for(int i = l->nroElem; i >= 0;i--){ 
            l->A[i+1].chave = l->A[i].chave;
            
            if (ch < l->A[i].chave){
               
                l->A[i].chave = ch;
                break;
            }
        }
    }
    
    l->nroElem++;

}

void imprimeLista(LISTA *l){
    for (int i = 0; i < l->nroElem; i++){
        printf("Posicao %d = %d\n",i, l->A[i].chave);
    }
}

void primeiro(LISTA *l){
    printf("Primeiro Elemento lista = %d\n", l->A[0].chave);

}

void ultimo(LISTA *l){
    
    printf("Ultimo Elemento lista = %d\n", l->A[l->nroElem-1].chave);

}

void destruir(LISTA *l){
    l->nroElem = 0;
}

int posicao(LISTA *l, int n){

return l->A[n].chave;

}

bool inserirElemListaSeq(TIPOCHAVE ch, int pos, LISTA *l){
    for (int i = 0; i < l->nroElem; i++){
        if (ch == l->A[i].chave){
            return false;
        }
    }
    for (int i = l->nroElem; i > pos; i-- ){

        l->A[i+1].chave = l->A[i].chave;     
    
    }
    l->A[pos].chave = ch;
    l->nroElem++;
    return true;
}

int buscaSeq(TIPOCHAVE ch, LISTA l){
    for (int i = 0; i < l.nroElem; i++){
        if (ch == l.A[i].chave){
            return i;
        }
    }
    return -1;
}

bool removeElem(TIPOCHAVE ch, LISTA *l){

    for (int i = 0; i < l->nroElem; i++){
        if (ch == l->A[i].chave){
            l->nroElem--;
            for (int j = i; j < l->nroElem; j++){
                l->A[j].chave = l->A[j+1].chave;
            }
            return true;
        }   
    }
    return false;
}

int main(void){
 
    LISTA teste;

    iniciaLista(&teste);
    
    insere(&teste, 55);
    insere(&teste, 15);
    insere(&teste, 25);
    veTamanho(teste);
    imprimeLista(&teste);
    removeElem(15, &teste); 
      imprimeLista(&teste);
/*    primeiro(&teste);    
    ultimo(&teste);
    destruir(&teste);
    veTamanho(teste);
*/
    return 0;

}
