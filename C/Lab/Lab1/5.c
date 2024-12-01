#include <stdio.h> 

int main (){
    int amount = 98 ;

    int one , five , twen , fif = 0 ;
    fif = amount/50 ;
    amount -= (fif*50) ;
    twen = amount/20 ;
    amount -= (twen*20) ;
    five = amount/5 ;
    amount -= (five*5) ;
    one = amount ;
    printf("1: %d\n5: %d\n20: %d\n50: %d",one , five , twen , fif) ;


    return 0 ;
}