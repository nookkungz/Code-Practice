#include <stdio.h>
#include <stdlib.h>

int main() {
    char x_str[5], y_str[5];
    int x, y;

    printf("Enter the x coordinate: ");
    fgets(x_str, 5, stdin);
    x = atoi(x_str);

    printf("Enter the y coordinate: ");
    fgets(y_str, 5, stdin);
    y = atoi(y_str);

    if (x == 0 && y == 0) {
        printf("Center\n");
    } else if (y > 0 && x == 0) {
        printf("North\n");
    } else if (y < 0 && x == 0) {
        printf("South\n");
    } else if (x > 0 && y == 0) {
        printf("East\n");
    } else if (x < 0 && y == 0) {
        printf("West\n");
    } else if (x > 0 && y > 0) {
        printf("North-east\n");
    } else if (x < 0 && y > 0) {
        printf("North-west\n");
    } else if (x > 0 && y < 0) {
        printf("South-east\n");
    } else if (x < 0 && y < 0) {
        printf("South-west\n");
    }

    return 0;
}