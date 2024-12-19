#include <stdio.h>
#include <stdlib.h>

int fibo(int n) {
    if (n == 0) return 0; // Base case
    if (n == 1) return 1;
    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b; 
        a = b;      
        b = temp;    
    }
    return b;
}

int main() {
    char input_n[5];
    fgets(input_n, 5, stdin); 
    int n, i;
    n = atoi(input_n); 

    for (i = 0; i <= n; i++) { 
        printf("F(%d) = %d\n", i, fibo(i)); 
    }
    
    return 0;
}
