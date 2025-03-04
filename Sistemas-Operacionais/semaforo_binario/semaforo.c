#include <stdio.h> // Printf
#include <pthread.h> // Threads
#include <semaphore.h> // Semáforo
#include <unistd.h>  // Sleep
#include <stdlib.h> // Função Random

#define true 1
#define false 0
#define MAX 5

typedef int bool;

sem_t s;
sem_t in, ex;
sem_t turno;

typedef struct{
    int A[MAX];
    int inicio;
    int nroElem;
}FILA;

FILA f;

void inicializarFila(FILA *f){
    f->inicio = 0;
    f->nroElem = 0;
}

void inserir(FILA *f, int id){
    sem_wait(&in);
    if(f->nroElem==MAX){ 
    sem_post(&in);
    return ;
    }

    f->A[(f->inicio+f->nroElem)%MAX] = id;
    f->nroElem++;

    sem_post(&in);
}

void excluir(FILA *f){
    sem_wait(&ex);
    if(f->nroElem == 0){
        sem_post(&ex);
        return ;
    } 
    f->inicio = (f->inicio +1) % MAX;
    f->nroElem--;
    sem_post(&ex);

}

int vez(FILA *f){
    return f->A[f->inicio];
}

void* Thread(void * arg) {
 int id = *(int *) arg;

int v;
 while(1){
    
    inserir(&f, id);
    while(true){
        sem_wait(&turno);
        v = vez(&f);
        sem_post(&turno);
        if (id == vez(&f))
            break;
        sleep(0.3);
    }
    sem_wait(&s);
    printf("Thread %d Passou pelo semaforo e está na seção crítica\n", id);
    sleep(1);
    printf("Thread %d esta voltando para fila...\n", id);
    excluir(&f);
    sem_post(&s);
    sleep(0.3);

 }
}

int main() {
 inicializarFila(&f);
 pthread_t threads[3];
 int idThread[3];
 sem_init(&s, 0, 1);
 sem_init(&ex, 0, 1);
 sem_init(&in, 0, 1);
 sem_init(&turno, 0, 1);

 printf("------Problema da seção crítica com semáforo------\n");
 printf("\n   ------Iniciando Threads e semáforo------\n\n");
 
 for (int i = 0; i<3; i++){
   idThread[i] = i;
   pthread_create(&threads[i],NULL,Thread, (void*)&idThread[i]);
 }
 for (int i = 0; i<3; i++){
 pthread_join(threads[i],NULL);
 }

  return 0;
}
