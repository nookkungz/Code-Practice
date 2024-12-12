#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    char size_str[5], pepperoni_str[5], cheese_str[5], mushroom_str[5];
    int size, pepperoni, cheese, mushroom;

    double diameter, area, cost, price;
    double fixed_cost = 5.0, base_cost = 2.0, extracost = 0.0;

    printf("Welcome to My Pizza Shop!!\n");
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~\n");

    printf("Enter pizza size (1=s, 2=m, or 3=l): ");
    fgets(size_str, 5, stdin);
    size = atoi(size_str);

    if (size == 1) diameter = 10.0;  
    else if (size == 2) diameter = 16.0;  
    else if (size == 3) diameter = 20.0; 
    else {
        printf("Invalid pizza size.\n");
        return 0;
    }

    printf("Extra pepperoni? (1=yes, 0=no): ");
    fgets(pepperoni_str, 5, stdin);
    pepperoni = atoi(pepperoni_str);

    printf("Extra cheese? (1=yes, 0=no): ");
    fgets(cheese_str, 5, stdin);
    cheese = atoi(cheese_str);

    printf("Extra mushroom? (1=yes, 0=no): ");
    fgets(mushroom_str, 5, stdin);
    mushroom = atoi(mushroom_str);

  
    area = M_PI * (diameter * diameter) / 4.0;

    extracost = 0.0;
    if (pepperoni == 1) extracost += 0.5;
    if (cheese == 1) extracost += 0.25;
    if (mushroom == 1) extracost += 0.3;

    cost = fixed_cost + (base_cost * area) + (extracost * area);
    price = 1.5 * cost;


    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("Your order costs %.2f baht.\n", price);
    printf("Thank you.\n");

    return 0;
}
