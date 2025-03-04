#include <stdio.h>
int inversoMultiplicativo(int num, int mod)
{

    for (int x = 0; x < mod; x++)
    {
        if (((num)*x % mod) == 1)
        {
            return x;
        }
    }

    return num;
}
int inversoAditivo(int x, int mod)
{
return -x+mod;
}

int modulo(int x, int mod){
    return x%mod;
}

int main(){
    int x;
    while(1){
    scanf("%d", &x);
    printf("modulo = %d\n", x%26);
    printf("inverso Mult %d\n",inversoMultiplicativo(x,26));
    printf("inverso Ad %d\n", inversoAditivo(x,26));
    }
    return 0;

}