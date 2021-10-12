#include <stdio.h>
#include <stdlib.h>

/*---------------------------Ordenar---------------------*/

 #define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; })

void swap(int* xp, int* yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
int * selectionSort(int arr[], int n)
{
    int i, j, min_idx;
 
    for (i = 0; i < n - 1; i++) {
 
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
 

        swap(&arr[min_idx], &arr[i]);
    }

    return arr;
}


void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 /*---------------------------Ordenar---------------------*/
int remove_duplicate(int arr[], int n)
{

  if (n == 0 || n == 1)
    return n;

  int temp[n];

  int j = 0;
  int i;
  for (i = 0; i < n - 1; i++)
    if (arr[i] != arr[i + 1])
      temp[j++] = arr[i];
  temp[j++] = arr[n - 1];

  for (i = 0; i < j; i++)
    arr[i] = temp[i];

  return j;
}

 /*---------------------------Ordenar---------------------*/


int _lis(int arr[], int n)
{

    int *b[n];
    int aux2[n];

    for(int i = 0; i<n; i++){
        aux2[i]=arr[i];
    }

    *b = selectionSort(aux2, n);
    int m = remove_duplicate(*b, n);
    int x = n;


    int aux[n];
    for(int i = 0; i<n; i++){
        aux[i]=arr[i];
    }

    int temp = 0;
//Ordenar el Arreglo    
    for (int i = 0; i < n; i++) {     
        for (int j = i+1; j < n; j++) {     
           if(aux[i] > aux[j]) {    
               temp = aux[i];    
               aux[i] = aux[j];    
               aux[j] = temp;    
           }     
        }     
    }    
//Quitar Duplicados
    x = remove_duplicate(aux, x);


//Crear y llenado inicial de la matriz de memoizacion
    int mat[m][n];

    for(int i=0; i<=n; i++) {
      for(int j=0;j<=m; j++) {
         mat[i][j] = -1;
      }
   }
   
   for (int i = 0; i<=n; i++){
       for (int j = 0; j<=m; j++){
           if(i==0 || j==0){
               
               mat[i][j]=0;
           }
           else if(arr[i-1] == aux[j-1]){
     
               mat[i][j]=1+mat[i-1][j-1];
           }
           else{
               
               mat[i][j]=max(mat[i-1][j],mat[i][j-1]);
           }
       }
   }
 
    return mat[n][m];

}



int main(void) {
  
  int arr[] = {6,1,5,6};

  //printf("Hello World\n");
  int n = sizeof(arr) / sizeof(arr[0]);

  int d;
  d = _lis(arr,n);
  printf("%d",d);

  return 0;
}

