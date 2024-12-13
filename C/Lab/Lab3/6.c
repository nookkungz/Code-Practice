#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    char input_x[10], input_y[10];

    printf("Input x: ");
    fgets(input_x, 10, stdin);
    printf("Input y: ");
    fgets(input_y, 10, stdin);

    double x, y;
    char input_command;

    x = atof(input_x);
    y = atof(input_y);

    printf("x = %5.4f, y = %5.4f\n", x, y);
    printf("[a]:Add [s]:Subtract [m]:Multiply [d]:Divide [M]:modulo [^]: x^y\n");
    printf("Command? ");
    input_command = getchar();

    switch (input_command) {
    case 'a':
        printf("x + y = %5.4lf\n", x+y);
        break;
    case 's':
        printf("x - y = %5.4lf\n", x-y);
        break;
    case 'm':
        printf("x * y = %5.4lf\n", x*y);
        break;
    case 'd':
        printf("x / y = %5.4lf\n", x/y);
        break;
    case 'M':
        printf("x mod y = %5.4lf\n",  fmod(x , y ));
        break;
    case '^':
        printf("x ^ y = %5.4lf\n", pow(x,y));
        break;
    default :
        printf("Unknown Command.\n");
        break;
    }
    return 0;

}