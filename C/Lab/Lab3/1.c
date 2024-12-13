#include <stdio.h>
#include <stdlib.h>

int main () {
    int n , i = 0 ;
    char input[10];

    fgets(input, sizeof(input), stdin);
    n = atoi(input);
    while (i <= n)
    {
        printf("%d\n",n);
        n--;

    }
    return 0;
}