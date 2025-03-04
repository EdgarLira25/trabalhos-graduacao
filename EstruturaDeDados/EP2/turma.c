/*********************************************************************/
/**   ACH2023 - Algoritmos e Estruturas de Dados I                  **/
/**   EACH-USP - Segundo Semestre de 2022                           **/
/**   Turma 03 - Prof. Luciano Digiampietri                         **/
/**                                                                 **/
/**   Segundo Exercicio-Programa                                    **/
/**                                                                 **/
/**   Edgar Henrique de Oliveira Lira         12717266              **/
/**                                                                 **/
/*********************************************************************/

#include "turma.h"

/* Funcao usada em testes da correcao automatica - NAO APAGAR OU MODIFICAR */
void print123(){
	/* Funcao utilizada pelo sistema de correcao automatia
	   Nao apague ou modifique esta funcao                 */
}



void insereListaCerta(PONT lista, ELEMENTO* novoElem){

    PONT atual = lista->prox;
    if (atual == lista) {
    
        atual->prox = novoElem;
        atual->ant = novoElem;
        novoElem->prox = lista;
        novoElem->ant = lista;

    } else if(novoElem->aluno.nusp < atual->aluno.nusp){
        
        atual->ant = novoElem;
        novoElem->prox = atual;
        novoElem->ant = lista;
        lista->prox = novoElem;

    } else {
    
    while (atual->prox != lista && atual->prox->aluno.nusp < novoElem->aluno.nusp) {
    
        atual = atual->prox;
    
    }
    
    novoElem->ant = atual;
    novoElem->prox = atual->prox;
    atual->prox->ant=novoElem;
    atual->prox = novoElem;

    }

}



/* Funcao que retorna o numero de alunos da turma cujo endereco foi passado
   como parametro de entrada (deve somar os alunos das tres listas). */
int tamanho(TURMA* turma){
int tam = 0;

	PONT atual;
	ALUNO aluno;

	atual = turma->LISTAS[0]->prox;
	while (atual != turma->LISTAS[0]){
		tam++;
        atual = atual->prox;
	}
	atual = turma->LISTAS[1]->prox;
	while (atual != turma->LISTAS[1]){
		tam++;
        atual = atual->prox;
	}
    atual = turma->LISTAS[2]->prox;
	while (atual != turma->LISTAS[2]){
        tam++;
		atual = atual->prox;
	}

	return tam;
}


/* Funcao que recebe o endereco de uma turma e um numero USP e retorna 
   NULL caso nao exista um aluno com o respectivo numero USP na turma ou
   o endereco de memoria do ELEMENTO que contem o respectivo aluno, caso
   ele esteja presente na turma. */
PONT buscarAluno(TURMA* turma, int nusp){

	
	/* COMPLETE/IMPLEMENTE SEU CODIGO AQUI */
	PONT atual;
	
    //aprovados
	atual = turma->LISTAS[0]->prox;
	while (atual != turma->LISTAS[0]){
		if(atual->aluno.nusp == nusp) return atual;
    	atual = atual->prox;
	}
    //recuperação
	atual = turma->LISTAS[1]->prox;
	while (atual != turma->LISTAS[1]){
		if(atual->aluno.nusp == nusp) return atual;
    	atual = atual->prox;
    }
	//Reprovados
	atual = turma->LISTAS[2]->prox;
    while (atual != turma->LISTAS[2]){
	    if(atual->aluno.nusp == nusp) return atual;   
		atual = atual->prox;
	}
    //printf("aluno nao encontrado");
	return NULL;
}



/* Funcao que recebe o endereco de uma turma e o numero USP, nota e 
   frequencia de um aluno e deve: Retornar false caso:
   o numero USP seja menor do que zero, ou a nota seja menor do que zero ou
   maior do que cem ou a frequencia seja menor do que zero ou maior do que cem;
   Deve, tambem, retornar false se a turma ja contiver um aluno com o 
   mesmo numero USP.
   Caso contrario, esse novo aluno devera ser inserido na turma e a funcao 
   devera retornar true. A insercao na turma contem as seguintes atividades
   (lembre-se que todas as listas sao ordenadas de acordo com o numero 
   USP do aluno):
     1a) alocacao dinamica de memoria de uma estrutura do tipo ELEMENTO.
         Os campos do aluno do respectivo elemento deverao ser preenchidos 
         com os valores recebidos como parâmetro pela funcao.
     2a) este novo elemento devera ser inserido na lista ligada correta, 
         de acordo com a nota e a frequencia do aluno
         (LISTAS[0] para alunos aprovados; LISTAS[1] para alunos em
         recuperacao; e LISTAS[2] para alunos reprovados).
     3a) por fim, a função deverá retornar true.
*/
bool inserirAluno(TURMA* turma, int nusp, int nota, int frequencia){


    if (nusp < 0 || nota < 0 || nota > 100 || frequencia < 0 || frequencia > 100) return false;
    if (buscarAluno(turma, nusp)){
        return false;
    }

    ALUNO novoAluno;

    novoAluno.nusp = nusp;
    novoAluno.nota = nota;
    novoAluno.freq = frequencia;

    ELEMENTO *novoElem = (PONT)malloc(sizeof(ELEMENTO));
    novoElem->aluno = novoAluno;

    if(nota >= 50 && frequencia >= 70){

        insereListaCerta(turma->LISTAS[0], novoElem);

    }
    else if(nota >=30 && nota < 50 && frequencia >= 70){

        insereListaCerta(turma->LISTAS[1], novoElem);

    } else {

        insereListaCerta(turma->LISTAS[2], novoElem);

    }

	return true;

}


/* Funcao que recebe o endereco de uma turma e um numero USP e deve:
   Retornar false se a turma nao possuir um aluno com esse numero USP.
   Caso contrario, esse aluno devera ser excluido da turma e a função devera
   retornar true. A exclusao na turma contem as seguintes atividades:
     1a) remocao do elemento que aponta para o respectivo aluno na lista
         correta (nao esqueca de acertar os ponteiros).
     2a) liberacao da memoria do elemento da lista que apontava para o
         respectivo aluno.
     3a) por fim, a funcao devera retornar true.
*/
bool excluirAluno(TURMA* turma, int nusp){

	 PONT excluido = buscarAluno(turma, nusp); 
	if(!excluido) return false;

    excluido->prox->ant = excluido->ant;
    excluido->ant->prox = excluido->prox;

    
    free(excluido);

    return true;

}

/* Funcao que recebe o endereco de uma turma, o numero USP e a nota de 
   um aluno e deve: Retornar false caso este aluno nao esteja presenta na
   lista de alunos em recuperacao (LISTAS[1]).
   Caso contrario, esse aluno devera ter sua nota atualizada com o valor 
   passado como parametro, ser retirado da lista de recuperação e inserido
   na lista correta, ordenada pelo numero USP. A lista correta dependera da
   nota do aluno: se maior ou igual que 50 devera ir para a lista de aprovados
   (LISTAS[0]), caso contrario, para a lista de reprovados (LISTAS[2]).
   Apos a remocao do aluno da lista de alunos em recuperacao e insercao na 
   lista correta (de acordo com o desempenho na recuperacao),
   a funcao devera retornar true. */
bool inserirNotaRecuperacao(TURMA* turma, int nusp, int nota){
	
	PONT atual = turma->LISTAS[1]->prox;
	while (atual != turma->LISTAS[1]){
		if(atual->aluno.nusp == nusp) break;
    	atual = atual->prox;
    } 
    if (atual == turma->LISTAS[1]) return false;

    atual->aluno.nota = nota;
    atual->prox->ant = atual->ant;
    atual->ant->prox = atual->prox;

    if (nota >= 50){
        insereListaCerta(turma->LISTAS[0], atual);
    } else {
        insereListaCerta(turma->LISTAS[2], atual);
    }
	
	return true;
}



/* Funcao que cria e retorna uma TURMA.
   Neste EP, uma turma contem tres listas duplamente ligadas de ELEMENTOS,
   estas listas sao circulares e possuem no-cabeca
*/
TURMA inicializaTurma(){
	TURMA t1;

	// criacao de um aluno ficticio que poder ser usado como sentinela
	ALUNO ficticio;
	ficticio.nusp = -1;
	ficticio.nota = -1;
	ficticio.freq = -1;

	// criacao dos tres nos-cabeca
	int c;
	for (c=0; c<3; c++){
		t1.LISTAS[c] = (PONT) malloc(sizeof(ELEMENTO));
		t1.LISTAS[c]->aluno = ficticio;
		t1.LISTAS[c]->prox = t1.LISTAS[c];
		t1.LISTAS[c]->ant = t1.LISTAS[c];
	}
	return t1;
}



/* Funcao que reinicia (ou limpa) a TURMA passada como parametro.
   Todos os elementos, exceto os nos-cabeca, sao apagamos e a TURMA fica
   da mesma forma como se ela tivesse sido recem criada.
*/
void reinicializaTurma(TURMA* turma){
	PONT atual, apagar;
	
	// apagar todos os elementos, exceto o cabeca, da LISTAS[0]
	atual = turma->LISTAS[0]->prox;
	while (atual != turma->LISTAS[0]){
		apagar = atual;
		atual = apagar->prox;
		free(apagar);
	}
	atual->prox = atual;
	atual->ant = atual;
	
	// apagar todos os elementos, exceto o cabeca, da LISTAS[1]
	atual = turma->LISTAS[1]->prox;
	while (atual != turma->LISTAS[1]){
		apagar = atual;
		atual = apagar->prox;
		free(apagar);
	}
	atual->prox = atual;
	atual->ant = atual;

	// apagar todos os elementos, exceto o cabeca, da LISTAS[2]
	atual = turma->LISTAS[1]->prox;
	while (atual != turma->LISTAS[1]){
		apagar = atual;
		atual = apagar->prox;
		free(apagar);
	}
	atual->prox = atual;
	atual->ant = atual;
	
	
}

/* Funcao que exibe todos os alunos da turma referenciada como parametro.
   Exibe os alunos das tres listas. */
void exibirTurma(TURMA* turma){
	PONT atual;
	ALUNO aluno;
	printf("\n###### Exibindo lista [%i aluno(s)] ######\n", tamanho(turma));
	printf("   Alunos Aprovados:");
	atual = turma->LISTAS[0]->prox;
	while (atual != turma->LISTAS[0]){
		aluno = atual->aluno;
		printf(" (%4i, %3i, %3i)", aluno.nusp, aluno.nota, aluno.freq);
		atual = atual->prox;
	}
	printf("\n");
	
	printf("   Alunos em Recuperacao:");
	atual = turma->LISTAS[1]->prox;
	while (atual != turma->LISTAS[1]){
		aluno = atual->aluno;
		printf(" (%4i, %3i, %3i)", aluno.nusp, aluno.nota, aluno.freq);
		atual = atual->prox;
	}
	printf("\n");
	atual = turma->LISTAS[2]->prox;
	printf("   Alunos Reprovados:");
	while (atual != turma->LISTAS[2]){
		aluno = atual->aluno;
		printf(" (%4i, %3i, %3i)", aluno.nusp, aluno.nota, aluno.freq);
		atual = atual->prox;
	}
	printf("\n");

	printf("\n###### EXIBINDO OS ALUNOS EM ORDEM INVERSA ######\n");
	printf("   Alunos Aprovados:");
	atual = turma->LISTAS[0]->ant;
	while (atual != turma->LISTAS[0]){
		aluno = atual->aluno;
		printf(" (%4i, %3i, %3i)", aluno.nusp, aluno.nota, aluno.freq);
		atual = atual->ant;
	}
	printf("\n");
	
	printf("   Alunos em Recuperacao:");
	atual = turma->LISTAS[1]->ant;
	while (atual != turma->LISTAS[1]){
		aluno = atual->aluno;
		printf(" (%4i, %3i, %3i)", aluno.nusp, aluno.nota, aluno.freq);
		atual = atual->ant;
	}
	printf("\n");
	atual = turma->LISTAS[2]->ant;
	printf("   Alunos Reprovados:");
	while (atual != turma->LISTAS[2]){
		aluno = atual->aluno;
		printf(" (%4i, %3i, %3i)", aluno.nusp, aluno.nota, aluno.freq);
		atual = atual->ant;
	}
	printf("\n\n");	
}