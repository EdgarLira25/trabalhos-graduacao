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

bool inserirNo(NO* *raiz, NO *pai, TIPOCHAVE ch, LADO pos){

    NO* novo = (NO*) malloc(sizeof(NO));
    novo->chave = ch;
    novo->esq = NULL;
    novo->dir = NULL;

    
    if(pai){
        if(((pos==esq) && (pai->esq!=NULL))||((pos==dir) && (pai->dir!=NULL))){
            return false;
        }
    }

    if(pai == NULL){
        *raiz = novo;
        return true;

    } else {
        if(pos==esq){
            pai->esq = novo;
            return true;
        }
        if(pos == dir){
            pai->dir = novo;
            return true;
        }
    }


}

// printando arvore
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
