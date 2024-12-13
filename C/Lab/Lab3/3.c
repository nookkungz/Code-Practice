#include <stdio.h>
#include <stdlib.h>

int main () {
    int num1 , num2 ;
    char input[10];

    fgets(input,sizeof(input),stdin);
    num1 = atoi(input);

    fgets(input,sizeof(input),stdin);
    num2 = atoi(input);
}