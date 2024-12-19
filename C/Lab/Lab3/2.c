#include <stdio.h>
#include <stdlib.h>

int main() {
    char input1[20], input2[20];
    long long m, n, original_m, original_n, gcd, lcm;
    fgets(input1, sizeof(input1), stdin);
    fgets(input2, sizeof(input2), stdin);
    m = atoll(input1);
    n = atoll(input2);
    original_m = m;
    original_n = n;
    while (n != 0) {
        long long temp = n;
        n = m % n;
        m = temp;
    }
    gcd = m;
    lcm = (original_m / gcd) * original_n;
    printf("GCD: %lld\n", gcd);
    printf("LCM: %lld\n", lcm);
}
