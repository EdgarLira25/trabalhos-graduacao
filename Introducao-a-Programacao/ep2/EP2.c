/*********************************************************************/
/**   ACH2001 - Introducao a Programacao                            **/
/**   EACH-USP - Primeiro Semestre de 2021                          **/
/**   <2021102> - <Márcio Moretto Ribeiro>                          **/
/**                                                                 **/
/**   Segundo Exercicio-Programa                                    **/
/**                                                                 **/
/**   <Edgar Henrique de Oliveira Lira>         <12717266>          **/
/**                                                                 **/
/*********************************************************************/

/*
	Calculo para raiz quadrada
*/

#include <stdio.h>

/*
	Calcula a raiz quadrada de um valor, com uma determinada
	precisao. Retorna esse valor, ou -1 quando:
	
	* a < 0
	* epsilon <= 0
	* epsilon >= 1
	
	Parametro:
		a - valor cuja raiz quadrada sera calculada
		epsilon - precisao do calculo
*/

double funcaoAuxiliar(double xa, double xb){

if (xa - xb > 0)
  return (xa - xb);
   else{
      return (-xa + xb);
  }
}

double raizQuadrada(double a, double epsilon) {
	double resposta;
  double x0 = a*0.5;
  double x1 = 0.5*(x0 + (a/x0));

  if (a < 0 || epsilon <=0 || epsilon >= 1)

    resposta = -1;

  if (a == 0)

    resposta = 0;

  if (a > 0 && epsilon > 0 && epsilon < 1){

    do {

        x0=x1;

        x1 = 0.5*(x0 + (a/x0));
  } 
  while( funcaoAuxiliar(x1,x0) >= epsilon);
      resposta = x1;
  }

	return resposta;
}


/*
	Apenas para seus testes. ISSO SERA IGNORADO NA CORRECAO
*/
int main() {

	/* escreva seu codigo (para testes) aqui */

	/* Exemplo de teste: */
	double valor = 859;
	double precisao = 0.001;
	printf("Raiz aproximada de %f = %f\n", valor, raizQuadrada(valor, precisao));

	return 0;
}
