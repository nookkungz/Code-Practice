#include <stdio.h>

int main() {
    float goal, collect, total = 0.0;
    int days = 0;

    printf("Enter your goal amount: ");
    scanf("%f", &goal);

    while (total < goal) {
        printf("Enter money collected today: ");
        scanf("%f", &collect);

        days++;
        total += collect;

        if (total < goal) {
            printf("Total money collected up to day %d is %.2f. You need %.2f more.\n", 
                   days, total, goal - total);
        } else {
            if (days == 1) {
                printf("Congratulations! You take %d day to reach your goal.\n", days);
            } else {
                printf("Congratulations! You take %d days to reach your goal.\n", days);
            }
        }
    }

    return 0;
}
