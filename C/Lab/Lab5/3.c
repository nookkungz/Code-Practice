#include <stdio.h>
#include <stdlib.h>

void shift_left(char str[], int n) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    if (len == 0) return;  
    n = n % len; 

    for (int i = 0; i < n; i++) {
        char first = str[0];  


        for (int j = 0; j < len - 1; j++) {
            str[j] = str[j + 1];
        }

        str[len - 1] = first; 
    }
}
int main()
{  char str[80], *c;
   int n;

   printf("String: ");
   fgets(str, sizeof(str), stdin);
   for (c=str; *c && *c != '\n'; c++)
       ;
   *c = 0;
   printf("     n: ");
   scanf("%d", &n);
   shift_left(str, n);
   printf("Output: >>%s<<\n",str);
   return 0;
}