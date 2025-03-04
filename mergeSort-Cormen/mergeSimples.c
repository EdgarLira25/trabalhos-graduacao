#include <stdio.h>
#include <stdlib.h>

void merge(int A[], int q, int r, int p){
 int i, j, k;
 int n1 = q - p + 1;
 int n2 = r - q;
 int L[n1 + 1], R[n2 + 1];
  
  for (i=1; i <= n1; i++){ L[i] = A[p + i - 1]; }
  for (j=1; j <= n2; j++){ R[j] = A[q + j]; }

  L[n1 + 1] = 200;
  R[n2 + 1] = 200;

  i=1;
  j=1;
  
  for (k = p; k <= r; k++){
    if(L[i] <= R[j]){
      A[k] = L[i];
        i = i+1;
        } 
          else{
            A[k] = R[j];
              j = j+1;}
  }
}

int main(void){

int p = 0, q = 3, r = 7, A[8] = {2,4,5,7,1,2,3,6};

printf("Array Desordenado:\n");

int h;

putchar('{');
for(h = 0; h < 7; h++){
printf("%d, ", A[h]);
}
printf("%d}", A[h++]);


merge(A, q, r, p);


  printf("\nArray Ordenado:\n{");
  for(int k = 0; k < r; k++){
    printf("%d, ", A[k]);}
  printf("%d}\n", A[r]);

  return 0;
}
