#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef int TIPOCHAVE;
typedef enum {esq, dir} LADO;

typedef struct estrutura {
TIPOCHAVE chave;
struct estrutura *esq;
struct estrutura *dir;
} NO;

void inicializarArvore(NO* *raiz){
    *raiz = NULL;
}

bool arvoreVazia(NO* raiz){

    if (!raiz){
        return true;
    } else {
        return false;
    }

}

void visita(NO *x){

  printf("%d ", x->chave);
    
}

void preOrdem(NO* p){
    
    if(p){

        visita(p);
        preOrdem(p->esq);
        preOrdem(p->dir);

    }
}

void posOrdem(NO* p){

    if (p){
    
        posOrdem(p->esq);
        posOrdem(p->dir);
        visita(p);
    
    }
}

void emOrdem(NO* p){

    if (p){

        emOrdem(p->esq);
        visita(p);
        emOrdem(p->dir);
    }
}

void destruirArvore(NO* *p){

    if(*p){
        
        destruirArvore(&(*p)->esq);
        destruirArvore(&(*p)->dir);
        free(*p);
    }

    *p=NULL;
}

NO* BuscaNO(NO *raiz, TIPOCHAVE ch){

    NO *atual = raiz;
    bool achou = false;

    while (achou == false){

            if (ch == atual->chave){
                achou = true;
            }

            else if (ch < atual->chave && atual->esq != NULL && achou == false){
                atual = atual->esq;
            }

           else  if (ch > atual->chave && atual->dir != NULL && achou == false){
                atual = atual->dir;
            }
           
           else if (atual->esq == NULL && atual->dir == NULL && achou == false){
                printf("NO nao encontrado\n");
                return NULL;
            }

    }

    return atual;
}



void inserirNO(NO* *raiz, TIPOCHAVE ch){

    NO* novo = (NO*) malloc(sizeof(NO));
    novo->chave = ch;
    novo->esq = NULL;
    novo->dir = NULL;

    NO *atual = *raiz;
    
    bool lugInsere = false;

    if (*raiz == NULL){

        *raiz = novo;

    } else {

        while (lugInsere == false){

            if (ch < atual->chave && atual->esq != NULL){

                atual = atual->esq;

            }
            else{
                lugInsere = true;
            }

            if (ch > atual->chave && atual->dir != NULL){

                atual = atual->dir;

            } else {
                lugInsere = true;
            }
        }
        if (ch < atual->chave){
            atual->esq = novo;
           
        }
        else{
            atual->dir = novo;
           
        }
    }
}

/*
    REMOÇÂO INCOMPLETA
void removeNO(NO *raiz, TIPOCHAVE ch){

    NO* atual = BuscaNO(raiz, ch);

    if (atual->esq == NULL && atual->dir == NULL){

        free(atual);
        
    } else {
       
        NO* antRaiz = atual->esq;

        while(antRaiz->dir != NULL){
          
           
            antRaiz = antRaiz->dir;

        }
        
        
        antRaiz->dir = atual->dir;
        antRaiz->esq = atual->esq;
        
        free(atual);
        return raiz;
    }
}
*/
