#include <pthread.h> //Biblioteca para Threads
#include <stdio.h> //Biblioteca para o printf
#include <stdlib.h> //A função Sleep depende desta biblioteca para funcionar
#include <unistd.h> //Biblioteca da função de sleep
//função que será executada pelas Threads
void *functionThread(void *id) {
  //passa o ID da Thread para variável ID
  long *ID = (long *)id;
  // Seleciona um valor aleatório entre 0 e 5 e atribui ele a variável tempo
  int tempo = rand() % 5;
  // Printa o valor de tempo em que a thread irá dormir
  printf("Thread %ld vai dormir por: %ds\n", *ID, tempo);
  //coloca a thread para dormir 
  sleep(tempo);
  //printa HelloWorld e o ID da thread
  printf("HelloWorld, ID = %ld\n", *ID);
  //Retorno opcional (função do tipo void)
  return NULL;

}

int main(void) {
  //Declaro as variáveis
  pthread_t id0, id1, id2;
  //adiciono o ponteiro para memória delas em um array
  pthread_t *Theads[] = {&id0, &id1, &id2};
  // Crio um loop para criar as threads
  for (int k = 0; k < 3; k++) {
    pthread_create(Theads[k], NULL, functionThread, (void *)Theads[k]);
  }
  // função de Exit para as threads
  pthread_exit(NULL);
  // indica que a execução terminou 
  return 0;
}
