#include "turma.c"

int main(){

	int nusp;
	ALUNO* res;
	bool ok;
	
	TURMA turma1 = inicializaTurma();

	exibirTurma(&turma1);	

	nusp = 1234;
	ok = inserirAluno(&turma1, nusp, 100, 95);
	if (ok) printf("Inseracao do aluno %4i retornou true.\t(OK)\n", nusp);
	else  printf("Inseracao do aluno %4i retornou false.\t(NOK)\n", nusp);

	exibirTurma(&turma1);

	nusp = 1234;
	ok = inserirAluno(&turma1, nusp, 100, 95);
	if (ok) printf("Inseracao do aluno %4i retornou true.\t(NOK)\n", nusp);
	else  printf("Inseracao do aluno %4i retornou false.\t(OK)\n", nusp);

	exibirTurma(&turma1);

	nusp = 1111;
	ok = inserirAluno(&turma1, nusp, 50, 75);
	if (ok) printf("Inseracao do aluno %4i retornou true.\t(OK)\n", nusp);
	else  printf("Inseracao do aluno %4i retornou false.\t(NOK)\n", nusp);

	exibirTurma(&turma1);

	nusp = 2345;
	ok = inserirAluno(&turma1, nusp, 25, 100);
	if (ok) printf("Inseracao do aluno %4i retornou true.\t(OK)\n", nusp);
	else  printf("Inseracao do aluno %4i retornou false.\t(NOK)\n", nusp);

	exibirTurma(&turma1);

	ok = inserirAluno(&turma1, nusp, 25, 100);
	if (ok) printf("Inseracao do aluno %4i retornou true.\t(NOK)\n", nusp);
	else  printf("Inseracao do aluno %4i retornou false.\t(OK)\n", nusp);

	exibirTurma(&turma1);

	
	nusp = 9876;
	res = buscarAluno(&turma1, nusp);
	if (res) printf("Nota do aluno %i: %3i\n", nusp, res->nota);
	else printf("Aluno nao encontrado: '%i'\n", nusp);

	nusp = 1234;
	res = buscarAluno(&turma1, nusp);
	if (res) printf("Nota do aluno %i: %3i\n", nusp, res->nota);
	else printf("Aluno nao encontrado: '%i'\n", nusp);			
	
	nusp = 1111;
	res = buscarAluno(&turma1, nusp);
	if (res) printf("Nota do aluno %i: %3i\n", nusp, res->nota);
	else printf("Aluno nao encontrado: '%i'\n", nusp);

	nusp = 2345;
	res = buscarAluno(&turma1, nusp);
	if (res) printf("Nota do aluno %i: %3i\n", nusp, res->nota);
	else printf("Aluno nao encontrado: '%i'\n", nusp);



	nusp = 2345;
	ok = excluirAluno(&turma1, nusp);
	if (ok) printf("A exclusao do aluno %i retornou true.\t(OK)\n", nusp);
	else printf("A exclusao do aluno %i retornou false.\t(NOK)\n", nusp);

	exibirTurma(&turma1);

	nusp = 2345;
	ok = excluirAluno(&turma1, nusp);
	if (ok) printf("A exclusao do aluno %i retornou true.\t(NOK)\n", nusp);
	else printf("A exclusao do aluno %i retornou false.\t(OK)\n", nusp);

	exibirTurma(&turma1);

	nusp = 1234;
	ok = excluirAluno(&turma1, nusp);
	if (ok) printf("A exclusao do aluno %i retornou true.\t(OK)\n", nusp);
	else printf("A exclusao do aluno %i retornou false.\t(NOK)\n", nusp);

	exibirTurma(&turma1);

	nusp = 1111;
	ok = excluirAluno(&turma1, nusp);
	if (ok) printf("A exclusao do aluno %i retornou true.\t(OK)\n", nusp);
	else printf("A exclusao do aluno %i retornou false.\t(NOK)\n", nusp);

	exibirTurma(&turma1);
	
	nusp = -1;
	ok = excluirAluno(&turma1, nusp);
	if (ok) printf("A exclusao do aluno %i retornou true.\t(NOK)\n", nusp);
	else printf("A exclusao do aluno %i retornou false.\t(OK)\n", nusp);

	exibirTurma(&turma1);

	inserirAluno(&turma1, 2000, 80, 90);
	inserirAluno(&turma1, 2001, 81, 91);
	inserirAluno(&turma1, 2002, 82, 92);
	inserirAluno(&turma1, 1999, 79, 89);
	inserirAluno(&turma1, 1998, 78, 88);
	inserirAluno(&turma1, 1997, 77, 87);

	exibirTurma(&turma1);

	reinicializaTurma(&turma1);

	exibirTurma(&turma1);

	inserirAluno(&turma1, 1999, 79, 89);
	inserirAluno(&turma1, 1998, 78, 88);
	inserirAluno(&turma1, 1997, 77, 87);
	inserirAluno(&turma1, 2000, 80, 90);
	inserirAluno(&turma1, 2001, 81, 91);
	inserirAluno(&turma1, 2002, 82, 92);

	exibirTurma(&turma1);

	return 0;
}
