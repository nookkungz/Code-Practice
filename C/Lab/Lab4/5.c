#include <stdio.h>
#include <stdlib.h>

int main() {
    int num, i , j, k, c;
    char input[10];
    fgets(input, sizeof(input), stdin);
    num = atoi(input);
    for (j=num-2 ; j >= 0;j--) {
        for(i = j; i >= 0;i--){
            printf("--");
        }
        c -= 1;
        for (k=0 ;k >= 0; k--){
        printf("%c","a"+k);
    }
        printf("\n");
    
    }


    for (j=2 ; j <= num;j++) {
        for(i = 0; i <= j;i++){
            printf("--");
        }
        printf("\n");
    }

    return 0;
}
