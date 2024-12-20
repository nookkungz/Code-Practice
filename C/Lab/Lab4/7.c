#include <stdio.h>
#include <stdlib.h>

int main (){
    int n, i, j, k, p ;
    char input[10];
    fgets(input,sizeof(input),stdin);
    n = atoi(input);

    for (j = 0;j < n;j++){
        for(i = 0;i <= j;i++){
            printf("*");
        }
        printf("\n");
    }
    for (j = n-2;j >= 0;j--){
        for(i = 0;j >= i;i++){
            printf("*");
        }
        printf("\n");
    }
    
}