#include <stdio.h>
#include <stdlib.h>

int main() {
    char input[10];
    int binary[32]; 
    int num, i = 0;

    fgets(input, sizeof(input), stdin);
    num = atoi(input); 

    printf("Binary number of %d is ", num);

    while (num > 0 && i < 32) { 
        binary[i] = num % 2;
        num = num / 2;
        i++;
    }

    
    int total_bits = (i < 4) ? 4 : i; 
    for (int j = i; j < 4; j++) {
        printf("0");
    }

    
    while (--i >= 0 && total_bits > 0) { 
        printf("%d", binary[i]);
        total_bits--;
    }
    printf(".\n");
}
