#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, a, b, c;
    
    scanf("%d", &n);

    for (a = 1; a < n; a++) {
        for (b = a + 1; b < n; b++) {
            c = n - a - b;
            if (c > b && (a * a + b * b == c * c)) {
                printf("(%d, %d, %d)\n", a, b, c);
                return 0;
            }
        }
    }
    printf("No triple found.\n");
    return 0;
}