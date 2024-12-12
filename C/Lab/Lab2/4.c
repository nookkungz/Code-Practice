#include <stdio.h>
#include <stdlib.h>

int main () {

    float salary = 0 , tax = 0 ;
    char input[10] ;

    fgets(input, sizeof(input), stdin);
    salary = strtof(input, NULL) ;

    if (salary >= 0 ) {
        if (salary >= 300000){
            tax += (300000*0.05);
            salary -= 300000;
            if (salary > 0) {
                tax += (salary*0.1);
            }
        } else 
        {
            tax = (salary*(0.05));
        }
        printf("%.2f\n",tax);
        
    } else {
        printf("Error: Salary must be greater or equal to 0");
    }
}
    
    

