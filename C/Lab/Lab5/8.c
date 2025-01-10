#include <stdio.h>
#include <stdlib.h>
int main() {
    int stairs, step = 1, round = 1;
    int current_pos = 0;  
    printf("Input number of stairs: ");
    scanf("%d", &stairs);
    
    while (step != 0) {
        int i;
        printf("---- round %d ----\n", round);
        
        for (i = stairs - 1; i >= 0; i--) {
            if (i == current_pos + 1) {
                printf("|-O-|\n");  
            } else if (i == current_pos) {
                printf("|-^-|\n"); 
            } else {
                printf("|---|\n"); 
            }
        }

        printf("Input step command: ");
        scanf("%d", &step);
        current_pos += step;
        if (current_pos < 0) {
            current_pos = 0; 
        }
        if (current_pos > stairs - 2) {
            current_pos = stairs - 2; 
        }
        round++;
    }
    
    return 0;
}