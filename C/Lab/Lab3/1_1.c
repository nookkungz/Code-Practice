#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    char input[10];

    // Read input
    fgets(input, sizeof(input), stdin);
    n = atoi(input);

    // Handle the special case for -1
    if (n <= -1) {
        return 0; // Exit without printing anything
    }

    // Initialize i to n
    i = n;

    // Infinite loop with break condition
    while (1) {
        printf("%d\n", i);
        i--;

        if (i < 0) { // Break condition
            break;
        }
    }

    return 0;
}
