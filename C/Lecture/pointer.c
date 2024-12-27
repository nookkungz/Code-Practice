#include <stdio.h>
#include <stdlib.h>

int main() {
    int i = 21;
    printf("value of i: %d\n", i);
    printf("address of i: %p\n", &i);
    printf("value of i: %p\n", *(&i));
    printf("address of i: %p\n", &(*(&i)));
    // ใส่ * หนเ้า & ได้ value 
    // AMPERSAND &

    int *iPtr;
    iPtr = &i;

    int*ipointer = &i;

    printf(" iPtr: %p\n", iPtr);
    printf(" *iPtr: %p\n", *iPtr);


    *iPtr = 30;
    printf(" iPtr: %p\n", iPtr);
    printf(" *iPtr: %p\n", *iPtr);
    printf(" *iPtr: %p\n", *iPtr);



    char str[100];
    int a ;
    int b
    scanf("%s", str);

    scanf("%d", &a);


    return 0;
}