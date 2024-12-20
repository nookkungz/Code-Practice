#include <stdio.h>
#include <stdlib.h>

int main() {
    int n , i , j , k , p;
    char input[10] ;
    fgets(input,sizeof(input),stdin);
    n = atoi(input);
    fgets(input,sizeof(input),stdin);
    i = atoi(input);

    for (j = 0 ; j < i ; j++){
        
        for (k = 1; k <= j; k++){
            printf(" ");
        }
        printf("*");
        if (j == 0 || j == i-1) {
            for (p = 1 ; p < n ; p++){
            printf("*");
        }
        }
        else {
            for (p = 2 ; p < n ; p++){
            printf(" ");
        }
        printf("*");
        }
        
        printf("\n");
    }

}