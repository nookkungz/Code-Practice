#include <stdio.h>

void convert(char time12[], char time24[]) {
    int hour, minute;
    char period[3];
    sscanf(time12, "%d:%d %s", &hour, &minute, period);
    if ((period[0] == 'p' || period[0] == 'P') && (period[1] == 'm' || period[1] == 'M')) {
        if (hour != 12) {
            hour += 12;
        }
    } else if ((period[0] == 'a' || period[0] == 'A') && (period[1] == 'm' || period[1] == 'M')) {
        if (hour == 12) {
            hour = 0;
        }
    }
    sprintf(time24, "%02d:%02d", hour, minute);
}

int main() {
    char time12[10], time24[10];
    int i;

    printf("Enter a 12-hour time [eg. 12:34 am]: ");
    fgets(time12, sizeof(time12), stdin);
    for (i = 0; time12[i] != '\0'; i++) {
        if (time12[i] == '\n') {
            time12[i] = '\0';
            break;
        }
    }
    convert(time12, time24);
    printf("Equivalent 24-hour time: %s\n", time24);

    return 0;
}
