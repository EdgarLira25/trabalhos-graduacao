#include "listaAux.h"
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

LISTA inicializar()
{
    LISTA lista;
    lista.inicio = NULL;
    return lista;
}

void inserir(LISTA *l, TIPOCHAVE ch)
{
    NO *novo = (NO *)malloc(sizeof(NO));
    NO *no = (NO *)malloc(sizeof(NO));
    novo->chave = ch;
    novo->prox = NULL;

    if (l->inicio == NULL)
    {
        l->inicio = novo;
    }
    else
    {
        no = l->inicio;
        while (no->prox)
        {
            no = no->prox;
        }
        no->prox = novo;
    }
}

int buscaChave(LISTA l, int item)
{

    NO *p = l.inicio;

    while (p)
    {
        if (p->chave == item){
            return 1;
        }
        p = p->prox;
    }
    return -1;
}
