#include <stdio.h>
#include <stdlib.h>

typedef int TIPOCHAVE;

typedef struct estrutura{   
TIPOCHAVE chave;
struct estrutura *prox;
struct estrutura *ant;
} NO;

typedef struct {
    NO *inicio1;
    NO *inicio2;

} DEQUE;

void inicializarDeque(DEQUE *d){

    d->inicio1 = NULL;
    d->inicio2 = NULL;

}

void inserir1(DEQUE *d, TIPOCHAVE ch){

    NO* novo = (NO*) malloc(sizeof(NO));
    
    novo->chave=ch;
    if (d->inicio1 == NULL && d->inicio2 == NULL){
        novo->ant = NULL;
        novo->prox = NULL;
        d->inicio1 = novo;
        d->inicio2 = novo;
    } else {
        novo->ant = NULL;
        d->inicio1->ant = novo;
        novo->prox = d->inicio1;
        d->inicio1 = novo;

    }
}

void inserir2(DEQUE *d, TIPOCHAVE ch){

    NO* novo = (NO*) malloc(sizeof(NO));
    
    novo->chave=ch;
    
    if (d->inicio1 == NULL && d->inicio2 == NULL){
        novo->ant = NULL;
        novo->prox = NULL;
        d->inicio1 = novo;
        d->inicio2 = novo;
    } else {
        novo->prox = NULL;
        d->inicio2->prox = novo;
        novo->ant = d->inicio2;
        d->inicio2 = novo;
    }
}

void remover1(DEQUE *d){
    NO* p = d->inicio1;
    d->inicio1 = p->prox;
    d->inicio1->ant = NULL;
    free(p);
}

void remover2(DEQUE *d){
    NO* p = d->inicio2;
    d->inicio2 = p->ant;
    d->inicio2->prox = NULL;
    free(p);
}

void exibirlista1(DEQUE d){
   
    NO* p = d.inicio1;
    while (p){
        printf("%d ", p->chave);
        p = p->prox;
    }
    printf("\n");
}

void exibirlista2(DEQUE d){
   
    NO* p = d.inicio2;
    while (p){
        printf("%d ", p->chave);
        p = p->ant;
    }
    printf("\n");
}

void destruirDeque(DEQUE *d){

    NO* p = d->inicio1;
    NO* temp;
    while (p){
        temp = p->prox;
        free(p);
        p = temp;
    }
    d->inicio1 = d->inicio2 = NULL;
}
