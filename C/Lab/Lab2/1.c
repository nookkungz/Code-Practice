#include <stdio.h>
#include <stdlib.h>
int main()
{
    char hour_str[3], min_str[3];
    int hour, min;

    printf("Enter hour: ");
    fgets(hour_str, 24, stdin);

    printf("Enter minute: ");
    fgets(min_str, 60, stdin);

    hour = atoi(hour_str);
    min = atoi(min_str);

    printf("Time is %02d:%02d\n", hour, min);
    return 0;
}