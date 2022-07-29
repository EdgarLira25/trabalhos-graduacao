#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef int TIPOCHAVE;
typedef enum {esq, dir} LADO;

typedef struct estrutura {
TIPOCHAVE chave;
struct estrutura *esq;
struct estrutura *dir;
int bal;
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


//inserção
NO* inserirAVL(NO* p, TIPOCHAVE ch, bool *ajustar) {

    if(!p){
        p = (NO *) malloc(sizeof(NO));
        p->esq = NULL;
        p->dir = NULL;
        p->chave = ch;
        p->bal = 0;
        *ajustar = true;

    } else {
        if(ch < (p)->chave) {
            p->esq = inserirAVL(p->esq, ch, ajustar);
            if(*ajustar)
            switch (p->bal) {
                case 1 : p->bal = 0;
                    *ajustar = false;
                    break;
                case 0 : p->bal = -1;
                    break; // continua verificando
                case -1: p = rotacaoL(p);
                    *ajustar = false;
                    break;
            }
        }
        else {
            p->dir = inserirAVL(p->dir, ch, ajustar);
            if(*ajustar)
                switch (p->bal) {
                    case -1: p->bal = 0;
                        *ajustar = false;
                        break;
                    case 0 : p->bal = 1;
                        break; // continua verificando
                    case 1 : p = rotacaoR(p);
                        *ajustar = false;
                        break;
            }
        }
    }
    return (p);
}

NO* rotacaoL(NO* p){
    NO* u;
    NO* v;
    u = p->esq;
    if(u->bal == -1){
        // LL
        p->esq = u->dir;
        u->dir = p;
        p->bal = 0;
        p = u;
    } 
    else {
        // LR
        v = u->dir;
        u->dir = v->esq;
        v->esq = u;
        p->esq = v->dir;
        v->dir = p;
        
        if(v->bal == -1) 
            p->bal = 1;
        else 
            p->bal = 0;
        if(v->bal == 1) 
            u->bal = -1;
        else 
            u->bal = 0;
        
        p = v;
    }
    p->bal = 0; // balanço final da raiz (p) da subarvore
    return (p);
}





//remoção

int main(){
    

    
    return 0;
}