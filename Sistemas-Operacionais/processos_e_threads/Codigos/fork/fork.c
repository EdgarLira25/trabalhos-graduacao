#include <stdio.h>   //Biblioteca que implementa a função usada printf
#include <unistd.h>  //Biblioteca que implementa a função usada fork

int main() { // Declaração da função Main

  fork(); // Função que cria um processo filho igual ao processo pai
  printf("Hello World!\n"); // Imprime Hello World

  return 0; // Indica que o programa acabou
}
