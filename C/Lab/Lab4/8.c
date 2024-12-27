#include <stdio.h>
#include <stdlib.h>

void Recursion(int r) {
    
    if (r > 1) {
        Recursion(r / 2);
    }
    printf("%d", r % 2);
}

int main() {
    char input[12];
    int n;

    fgets(input, sizeof(input), stdin);
    n = atoi(input);
    Recursion(n);

    return 0;
}
