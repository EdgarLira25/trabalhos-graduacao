
typedef int TIPOCHAVE;

typedef struct estrutura
{
    TIPOCHAVE chave;
    struct estrutura *prox;
} NO;

typedef struct
{
    NO *inicio;
} LISTA;

LISTA inicializar();
void inserir(LISTA *l, TIPOCHAVE ch);
int buscaChave(LISTA l, int item);
