#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<semaphore.h>
#include<unistd.h>

sem_t prato;
sem_t garfo[5];

typedef struct {

char *nome;
int numero;
pthread_t thread;

} filosof;

void* filosofo(void *pensador) {
	
	filosof* fil=(filosof *)pensador;

		sleep(3);
	
	while(1){
		
		sem_wait(&prato);	

		sem_wait(&garfo[fil->numero]);
		printf("%s pegou o garfo %d\n",fil->nome , fil->numero);
		sem_wait(&garfo[(fil->numero+1)%5]);
		printf("%s pegou o garfo %d\n",fil->nome, (fil->numero+1)%5);
		
		printf("%s esta comendo.\n",fil->nome);
		sleep (1);

	        printf("%s soltou os garfos %d e %d\n", fil->nome, fil->numero, (fil->numero+1)%5);
		
		sem_post(&garfo[(fil->numero+1)%5]);
		sem_post(&garfo[fil->numero]);
		
		printf("%s voltou a pensar...\n",fil->nome );
		sem_post(&prato);
		sleep(5);
	}
}

int main(){

	filosof pensador[5];

	printf("---------Iniciando o Jantar dos Filósofos----------\n\n");
	
	pensador[0].nome = "Sócrates";
	pensador[1].nome = "Platao";
	pensador[2].nome = "Aristoteles";
	pensador[3].nome = "Democrito";
	pensador[4].nome = "Espinoza";
	
	sem_init(&prato,0,2);

	for(int i=0;i<5;i++){
		sem_init(&garfo[i],0,1);
	}

	for(int i=0;i<5;i++){
		pensador[i].numero = i;
		pthread_create(&pensador[i].thread, NULL, filosofo, (void *)&pensador[i]);
		printf("%s esta pensando...\n", pensador[i].nome);
	}

	for(int i=0;i<5;i++) 
		pthread_join(pensador[i].thread,NULL);
}
