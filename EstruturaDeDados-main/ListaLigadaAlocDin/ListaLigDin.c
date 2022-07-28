#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

typedef int TIPOCHAVE;

typedef struct estrutura{

    TIPOCHAVE chave;
    struct estrutura *prox;

} NO;

typedef struct {

NO *inicio;
int tam;   

}LISTA;

void inicializar(LISTA *l){
    l->inicio = NULL;
    l->tam=0;
}

void exibirLista(LISTA l){

    NO* p = l.inicio;
    while(p){

        printf("%d\n", p->chave);
        p = p->prox;
    }
}

void inserir(LISTA *l, TIPOCHAVE ch){
    NO* novo = (NO*) malloc(sizeof(NO));
    NO* no = (NO*) malloc(sizeof(NO));
    novo->chave = ch;
    novo->prox = NULL;
    
    if (l->inicio == NULL){       
        l->inicio = novo;
        l->tam++;
    } else {
        no = l->inicio;
        while(no->prox){
            no = no->prox;
        }
        no->prox = novo;
        l->tam++;
    }
}

void remover(LISTA *l, TIPOCHAVE ch){

    NO* ant = (NO*) malloc(sizeof(NO));
    NO* no = (NO*) malloc(sizeof(NO));

    no = l->inicio;
    if (no -> prox == NULL){
        free(no);
        l->inicio = NULL;
        l->tam--;
    }
    while (no->prox){
        if(no->chave == ch){
            if (no->prox == NULL){
                free(no);
                ant->prox = NULL;
                l->tam--;
            }
            else{
            ant->prox = no->prox;
            free(no);
            l->tam--;
            break;
            }
        }
            ant = no;
            no = no->prox;
    }
}

void destruir(LISTA *l){

    NO *atual;
    NO *prox;
    atual = l->inicio;
    while (atual){
        prox = atual->prox;
        free(atual);
        atual = prox;
    }
    l->inicio = NULL;
}

NO* buscaChave(LISTA l, int pos){

    NO* p = l.inicio;
    int i = 1;
    while (p->prox && i<pos){
        
        p = p->prox;
        i++;

    }
    
    if (i != pos){
        return NULL;
    }
    
    else {
        return p;
    }
}

int encontraPos(LISTA *l, TIPOCHAVE ch){
   NO* p =  l->inicio;
   int cont = 0;
    while (p){
        
        if (p->chave == ch){
            return cont;
        }
        
        p = p->prox;
        cont++;
    }
    return -1;
}

int main(){

    LISTA lista;

    inicializar(&lista);
     
    inserir (&lista, 25);
    inserir (&lista, 5);
    inserir (&lista, 15);
    remover (&lista, 5);
    exibirLista(lista);


    
    return 0;

}


