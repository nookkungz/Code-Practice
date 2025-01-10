#include <stdio.h>
#include <stdlib.h>
int main() {
    int n;
    double pi = 0.0;

    printf("Enter n: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        double term = 4.0 / (2 * i + 1);
        if (i % 2 == 0) {
            pi += term; 
        } else {
            pi -= term; 
        }
    }

    printf("%.10f\n", pi);
    return 0;
}