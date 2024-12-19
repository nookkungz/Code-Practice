#include <stdio.h>
#include <stdlib.h>

int main() {
    char input_a[20], input_b[20];
    int a, b, gcd, temp, original_a, original_b;
    fgets(input_a, sizeof(input_a), stdin);
    fgets(input_b, sizeof(input_b), stdin);
    a = atoi(input_a);
    b = atoi(input_b);
    original_a = a;
    original_b = b;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    gcd = a; 
    int p = original_a / gcd;
    int q = original_b / gcd;
    if (q == 1) {
        printf("= %d\n", p);
    } else {
        printf("= %d/%d\n", p, q); 
    }
    return 0;
}
