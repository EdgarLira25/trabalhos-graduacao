/*********************************************************************/
/**   ACH2001 - Introducao a Programacao                            **/
/**   EACH-USP - Primeiro Semestre de 2021                          **/
/**   <2021102> - <Márcio Moretto Ribeiro>                          **/
/**                                                                 **/
/**   Primeiro Exercicio-Programa                                   **/
/**                                                                 **/
/**   <Edgar Henrique de Oliveira Lira>         <12717266>          **/
/**                                                                 **/
/*********************************************************************/

/*
	Caixa eletronico das Ilhas Weblands, com estoque ilimitado de cedulas
	de B$50,00, B$20,00, B$5,00 e B$1,00.
*/

#include <stdio.h>

/* Numero de cedulas de B$50,00 */
int n50;
	
/* Numero de cedulas de B$20,00 */
int n20;

/* Numero de cedulas de B$5,00 */
int n5;
	
/* Numero de cedulas de B$1,00 */
int n1;


/*
	Determina a quantidade de cada nota necessaria para totalizar
	um determinado valor de retirada, de modo a minimizar a quantidade
	de cÃ©dulas entregues.
	
	Abastece as variaveis globais n50, n20, n5 e n1 com seu respectivo
	numero de cedulas.
	
	Parametro:
		valor - O valor a ser retirado
*/
void fazRetirada(int valor) {
  int valorPedido = valor;
  
    if (valor <=0)
      n50 = -1, n20 = -1, n5 = -1, n1 = -1;
  
    else{
      n50 = valorPedido / 50;
      valorPedido = valorPedido % 50;
      
      n20 = valorPedido / 20;
      valorPedido = valorPedido % 20;
      
      n5 = valorPedido / 5;
      valorPedido = valorPedido % 5;
      
      n1 = valorPedido;

  }
}



/*
	Funcao main apenas para seus testes. ISSO SERA IGNORADO NA CORRECAO
*/
int main() {
	/* escreva seu codigo (para testes) aqui */

	int valor;
	/* Exemplos de testes: */
	valor = 138;
	fazRetirada(valor);
	printf("Valor: %i\n",valor);
	printf("Notas de 50: %i\n", n50);
	printf("Notas de 20: %i\n", n20);
	printf("Notas de 5:  %i\n", n5);
	printf("Notas de 1:  %i\n", n1);

	valor = 21;
	fazRetirada(valor);
	printf("Valor: %i\n",valor);
	printf("Notas de 50: %i\n", n50);
	printf("Notas de 20: %i\n", n20);
	printf("Notas de 5:  %i\n", n5);
	printf("Notas de 1:  %i\n", n1);
	return 0;
}
