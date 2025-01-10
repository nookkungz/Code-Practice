#include <stdio.h>
#include <stdlib.h>

int main() {
    long long n;
    
    printf("Input n = ");
    scanf("%lld", &n);
    
    long long s = n * n;
    long long temp = n;
    long long d = 1;
    while (temp > 0) {
        d *= 10;
        temp /= 10;
    }
    
    printf("n^2 = %lld\n", s);
    
    if (s % d == n) {
        printf("Yes. %lld is automorphic number.\n", n);
    } else {
        printf("No. %lld is not automorphic number.\n", n);
    }
    
    return 0;
}