#include <stdio.h>
#include <stdlib.h>

int main() {
    int sideA, sideB, sideC;
    char input[10];

    printf("Enter length of side A: ");
    fgets(input, sizeof(input), stdin);
    sideA = atoi(input);

    printf("Enter length of side B: ");
    fgets(input, sizeof(input), stdin);
    sideB = atoi(input);

    printf("Enter length of side C: ");
    fgets(input, sizeof(input), stdin);
    sideC = atoi(input);

    if (sideA <= 0 || sideB <= 0 || sideC <= 0) {
        printf("Triangle type is invalid.\n");
        return 0;
    }

    if (sideA + sideB <= sideC || sideA + sideC <= sideB || sideB + sideC <= sideA) {
        printf("Triangle type is invalid.\n");
    }
    else if (sideA == sideB && sideB == sideC) {
        printf("Triangle type is equilateral.\n");
    }

    else if (sideA == sideB || sideB == sideC || sideA == sideC) {
        printf("Triangle type is isosceles.\n");
    }

    else {
        printf("Triangle type is scalene.\n");
    }

    return 0;
}
