#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Enter n: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        printf("-");
        for (int j = 1; j < i; j++) {
            if (j % 2 == 1) {
                printf("x");
            } else {
                printf("-");
            }
        }
        printf("\n");
    }

    for (int i = n - 1; i >= 1; i--) {
        printf("-");
        for (int j = 1; j < i; j++) {
            if (j % 2 == 1) {
                printf("x");
            } else {
                printf("-");
            }
        }
        printf("\n");
    }

    return 0;
}
