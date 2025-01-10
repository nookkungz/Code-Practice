#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    printf("Enter the number of rows or columns: ");
    scanf("%d", &n);

    // Allocate memory for row pointers
    int **a = (int **)malloc(n * sizeof(int *));
    
    // Allocate memory for each row
    for (i = 0; i < n; i++) {
        a[i] = (int *)malloc(n * sizeof(int));
    }

    // Assign values to array a
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            a[i][j] = i + j + 1;  // Filling the array according to the required pattern
        }
    }

    // Print all values in array a
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%2d ", a[i][j]);  // Adjust formatting for proper spacing
        }
        printf("\n");
    }

    // Free allocated memory
    for (i = 0; i < n; i++) {
        free(a[i]);
    }
    free(a);

    return 0;
}
