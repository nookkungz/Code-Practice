#include <stdio.h>
#include <stdlib.h>

int main() {

    int num , i;
    char input[10];

    fgets(input,sizeof(input),stdin);
    num = atoi(input);

    for (i = (num+96) ;  i >= 97 ; i--){
        printf("%c-",i);
    }
    printf("%c",97);
    i = (num+96) ;
    for (i >= 98 ; i ; i--){
        printf("-%c",i);
    }
}