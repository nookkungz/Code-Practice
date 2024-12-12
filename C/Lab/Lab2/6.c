#include <stdio.h>
#include <stdlib.h>
#include <ctype.h> 

int main() {
    char input[2];  

    fgets(input, sizeof(input), stdin); 

    char ch = input[0]; 

 
    if (islower(ch)) {
        printf("Output: lower case\n");
    } else if (isupper(ch)) {
        printf("Output: upper case\n");
    } else if (isdigit(ch)) {
        printf("Output: digit\n");
    } else {
        printf("Output: others\n");
    }

    return 0;
}