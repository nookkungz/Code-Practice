#include <stdio.h>
#include <stdlib.h>

int main () {

    int stick ,dis = 0;
    float price , result ;

    char input[10];
    fgets(input, sizeof(input), stdin);
    stick = atoi(input);

    fgets(input, sizeof(input), stdin);
    price = strtof(input, NULL);

    if (stick == 1) {
        result = (price-(price*(0.1)));
        dis = 10;
        stick -= 1 ;
    } else if (stick == 2) {
        result = (price-(price*(0.15))); 
        dis = 15;
        stick -= 2 ;
    } else if (stick >= 3 && stick < 6 ) {
        result = (price-(price*(0.2)));
        dis = 20;
        stick -= 3 ;
    } else if (stick >= 6 && stick < 9) {
        result = (price-(price*(0.3)));
        dis = 30;
        stick -= 6 ;
    } else if (stick >= 9) {
        result = (price-(price*(0.4)));
        dis = 40;
        stick -= 9 ;
    } else if (stick == 0)
    {
        dis = 0 ;
        result = price ;
    }



    printf("You get %d percents discount.\n", dis);
    printf("Total amount due is %.2f Baht.\n", result);
    printf("And you have %d stickers left.", stick);


}