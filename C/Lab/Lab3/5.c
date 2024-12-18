#include <stdio.h>
#include <stdlib.h>

int main() {

    int num , i;
    char input[10];

    fgets(input,sizeof(input),stdin);
    num = atoi(input);
    if (num == 0) {
        printf("-");
    }
    else {
    for (i = (num+96) ;  i >= 97 ; i--){
        printf("%c",i);
        if (i > 97) printf("-");
    }
    for (i = 98 ;  i <= (num + 96) ; i++){
        printf("-%c",i);
    }
    }
}