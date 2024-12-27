#include <stdio.h>

int main() {
    int N;
    char input[10];
    fgets(input, sizeof(input), stdin);
    N = atoi(input);
    
    char top = 'a' + (N - 1);
    int total = 2 * N - 1;
    if( N <= 0 || N > 26){
        printf("-");
    }
    else{ 
        for (int i = 0; i < total; i++) {
        int r = (i < N) ? i : (2 * N - 2 - i);
        
        int s = 2 * (N - 1 - r);
        for (int d = 0; d < s; d++) {
            printf("-");
        }
        
        for (int k = 0; k <= r; k++) {
            printf("%c", (char)(top - k));
            if (k < r) {
                printf("-");
            }
        }
        
        for (int k = r - 1; k >= 0; k--) {
            printf("-%c", (char)(top - k));
        }
        
        for (int d = 0; d < s; d++) {
            printf("-");
        }
        
        printf("\n");
    }
    }
    
    return 0;
}
