#include <stdio.h>
int main () {

    int computer_time = 670 ;
    int d=0 , h=0 , m=0 , s=0 ;

    d = computer_time/1440 ;
    computer_time -= d*1440 ;
    h = computer_time/60 ;
    computer_time -= h*60 ;
    m = computer_time ;
    printf("It is %d days %d hours and %d minutes. \n",d,h,m); 

    
    return 0; // error code that mean not error after here 
}