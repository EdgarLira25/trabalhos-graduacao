#include <stdio.h>
#include "listaAux.c"

int main(){
    LISTA x = inicializar();

    inserir(&x, 5);
    inserir(&x, 5);
    printf("%d", buscaChave(x,5));
}