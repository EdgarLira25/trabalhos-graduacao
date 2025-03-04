#include <pthread.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int vez = 0;
int count = 0;

void secao_nao_critica(int x) {
  printf("Processo %d saiu da seção critica... Executando seção não crítica\n\n", x);
}

void secao_critica(int y) {
  printf("Processo %d entrou na seção crítica\n", y);
  sleep(1.5);
  printf("count = %d, ID = %d\n", count, y);
  count++;
}

void *P0(void *id) {

  int meu_id = 0;
  int outro = 1;

  while (1) {

    while (vez != meu_id)
      ;
    secao_critica(meu_id);
    vez = outro;
    secao_nao_critica(meu_id);
  }

  return NULL;
}

void *P1(void *id) {

  int meu_id = 1;
  int outro = 0;
  while (1) {

    while (vez != meu_id)
      ;
    secao_critica(meu_id);
    vez = outro;
    secao_nao_critica(meu_id);
  }

  return NULL;
}

int main(void) {

  printf("/////INICIO//////\n-----------------\n");

  pthread_t id0, id1;

  pthread_create(&id0, NULL, P0, (void *)&id0);
  pthread_create(&id1, NULL, P1, (void *)&id1);

  pthread_exit(NULL);

  return 0;

}
