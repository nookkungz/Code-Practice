#include <stdio.h>
int main()
{
    float preGrade = 1.75;
    int preCredit = 21;
    int credit = 18;
    float requiredGrade = 2.00;
    float needGrade = 0 ;

    needGrade = ((requiredGrade * (preCredit+credit)) - (preGrade*preCredit))/credit ;

    printf("The GPA this semester should be %.2f",needGrade);

    return 0;
}