#include <stdio.h>
#include <stdlib.h>

typedef int TIPOCHAVE;

typedef struct estrutura{   
TIPOCHAVE chave;
struct estrutura *prox;
} NO;

typedef struct {
    NO *inicio;
    NO *fim;

} FILA;

void inicializarFila(FILA *f){

    f->inicio = NULL;
    f->fim = NULL;

}

void insereFila(FILA *f, TIPOCHAVE ch){

    NO* novo = (NO*) malloc(sizeof(NO));
        novo->chave = ch;
        novo->prox = NULL;
    if (f->inicio == NULL && f->fim == NULL){
        f->fim = novo;
        f->inicio = novo;
    } else {
        f->fim->prox = novo;
        f->fim = novo;
    } 
}
void exibirLista(FILA f){
    NO* p = f.inicio;
    while(p){
        printf("%d\n", p->chave);
        p = p->prox;

    }
}

void removeFila(FILA *f){

    NO *p = f->inicio;
    f->inicio = p->prox;
    free(p);

}

void tamanhoFila(FILA *f){
    NO* p = f->inicio;
    int i = 0;
    while(p){
        i++;
        p = p->prox;

    }
   printf("Tamanho fila: %d\n", i);
}

int main (){

    FILA fila;
    inicializarFila(&fila);
    insereFila(&fila, 15);
    insereFila(&fila, 25);
    insereFila(&fila, 55);
    insereFila(&fila, 75);
    insereFila(&fila, 5);
    insereFila(&fila, 2);
    tamanhoFila(&fila);
    exibirLista(fila);
    removeFila(&fila);
    removeFila(&fila);
    removeFila(&fila);
     removeFila(&fila);
    removeFila(&fila);
    
    printf("\n");
    exibirLista(fila);


    return 0;
}