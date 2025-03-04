#include <stdio.h>
#include <stdlib.h>

typedef int TIPOCHAVE;

typedef struct estrutura{   
    
TIPOCHAVE chave;

struct estrutura *prox;
} NO;

typedef struct {
    NO *topo;
   
} PILHA;

void inicializarPilha(PILHA *p){
    p->topo = NULL;
}

void push(PILHA *p, TIPOCHAVE ch){

    NO* novo = (NO*) malloc(sizeof(NO));
    novo->chave = ch;
    novo->prox = NULL;
    if (p->topo == NULL){
        p->topo = novo;
    } else {
        novo->prox = p->topo;
        p->topo = novo;
    }

}
void pop(PILHA *p){
    NO *x = p->topo;
    p->topo = x->prox;
    free(x);
    
}

void imprimirPilha(PILHA p){
    NO* x = p.topo;
    while(x){
        printf("%d\n", x->chave);
        x = x->prox;
    }
}
void tamanho(PILHA *p){
    NO* x = p->topo;
    int i = 0;

    while(x){
        i++;
        x = x->prox;
    }
    printf("Tamanho: %d\n", i);

}

